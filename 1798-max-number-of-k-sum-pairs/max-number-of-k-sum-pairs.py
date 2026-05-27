from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #checking
        if(k<1 or k>10**9):
            return None
        if(len(nums)<1 or len(nums)>10**5):
            return None
        for i in nums:
            if(i<1 or i>10**9):
                return None
        #checking end
        #declaration
        d = defaultdict(int)
        pairs = 0
        #declaration end
        #logic
        for i in nums:
            if(d[k-i]>0):
                pairs = pairs+1
                d[k-i] -= 1
            else:
                d[i] += 1
        return pairs
        #logic end
        