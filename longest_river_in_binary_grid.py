class River():
    def longest_path_from_this_position(self,node, grid):
        x, y = node
        grid[x][y] = 1
        size = 0
        n = len(grid)
        m = len(grid[0])

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
            new_x, new_y = x + dx, y+dy
            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 0:
                size += self.longest_path_from_this_position((new_x, new_y), grid)
        return size + 1


    def find_max_path(self,grid):
        ans = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    ans = max(ans, self.longest_path_from_this_position((i, j), grid))
        return ans
grid=[ [0, 1, 1, 1, 1], [1, 1, 0, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1]]
river=River()
print(river.find_max_path(grid))