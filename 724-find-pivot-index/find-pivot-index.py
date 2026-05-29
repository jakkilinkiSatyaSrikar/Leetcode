class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = -1
        left_sum = 0
        right_sum = 0
        flag = 0
        for i in range(0,len(nums)):
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1:len(nums)])
            if(left_sum == right_sum):
                flag = 1
                return i
        if(flag == 0):
            return -1
        if(nums == sorted(nums)):
            return -1