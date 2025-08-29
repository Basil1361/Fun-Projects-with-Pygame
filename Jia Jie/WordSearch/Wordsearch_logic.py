import sys, random, string, copy

def can_place_word(grid, word, r, c, d, n):
    for i in range(len(word)):
        if d == "horizontal":
            if grid[r][c + i] not in (" ", word[i]):
                return False
        elif d == "vertical":
            if grid[r + i][c] not in (" ", word[i]):
                return False
        elif d == "diagonal":
            if grid[r + i][c + i] not in (" ", word[i]):
                return False
    return True

def place_word(grid, word, r, c, d):
    placed = []
    for i in range(len(word)):
        if d == "horizontal":
            grid[r][c + i] = word[i]
            placed.append((r, c + i))
        elif d == "vertical":
            grid[r + i][c] = word[i]
            placed.append((r + i, c))
        elif d == "diagonal":
            grid[r + i][c + i] = word[i]
            placed.append((r + i, c + i))
    return placed  # returns the list of positions

def undo_word(grid, placed):
    for r, c in placed:
        grid[r][c] = " "

def backtrack(grid, words, idx, n, directions, placements):
    if idx == len(words):
        return True
    word = words[idx].upper()
    positions = []
    for r in range(n):
        for c in range(n):
            for d in directions:
                if d == "horizontal" and c + len(word) <= n:
                    positions.append((r, c, d))
                elif d == "vertical" and r + len(word) <= n:
                    positions.append((r, c, d))
                elif d == "diagonal" and r + len(word) <= n and c + len(word) <= n:
                    positions.append((r, c, d))
    random.shuffle(positions)
    for r, c, d in positions:
        if can_place_word(grid, word, r, c, d, n):
            placed = place_word(grid, word, r, c, d)
            # Record start and end position
            start = (r, c)
            if d == "horizontal":
                end = (r, c + len(word) - 1)
            elif d == "vertical":
                end = (r + len(word) - 1, c)
            elif d == "diagonal":
                end = (r + len(word) - 1, c + len(word) - 1)

            placements.append((word, start, end))

            if backtrack(grid, words, idx + 1, n, directions, placements):
                return True

            # Undo if failed
            undo_word(grid, placed)
            placements.pop()
    return False

def create_crossword(order: int, words: list):
    # basic validation
    if len(words) > 20:
        raise ValueError("Total number of words limit excedded.")
    for w in words:
        if len(w) == 0:
            raise ValueError("Empty words are not allowed.")
        if len(w) > order:
            raise ValueError(f"'{w}' is too long for grid size {order}.")
    total = sum(len(w) for w in words)
    if total > order * order:
        raise ValueError("Total character length exceeds grid capacity.")

    # grid
    grid = [[" " for _ in range(order)] for _ in range(order)]
    words_sorted = sorted(words, key=len, reverse=True)
    directions = ["horizontal", "vertical", "diagonal"]
    placements = []  # list of (word, start, end)

    if not backtrack(grid, words_sorted, 0, order, directions, placements):
        raise ValueError("Could not place all words. Try different words or a larger grid.")
    return grid, placements

def add_random_letters(order, grid):
    letters = string.ascii_uppercase
    for r in range(order):
        for c in range(order):
            if grid[r][c] == " ":
                grid[r][c] = random.choice(letters)
    return grid

def make_answer_view(order, grid):
    # convert blanks to dots
    ans = copy.deepcopy(grid)
    for r in range(order):
        for c in range(order):
            if ans[r][c] == " ":
                ans[r][c] = "."
    return ans

def grid_to_str(grid):
    return "\n".join("".join(row) for row in grid)
