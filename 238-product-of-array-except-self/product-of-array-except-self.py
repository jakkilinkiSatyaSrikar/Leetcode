import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #checking
        if(len(nums)<2 or len(nums)>10**5):
            return None
        for i in nums:
            if(i<-30 or i>30):
                return None
        #checking end
        #declaration
        d = -1
        temp = []
        prefix = []
        postfix = []
        #declaration end
        #logic
        for i in range(len(nums)):
            if(i==0):
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1]*nums[i])
        for i in range(0,(len(nums))):
            if(i==0):
                postfix.append(nums[-1])
            else:
                d = d-1
                postfix.append(postfix[i-1]*nums[d])
        postfix = postfix[::-1]
        for i in range(len(nums)):
            if(i==0):
                temp.append(1 * postfix[i+1])
            elif(i==len(nums)-1):
                temp.append(prefix[i-1] * 1)
            else:
                temp.append(prefix[i-1]*postfix[i+1])
        print(prefix,postfix)
        #logic end
        return temp

obj = Solution()
nums = []
r = obj.productExceptSelf(nums)