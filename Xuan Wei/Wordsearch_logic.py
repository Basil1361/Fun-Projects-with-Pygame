import sys, random, string, copy

def can_place_word(grid, word, row, col, direction, n):
    for i in range(len(word)):
        r, c = row, col
        if direction == "horizontal":
            c += i
        elif direction == "vertical":
            r += i
        elif direction == "diagonal":
            r += i; c += i
        if r >= n or c >= n:
            return False
        cell = grid[r][c]
        if cell != " " and cell != word[i]:
            return False
    return True

def place_word(grid, word, row, col, direction):
    placed = []
    for i, ch in enumerate(word):
        r, c = row, col
        if direction == "horizontal":
            c += i
        elif direction == "vertical":
            r += i
        else:  # diagonal
            r += i; c += i
        if grid[r][c] == " ":
            grid[r][c] = ch
            placed.append((r, c))
    return placed

def undo_word(grid, placed):
    for r, c in placed:
        grid[r][c] = " "

def backtrack(grid, words, idx, n, directions):
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
            if backtrack(grid, words, idx + 1, n, directions):
                return True
            undo_word(grid, placed)
    return False

def create_crossword(order: int, words: list) -> list:
    # basic validation
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

    # place
    words_sorted = sorted(words, key=len, reverse=True)
    directions = ["horizontal", "vertical", "diagonal"]
    if not backtrack(grid, words_sorted, 0, order, directions):
        raise ValueError("Could not place all words. Try different words or a larger grid.")
    return grid

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

question = create_crossword(10, ["apple", "hell"])
add_random_letters(10, question)
question = grid_to_str(question)
print(question)

