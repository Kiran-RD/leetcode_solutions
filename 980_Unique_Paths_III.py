class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs()



        ways = 0
        empty = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x, y = row, col

                if grid[row][col] == 0:
                    empty += 1

