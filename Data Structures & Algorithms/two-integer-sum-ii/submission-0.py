class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        seen= {}

        for i in range(len(numbers)):

            diff = target - numbers[i]

            if diff not in seen:
                seen[numbers[i]] = i+1

            else:
                return [seen[diff], i+1]

        return []

