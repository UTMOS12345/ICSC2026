import sys
from collections import defaultdict


def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    # Creates and dict with default values as list []
    frame_map = defaultdict(list)

    # Goes throug each event
    for player, frame, damage in events:
        frame_map[frame].append(
            (player, damage)
        )  # Appends information to the specific frame

    chrono_sorted_frames = sorted(frame_map.keys())  # Sorts the frames chronologically
    # Sorting frames chronologically ensures that events happen in chronological order

    # Sets up initial healt of players
    hp1, hp2 = H, H

    # Goes through each frame
    for frame in chrono_sorted_frames:
        # Firs applies the events happened in that frame
        for player, damage in frame_map[frame]:
            if player == 1:
                hp2 -= damage
            elif player == 2:
                hp1 -= damage
        # Then checks for KO
        if hp1 <= 0 or hp2 <= 0:
            break

    # Returns the values and clamps minimum to 0
    return [max(0, hp1), max(0, hp2)]


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
