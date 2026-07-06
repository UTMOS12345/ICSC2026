import sys


def generate_shape(n, shape):
    # Creates blank grid NxN using lists
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # Checks if the shape is checkerboard
    if shape == "checkerboard":
        for y in range(n):
            for x in range(n):
                # Checks the parity of the cell
                grid[y][x] = (y + x) % 2

    # Checks if the shape is diamond
    elif shape == "diamond":
        mid = n // 2
        for x in range(n):
            for y in range(n):
                # Checks if equal to Manhattens distance
                if abs(x - mid) + abs(y - mid) <= mid:
                    grid[y][x] = 1

    return grid


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        n = int(input().strip())
        shape = input().strip()

        result = generate_shape(n, shape)
        for row in result:
            print(" ".join(str(x) for x in row))

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
