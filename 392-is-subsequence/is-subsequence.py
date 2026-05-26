class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #checking
        if(len(s)<0 or len(s)>100):
            return None
        if(len(t)<0 or len(t)>10**4):
            return None
        #checking end
        #declaration
        count = 0
        length = 0
        #declaration end
        #logic
        if(len(s)<1):
            return True
        for i in t:
            if(s[count]==i):
                length = length +1
                count = count + 1
                if(count>=(len(s))):
                    break
        if(length==len(s)):
            return True
        else:
            return False
        #logic end