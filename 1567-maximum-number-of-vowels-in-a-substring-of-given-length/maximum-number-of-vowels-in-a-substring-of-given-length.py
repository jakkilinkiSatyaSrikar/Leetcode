class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #checking
        if(len(s)<1 or len(s)>10**5):
            return None
        for i in s:
            if(len(i)<1 or len(i)>len(s)):
                return None
        #checking end
        #declarations
        max_count = 0
        count1 = 0
        prev_window = s[0:k]
        vowels = ['a','e','i','o','u']
        for i in prev_window:
            if(i in vowels):
                count1 = count1+1
        max_count = count1
        #declarations end
        #logic
        print("prev_window:",prev_window)
        print("max_count:",max_count)
        for i in range(1,len(s)-k + 1):
            temp = s[i:i+k]
            if(temp[-1] in vowels):
                count1 = count1+1
            if(prev_window[0] in vowels):
                count1 = count1 - 1
            prev_window = temp
            if(count1>max_count):
                max_count = count1
        #logic end
        return max_count
        