class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #declarations
        col = []
        temp = []
        count = 0
        #declarations end
        #logic
        print(len(grid))
        for i in range(0,len(grid)):
            for k in range(0,len(grid)):
                temp.append(grid[k][i])
            col.append(temp)
            temp = []

        print(col)
        for i in grid:
            print(i)
            if(i in grid):
                a = col.count(i)
                print(a)
                count = count +a
        
        return count
        #logic ends