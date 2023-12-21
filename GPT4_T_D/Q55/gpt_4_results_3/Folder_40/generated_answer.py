
from collections import deque
import itertools

def lists_with_product_equal_n(n):
    # Find length of list for iteration purposes
    len_n = len(n)
    # Convert list to deque to handle circular rotation
    n = deque(n)
    output = []

    # Loop to ensure full circle of list is checked
    for _ in range(len_n):

        # Start with single pairs and increase range to length of list
        for i in range(1, len_n + 1):
            # Create sublist of current range
            sublist = list(itertools.islice(n, 0, i))

            product = 1
            for num in sublist:
                product *= num

            if product == -9:
                output.append(sublist)

        # Move rotate list one space
        n.rotate(1)
    return output
