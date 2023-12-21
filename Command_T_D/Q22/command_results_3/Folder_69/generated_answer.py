import math
def find_sum_of_multiples(n):
    return (sum(list(range(n, 472, n)) + list(range(n, 0, -1))))) / n
