class RecentCounter:

    def __init__(self):
        self.q = []
        self.count = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        #print(self.q)
        time_line = []
        time_line.append(self.q[-1] - 3000)
        time_line.append(self.q[-1])
        #print(time_line)
        i = 0
        while self.q and i<len(self.q):
            #print(self.q[i])
            if self.q[i]<time_line[0] or self.q[i]>time_line[-1]:
                self.q.pop(i)
            else:
                i = i+1
        if len(self.count) == 0:
            self.count.append(1)
        else:
            self.count.append(len(self.q))
        return self.count[-1]
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
# print(obj.ping(1))
# param_1 = obj.ping(t)