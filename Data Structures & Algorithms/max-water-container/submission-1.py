class Solution:

    def maxArea(self,heights: list[int]) -> int:

        if not heights:
            return 0

        l, r, vol = 0, len(heights)-1, 0
        left_max, right_max = heights[0], heights[r]

        while l<r:

            curr_vol = min(heights[l], heights[r]) * (r-l)
            vol = max(curr_vol, vol)

            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
                

            else:
                r -= 1
                right_max = max(right_max, heights[r])
                

        return vol

