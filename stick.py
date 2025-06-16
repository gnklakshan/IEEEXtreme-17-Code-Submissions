from sortedcontainers import SortedList


def union_area(n: int, k: int, l: int) -> int:
    """
    Calculate the union area of n squares with side length 2l, centered at points (i*k, i*k) for i from 1 to n.

    Args:
        n: Number of squares
        k: Distance between square centers
        l: Half side length of each square

    Returns:
        Total area of the union of all squares
    """
    # Create events for sweep line algorithm
    events = []
    for i in range(1, n + 1):
        x1, y1 = i * k - l, i * k - l  # Bottom-left corner
        x2, y2 = i * k + l, i * k + l  # Top-right corner

        # Add vertical edges as events
        # Type 1 for entering edge, -1 for exiting edge
        events.append((x1, y1, y2, 1))  # Left edge
        events.append((x2, y1, y2, -1))  # Right edge

    # Sort events by x-coordinate
    events.sort()

    # Use sorted list to maintain active y-intervals
    active_intervals = SortedList()
    area = 0
    prev_x = events[0][0]

    # Process events from left to right
    for x, y1, y2, typ in events:
        # Calculate area up to current x
        width = x - prev_x
        if active_intervals:
            height = 0
            prev_y = active_intervals[0]

            # Calculate total height of active intervals
            for i in range(1, len(active_intervals)):
                cur_y = active_intervals[i]
                if cur_y > prev_y:
                    height += cur_y - prev_y
                prev_y = cur_y

            area += width * height

        # Update active intervals
        if typ == 1:  # Entering edge
            active_intervals.add(y1)
            active_intervals.add(y2)
        else:  # Exiting edge
            active_intervals.remove(y1)
            active_intervals.remove(y2)

        prev_x = x

    return area


def main():
    """Main function to handle input and output."""
    # Get input values
    N = int(input("Enter the value of N: "))
    K = int(input("Enter the value of K: "))
    L = int(input("Enter the value of L: "))

    # Calculate and print result
    result = union_area(N, K, L)
    print(result)


if __name__ == "__main__":
    main()