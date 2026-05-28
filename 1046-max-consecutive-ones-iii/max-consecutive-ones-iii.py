class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #declaration
        start = 0
        end = 0
        max_count = 0
        #declration end
        #logic
        while(end < len(nums)):
            if(nums[end]==0):
                k = k-1
            while k<0:
                if(nums[start]==0):
                    k+=1
                start=start+1
            max_count = max(max_count,end-start+1)
            end = end+1
        return max_count
        #logic end