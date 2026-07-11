class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        check = {}

        for i in s:

            if i in check.keys():
                check[i]+=1
            else:
                check[i] = 1

        for i in t:

            if i in check.keys() and check[i] > 0:
                check[i]-=1

            elif i in check.keys() and check[i] <= 0:
                return False

            elif i not in check.keys():
                return False

        return True



