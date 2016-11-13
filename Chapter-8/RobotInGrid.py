grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
path = []


def find_path(grid):
    if grid is not None or len(grid) != 0:
        return cal_path(grid, len(grid)-1, len(grid[0]) - 1, path)
    else:
        return None


def cal_path(matrix, r, c, path):
    if r < 0 or c < 0 or not matrix[r][c]:
        return False

    is_at_origin = (r == 0) and (c == 0)
    if is_at_origin or cal_path(matrix, r - 1, c, path) or cal_path(matrix, r, c - 1, path):
        path.append((r, c))
        return True
    return False


print find_path(grid)
for i in path:
    print i
