class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #declaration
        end = 0
        s = []
        #declaration end
        #logic
        for i in senate:
            s.append(i)
        while end<=len(s)-1:
            if 'R' not in s:
                return "Dire"
            if 'D' not in s:
                return "Radiant"

            if s[end] == 'R':
                #print("If executing")
                if end!=len(s)-1 and 'D' in s[end+1:len(s)]:
                    idx = s[end+1:len(s)].index('D') + (end + 1)
                    s[idx] = 'X'
                else:
                    k = 0
                    idx = s[k:len(s)-1].index('D')
                    s[idx] = 'X'
            elif s[end] == 'D':
                #print("elif executing")
                if end!=len(s)-1 and 'R' in s[end+1:len(s)]:
                    idx = s[end+1:len(s)].index('R') + (end + 1)
                    s[idx] = 'X'
                else:
                    k = 0
                    idx = s[k:len(s)-1].index('R')
                    s[idx] = 'X'
            else:
                #print("else executing")
                pass
            
            #print(s)

            if end==len(s)-1:
                end = 0
            else:
                end = end+1
        #logic end