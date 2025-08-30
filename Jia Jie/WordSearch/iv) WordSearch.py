# only has 2d
# only has verti (down), hori (up). 

import random
import string

# customization
COLS = 8   # columns
ROWS = 8   # rows

def get_words(count: int, grid_size: int = COLS):
    words = []
    for i in range(count):
        while True:
            raw = input(f"Word {i+1}/{count}. (Letters only, 1–{grid_size} chars): ").strip()
            if not raw:
                print("Empty input, try again")
                continue
            if not raw.isalpha():
                print("Only letters. Try again")
                continue
            if len(raw) > grid_size:
                print("Exceeded word length. Try again.")
                continue
            w = raw.upper()
            if w in words:
                print("Duplicate word, try another")
                continue
            words.append(w)
            break
    return words

def make_empty_grid(cols: int = COLS, rows: int = ROWS, fill="."):
    grid = [[fill for _ in range(cols)] for _ in range(rows)]
    return grid 

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    
def can_place_horizontal(grid, word, r, c):
    rows, cols = len(grid), len(grid[0])
    if c + len(word) > cols:
        return False
    for i, ch in enumerate(word):
        cc = c + i
        cell = grid[r][cc]
        if cell != "." and cell != ch:
            return False
    return True

def can_place_vertical(grid, word, r, c):
    rows, cols = len(grid), len(grid[0])
    if r + len(word) > rows:
        return False
    for i, ch in enumerate(word):
        rr = r + i
        cc = c
        cell = grid[rr][cc]
        if cell != "." and cell != ch:
            return False
    return True

def place_word_horizontal(grid, word, max_tries=200):
    rows, cols = len(grid), len(grid[0])
    for _ in range(max_tries):
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - len(word))
        if can_place_horizontal(grid, word, r, c):
            for i, ch in enumerate(word):
                grid[r][c + i] = ch
            print(f"Placed H: {word} at (row={r}, col={c})")
            return True
    return False

def place_word_vertical(grid, word, max_tries=200):
    rows, cols = len(grid), len(grid[0])
    for _ in range(max_tries):
        r = random.randint(0, rows - len(word))
        c = random.randint(0, cols - 1)
        if can_place_vertical(grid, word, r, c):
            for i, ch in enumerate(word):
                grid[r + i][c] = ch
            print(f"Placed V: {word} at (row={r}, col={c})")
            return True
    return False

def fill_random_letters(grid):
    letters = string.ascii_uppercase
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ".":
                grid[r][c] = random.choice(letters)

def main():
    # 1) Get words
    words = get_words(4, grid_size=COLS)

    # Optional: place longer words first
    words.sort(key=len, reverse=True)

    # 2) Build empty grid
    grid = make_empty_grid(COLS, ROWS, fill=".")

    # 3) Place each word
    for w in words:
        direction = random.randint(0, 1)  # 0 = horizontal, 1 = vertical
        if direction == 0:
            ok = place_word_horizontal(grid, w)
            if not ok:
                ok = place_word_vertical(grid, w)
        else:
            ok = place_word_vertical(grid, w)
            if not ok:
                ok = place_word_horizontal(grid, w)

        if not ok:
            print(f"Warning: couldn't place '{w}' in {ROWS}x{COLS} grid.")

    # 4) Fill empty cells with random letters
    fill_random_letters(grid)

    # 5) Show final grid
    print("\nFinal Grid:")
    print_grid(grid)

if __name__ == "__main__":
    main()
