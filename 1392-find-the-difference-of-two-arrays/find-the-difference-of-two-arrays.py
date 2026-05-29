class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = []
        pos = 0
        temp = []
        for i in nums1:
            if(i not in nums2) and (i not in temp):
                temp.append(i)
        output.append(temp)
        temp = []
        for i in nums2:
            if((i not in nums1) and (i not in temp)):
                temp.append(i)
        output.append(temp)
        return output
                