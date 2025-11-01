import sys
from collections import deque

def read_maze(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def find_start_target(maze):
    start = target = None
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'T':
                target = (r, c)
    return start, target

def get_neighbors(maze, pos):
    r, c = pos
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = []
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[r]) and maze[nr][nc] != '#':
            res.append((nr, nc))
    return res

def bfs(maze, start, target):
    q = deque([start])
    parent = {start: None}
    while q:
        cur = q.popleft()
        if cur == target:
            return parent
        for neigh in get_neighbors(maze, cur):
            if neigh not in parent:
                parent[neigh] = cur
                q.append(neigh)
    return {}

def dfs(maze, start, target):
    stack = [start]
    parent = {start: None}
    while stack:
        cur = stack.pop()
        if cur == target:
            return parent
        for neigh in get_neighbors(maze, cur):
            if neigh not in parent:
                parent[neigh] = cur
                stack.append(neigh)
    return {}

def build_path(parent, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]

def print_solution(maze, path, start, target):
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    grid = [list(row) for row in maze]
    path_set = set(path)
    for r, c in path_set:
        if (r, c) != start and (r, c) != target:
            grid[r][c] = RED + '*' + RESET
    sr, sc = start
    tr, tc = target
    grid[sr][sc] = YELLOW + 'S' + RESET
    grid[tr][tc] = GREEN + 'T' + RESET
    for row in grid:
        print(''.join(row))

def main():
    if len(sys.argv) != 3:
        print("Usage: python search_maze.py <bfs|dfs> <maze_file>")
        sys.exit(1)
    alg = sys.argv[1].lower()
    filename = sys.argv[2]
    maze = read_maze(filename)
    start, target = find_start_target(maze)
    if alg == 'bfs':
        parent = bfs(maze, start, target)
    elif alg == 'dfs':
        parent = dfs(maze, start, target)
    else:
        print("Algorithm must be bfs or dfs")
        sys.exit(1)
    if target not in parent:
        print("No path found")
        return
    path = build_path(parent, target)
    print_solution(maze, path, start, target)

if __name__ == "__main__":
    main()