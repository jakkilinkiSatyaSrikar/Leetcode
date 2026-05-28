class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #declaration
        starting = 0
        ending = k
        s = sum(nums[starting:ending])
        avg = s/k
        avgs = []
        avgs.append(avg)
        #declaration end
        #logic
        for i in range(1,len(nums)-k + 1):
            ending = ending+1
            s = (s + nums[ending-1]) - nums[starting]
            starting = starting + 1
            avg = s/k
            avgs.append(avg)
        #print(type(avgs))
        return max(avgs)
        #logic end