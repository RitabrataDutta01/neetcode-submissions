class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        prod = 1
        nan = 1
        for i in nums:
            if i==0:
                nan = 0
            else:
                prod*=i

        res = []

        for i in nums:
            
            if i!=0 and nan == 0:
                res.append(prod*0)
            elif i==0 and nan == 0:
                res.append(prod//1)
            else:
                res.append(prod//i)

        return res


