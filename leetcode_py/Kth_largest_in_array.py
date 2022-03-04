"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        
        class heap():
            def __init__(self):
                self.array = []
            
            def len(self):
                return len(self.array)
            
            def switch(self, i, j):
                tmp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = tmp
            
            def top(self):
                return self.array[0]
                
            def add(self, val):
                self.array.append(val)
                self._swim()
            
            def pop(self):
                self.switch(0,-1)
                self.array.pop(-1)
                self._sink()
                
            def build(self, array):
                self.array = array
                l = len(array)
                for i in range(l):
                    self._swim(i)
                    
            def _swim(self, cp=None):
                # print 'swim', self.array
                if cp is None:
                    cp = len(self.array)-1
                if cp%2 == 1:
                    fp = (cp-1)/2
                else:
                    fp = (cp-2)/2
                
                while fp>=0 and self.array[fp] > self.array[cp]:
                    self.switch(fp, cp)
                    cp = fp
                    if cp%2 == 1:
                        fp = (cp-1)/2
                    else:
                        fp = (cp-2)/2
                # print 'end swim', self.array
                    
            
            def _sink(self, cp=None):
                # print 'sink', self.array
                if cp is None:
                    cp = 0
                left = cp*2+1
                right = cp*2+2
                
                while left < self.len():
                    if right < self.len():
                        if self.array[cp] > min(self.array[left], self.array[right]):
                            if self.array[left] < self.array[right]:
                                self.switch(left, cp)
                                cp = left
                                left = cp*2+1
                                right = cp*2+2
                            else:
                                self.switch(right, cp)
                                cp = right
                                left = cp*2+1
                                right = cp*2+2
                        else:
                            break
                    else:
                        # right is out of range
                        if self.array[cp] > self.array[left]:
                            self.switch(left, cp)
                            cp = left
                            left = cp*2+1
                            right = cp*2+2
                        else:
                            break
                # print 'end sink', self.array
                            
                            
        h = heap()
        
        for i in nums:
            if h.len() < k:
                h.add(i)
            else:
                if i > h.top():
                    h.pop()
                    h.add(i)
                    
        # or         
        h.build(nums)
        for _ in range(len(nums)-k):
            h.pop()
        
        return h.top()
                    