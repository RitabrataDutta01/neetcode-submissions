from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        cols= defaultdict(set)
        rows= defaultdict(set)
        boxes= defaultdict(set)

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                if(val in cols[c] or val in rows[r] or val in boxes[(r//3, c//3)]):
                    return False

                cols[c].add(val)
                rows[r].add(val)
                boxes[(r//3, c//3)].add(val)

        return True
