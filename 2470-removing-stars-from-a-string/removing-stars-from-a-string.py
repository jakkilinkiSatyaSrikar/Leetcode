class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        index = -1
        for i in s:
            #print(stack)
            if(index == -1):
                stack.append(i)
            elif(i == '*'):
                stack.pop()
            else:
                stack.append(i)
            index = index+1
        s = ""
        for i in stack:
            s = s+i
        return s  