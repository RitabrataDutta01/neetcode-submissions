class Solution:

    def threeSum(self, nums:list[int]) -> list[list[int]]:

        result = []

        nums.sort()

        for i in range(len(nums)):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            target = 0
            target -= nums[i]
            l,r = i+1, len(nums) -1

            while(l<r):
                curr_sum = nums[l] + nums[r]

                if curr_sum == target:

                    result.append([nums[i],nums[l],nums[r]])

                    l+=1
                    r-=1

                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1

                elif curr_sum < target:
                    l+=1 
                elif curr_sum > target:
                    r-=1 

        return result

