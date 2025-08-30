import random, string

# customization
words = []
length = 8
width = 8
words = []

# words reject if 
# is not alpha (numbers) /
# more than n and k /
# empty input /
# duplicate words /

def get_words(count : int, grid_size : int = length):
    for i in range(count):
        while True:
            raw = input(f"Word {i+1}/{count}. (Letters only, 1–{grid_size} chars): ").strip()
            if not raw.isalpha():
                print("Only letters. Try again")
                continue
            if not raw:
                print("Empty input, try again")
                continue
            if len(raw) > grid_size:
                print("Exceeded Word Length. Try again.")
                continue
                
            w = raw.upper()
            if w in words:
                print("Duplicate words, try another")
                continue
            words.append(w)
            break
    return words

get_words(4)
        

def grids(n,k):
    grid = [[random.choice(string.ascii_lowercase) for _ in range(n)] for _ in range(k)]
    for row in grid:
        print(' '.join(row))

# grids(length, width)