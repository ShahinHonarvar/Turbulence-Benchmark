
def find_sum_of_multiple(n):
    if n <= 0:
        return "Argument must be a positive integer"
    else:
        return sum([i*n for i in range(1, 476)])
