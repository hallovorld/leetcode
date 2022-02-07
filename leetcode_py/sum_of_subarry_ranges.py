class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Monotonic Stack + DP
        """
        
        l = len(nums)
        
        s = [0]
        
        sumMax = [i for i in nums]
        sumMin = [i for i in nums]
        
        for i in range(1,l):
            if nums[i] >= nums[i-1]:
                sumMin[i] = sumMin[i-1] + nums[i]
            else:
                while s and nums[s[-1]] > nums[i]:
                    s.pop(-1)
                    
                if s == []:
                    sumMin[i] = nums[i] * (i+1)
                else:
                    sumMin[i] = sumMin[s[-1]] + nums[i]*(i-s[-1])
                    
            s.append(i)
            
        s = [0]
        
        for i in range(1,l):
            if nums[i] <= nums[i-1]:
                sumMax[i] = sumMax[i-1] + nums[i]
            else:
                while s and nums[s[-1]] < nums[i]:
                    s.pop(-1)
                    
                if s == []:
                    sumMax[i] = nums[i] * (i+1)
                else:
                    sumMax[i] = sumMax[s[-1]] + nums[i] * (i-s[-1])
            s.append(i)
            
        
        return sum(sumMax) - sum(sumMin)
           