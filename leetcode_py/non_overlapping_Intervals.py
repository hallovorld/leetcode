"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count = 0
        
        intervals.sort(key=lambda k:k[1])
        intervals.sort(key=lambda k:k[0])
        
        s = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < s[-1][1]:
                count += 1
                if intervals[i][1] < s[-1][1]:
                    s.pop(-1)
                    s.append(intervals[i])
            else:
                s.append(intervals[i])
                
        print s
        print count
        return count