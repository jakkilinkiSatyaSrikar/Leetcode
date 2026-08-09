class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        li = [0,1,1]
        i = 0
        current_sum = 2
        while i<n-2:
            ''' n = 6
                0 1 1
                i
                0 1 1 2
                  i
                current_sum = (li[i-1]-current_sum)+li[i+2]
                current_sum = 4
                0 1 1 2 4
                    i
                current_sum = (li[i-1]-current_sum)+li[i+2]
                current_sum = 7
                0 1 1 2 4 7
                      i = 4
                      condition fails
                      return current_sum
                        '''
            li.append(current_sum)
            i+=1
            current_sum = (current_sum-li[i-1])+li[i+2]
        # print(li)
        return li[-1]
        