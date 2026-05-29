class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #checking
        if(len(gain)<1 or len(gain)>100):
            return None
        #checking end
        #declaration
        initial = 0
        alt_arr = []
        max_alt = 0
        #declaration end
        #logic
        alt_arr.append(initial)
        for i in gain:
            initial = initial + i
            alt_arr.append(initial)
        for i in alt_arr:
            if(i>max_alt):
                max_alt = i
        return max_alt
        #logic end
        