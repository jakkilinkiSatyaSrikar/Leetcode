class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        for i in word1:
            if(i not in word2):
                return False
        for i in word2:
            if(i not in word1):
                return False
        #declaration
        w1 = {}
        w2 = {}
        visited = []
        w1_list =[]
        w2_list =[]
        #declaration end
        #logic
        for i in word1:
            if i not in visited:
                w1[i] = word1.count(i)
                w1_list.append(word1.count(i))
                visited.append(i)
        visited = []
        for i in word2:
            if i not in visited:
                w2[i] = word2.count(i)
                w2_list.append(word2.count(i))
                visited.append(i)
        for i in w1.values():
            print(i)
            print(i in w2_list)
            if i in w2_list:
                print(w2_list)
                ind = w2_list.index(i)
                w2_list.pop(ind)
                print(w2_list)
        if(len(w2_list)==0):
            return True
        else:
            return False
        #logic end