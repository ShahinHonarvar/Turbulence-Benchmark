
def find_sum_of_multiple(n):
    if n < 1:
        return "The provided number must be a positive integer"
    return sum([i*n for i in range(1, 277)])
