class Solution:
    def maxArea(self, height: List[int]) -> int:
        #checking
        areas = []
        area = 0
        init_pos_l = 0
        left_p = height[0]
        init_pos_r = -1
        right_p = height[init_pos_r]
        width = len(height)-1
        #checking end
        #logic
        #initial area
        area = width * min(left_p,right_p)
        areas.append(area)
        #initial area
        for i in range(0,len(height)-1):
            area = width * min(left_p,right_p)
            areas.append(area)
            if(left_p<right_p):
                init_pos_l = init_pos_l + 1
                left_p = height[init_pos_l]
            else:
                init_pos_r = init_pos_r - 1
                right_p = height[init_pos_r]
            width = width - 1
        return max(areas)
        #logic end
        