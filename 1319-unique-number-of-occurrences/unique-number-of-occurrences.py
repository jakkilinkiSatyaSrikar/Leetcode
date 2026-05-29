class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        visited = []
        for i in arr:
            if(i not in visited):
                counts.append(arr.count(i))
                visited.append(i)
        return len(counts) == len(set(counts))
        