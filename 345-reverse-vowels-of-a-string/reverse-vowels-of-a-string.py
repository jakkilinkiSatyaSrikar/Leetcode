class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        L = 0
        R = len(s) - 1
        ns = ""
        while L < R:
            if s[L] in ['A','a','E','e','I','i','O','o','U','u'] and s[R] in ['A','a','E','e','I','i','O','o','U','u']:
                s[L],s[R] = s[R],s[L]
                L +=1
                R -=1
            if s[L] not in ['A','a','E','e','I','i','O','o','U','u']:
                L +=1
            if s[R] not in ['A','a','E','e','I','i','O','o','U','u']:
                R -=1
        return ns.join(s)
