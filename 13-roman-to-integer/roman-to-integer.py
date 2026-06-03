class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        s = s.upper()
        i = 0
        while(i<len(s)):
            if s[i] == 'I':
                print("s[i] == 'I'")
                if i<len(s) and s[i+1:i+2]== 'V':
                    res = res+4
                    print(res)
                    i = i+2
                elif i<len(s) and s[i+1:i+2]=='X':
                    res = res+9
                    print(res)
                    i = i+2
                else:
                    res = res+1
                    print(res)
                    i = i+1
            elif s[i] == 'V':
                print("s[i] == 'V'")
                res = res+5
                print(res)
                i = i+1
            elif s[i] == 'X':
                print("s[i] == 'X'")
                if i<len(s) and s[i+1:i+2]== 'L':
                    res = res+40
                    print(res)
                    i = i+2
                elif i<len(s) and s[i+1:i+2]=='C':
                    res = res+90
                    print(res)
                    i = i+2
                else:
                    res = res+10
                    print(res)
                    i = i+1
            elif s[i] == 'L':
                print("s[i] == 'L'")
                res = res + 50
                print(res)
                i = i+1
            elif s[i] == 'C':
                print("s[i] == 'C'")
                if i<len(s) and s[i+1:i+2]== 'D':
                    res = res+400
                    print(res)
                    i = i+2
                elif i<len(s) and s[i+1:i+2]=='M':
                    res = res+900
                    print(res)
                    i = i+2
                else:
                    res = res+100
                    print(res)
                    i = i+1
            elif s[i] == 'D':
                print("s[i] == 'D'")
                res = res+500
                print(res)
                i = i+1
            elif s[i] == 'M':
                print("s[i] == 'M'")
                res = res+1000
                print(res)
                i = i+1
        return res
        