class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #declaration section
        zero = []
        one = []
        pos = 0
        k = 0
        #declaration end
        #logic start
        for i in nums:
            if(i == 0):
                zero.append(i)
            else:
                one.append(i)
        if(len(one)!=0):
            for i in range(0,len(one)):
                nums[i] = one[i]
                pos = pos+1
        if(len(zero)!=0):
            for i in range(pos,len(nums)):
                nums[i] = zero[k]
                k = k+1
        #logic end
        