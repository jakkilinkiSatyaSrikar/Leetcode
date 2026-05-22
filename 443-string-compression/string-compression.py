class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars)<1 or len(chars)>2000):
            return None
        #declaration
        visited = []
        count = []
        count_str = ""
        pos = 0
        temp_count = 0
        prev = chars[0]
        #declaration end
        if(len(chars)==1):
            return len(chars)
        for i in range(0,len(chars)):
            if(len(visited) == 0):
                visited.append(chars[i])
                #print("i",i)
                #print("count",count)
                #print("visited",visited)                
                #temp_count=temp_count+1
            if(prev==chars[i] and i!=len(chars)-1):
                temp_count=temp_count+1
                prev = chars[i]
                #print("i",i)
                #print("count",count)
                #print("visited",visited)
            elif(prev==chars[i] and i == len(chars)-1):
                temp_count = temp_count+1
                temp_count = str(temp_count)
                count.append(temp_count)
                #print("i",i)
                #print("count",count)
                #print("visited",visited)
            elif(prev!=chars[i] and i == len(chars)-1):
                temp_count = str(temp_count)
                count.append(temp_count)
                temp_count = 0
                visited.append(chars[i])
                temp_count = temp_count+1
                prev = chars[i]
                temp_count = str(temp_count)
                count.append(temp_count)
                #print("i",i)
                #print("count",count)
                #print("visited",visited)
            else:
                temp_count = str(temp_count)
                count.append(temp_count)
                temp_count = 0
                visited.append(chars[i])
                temp_count = temp_count+1
                prev = chars[i]
                #print("i",i)
                #print("count",count)
                #print("visited",visited)                
        #print("count",count)
        '''for i in count:
            count_str = count_str+i
        count = []
        for i in count_str:
            count.append(i)
        print(type(count))
        print(count)'''
        for v,c in zip(visited,count):
            chars[pos] = v
            pos = pos+1
            #print("chars for ",v," ",c,":-",chars)
            if(c == '1'):
                pass
            elif(len(c)>1):
                for k in c:
                    chars[pos] = k
                    pos=pos+1
            else:
                chars[pos] = c
                pos = pos+1
            #print("chars for ",v," ",c,":-",chars)
        #print(chars)
        chars = chars[0:pos]
        if(len(visited)>len(count)):
            chars.extend(visited[pos:len(visited)])
        return len(chars)
        