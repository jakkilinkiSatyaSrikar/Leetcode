class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        count = 0
        k = 1
        long = []
        maxi = 0
        if(nums.count(0)<1):
            return len(nums) - 1
        
        while(end<len(nums)):
            if(nums[end]==0):
                # count = count+1
                k-=1
            else:
                count = count+1
            
            if k<0:
                long.append(count)
                while k<0:
                    if nums[start] == 0:
                        #count = count -1
                        k+=1
                    else:
                        count = count -1
                    start +=1 
            end +=1
        long.append(count)
        for i in long:
            if(i>maxi):
                maxi = i
        return maxi