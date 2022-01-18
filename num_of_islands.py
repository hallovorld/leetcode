class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        """
        m = len(grid) if grid else 0
        n = len(grid[0]) if grid[0] else 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [ [0 for j in range(n)] for i in range(m) ]
        ans = 0
        islands = []
        
        def check_point(x,y):
            if x < 0 or x >= m or y < 0 or y >= n:
                print("debug: ({}, {}) is out of range".format(x,y))
                return False
            if visited[x][y]:
                print("debug ({}, {}) visited".format(x,y))
                return False
            if grid[x][y] != "1":
                print("debug ({}, {}) is sea".format(x,y))
                return False
            return True
        
        def get_island_dfs_r(x,y,island_land=[]):
            if not check_point(x,y):
                return None
            
            visited[x][y] = 1
            island_land.append((x,y))
            print("debug: visiting ({}, {})".format(x,y))
            for direct in directions:
                get_island_dfs_r(x+direct[0], y+direct[1], island_land)
                
            return island_land
        
        def get_island_dfs_s(x,y):
            if not check_point(x,y):
                return None 
            
            s = [(x,y)]
            island_land = []
            while s:
                cx, cy = s.pop(-1)
                if check_point(cx,cy):
                    visited[cx][cy] = 1
                    island_land.append((cx,cy))
                    for direct in directions:
                        s.append((cx+direct[0], cy+direct[1]))
                
            return island_land
        
        def get_island_bfs_q(x,y):
            if not check_point(x,y):
                return None
            q = [(x,y)]
            island_land = []
            while q:
                cx, cy = q.pop(0)
                if check_point(cx,cy):
                    visited[cx][cy] = 1
                    island_land.append((cx,cy))
                    for direct in directions:
                        q.append((cx+direct[0], cy+direct[1]))
            return island_land
                
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    islands.append(get_island_dfs_r(i,j,[]))
                    # islands.append(get_island_dfs_s(i,j))
                    # islands.append(get_island_bfs_q(i,j))
         
            
        for island in islands:
            head = island[0]
            print("formatted island: {}".format(sorted([(i[0]-head[0], i[1]-head[1]) for i in island])))
                    
        return len(islands)
