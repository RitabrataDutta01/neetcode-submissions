class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        rep = {}

        for i in nums:

            rep[i] = rep.get(i,0) + 1

        group = {}

        for num,freq in rep.items():

            group.setdefault(freq, []).append(num)

        result = []
        for freq in sorted(group.keys(), reverse= True):
            result.extend(group[freq])
            if len(result) >= k:
                break

        return result[:k]
