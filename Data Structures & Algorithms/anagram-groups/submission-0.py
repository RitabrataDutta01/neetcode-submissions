class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]] :

        strings = {}

        for i in strs:

            counts = [0] * 26

            for char in i:
                if char.isalpha():
                    counts[ord(char)-ord('a')] +=1

            key = tuple(counts)

            strings.setdefault(key,[]).append(i)

        return list(strings.values())

