class Solution:

    def encode(self, strs: list[str]) -> str:

        encoded_strs = []
        for s in strs:

            encoded_strs.append(f"{len(s)}#{s}")

        return "".join(encoded_strs)

    def decode(self, s: str) -> list[str]:

        decoded_strs = []

        lenh = len(s)
        i=0

        while (i<lenh):

            hash_pos = s.index('#', i)

            length = int(s[i:hash_pos])

            start = hash_pos + 1
            end = start + length

            decoded_strs.append(s[start:end])

            i=end

        return decoded_strs
