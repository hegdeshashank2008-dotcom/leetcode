class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        # Initialize bitmasks
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    bit = 1 << num
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit

        def solve(k):
            if k == len(empty):
                return True

            r, c = empty[k]
            b = (r // 3) * 3 + c // 3

            mask = ~(rows[r] | cols[c] | boxes[b]) & 0x1FF

            while mask:
                bit = mask & -mask
                num = bit.bit_length()

                board[r][c] = str(num)

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if solve(k + 1):
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = "."

                mask &= mask - 1

            return False

        solve(0)