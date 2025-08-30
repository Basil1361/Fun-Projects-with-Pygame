def grids(n,k):
    grid = [['.' for _ in range(n)] for _ in range(k)]
    for row in grid:
        print(' '.join(row))
    
grids(8,7)

# for row in grid:
#     # printing row gives us (8x8) but it's not joined
#     print(' '.join(row)) joins together
