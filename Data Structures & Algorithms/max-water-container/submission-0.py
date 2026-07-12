class Solution:

    def maxArea(self,heights: list[int]) -> int:

        if not heights:
            return 0

        l, r, vol = 0, len(heights)-1, 0
        
        while l<r:

            curr_height = min(heights[l],heights[r])
            curr_width = r-l 
            
            vol = max(curr_height*curr_width, vol)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return vol
