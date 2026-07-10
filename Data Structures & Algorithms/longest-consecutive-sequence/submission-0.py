class Solution:

    def longestConsecutive(self, nums:list[int]) -> int:

        numList = set(nums)
        streak = 0

        for i in numList:

            prev= i-1
            if prev not in numList:

                curr = i
                curr_streak = 1
                while (curr+1) in numList:
                    curr +=1
                    curr_streak +=1

                if curr_streak > streak:
                    streak= curr_streak
                    
        return streak


