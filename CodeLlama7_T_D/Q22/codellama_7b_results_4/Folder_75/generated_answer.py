
def find_sum_of_multiples(n):
    if n < 0:
        return "Error: Argument must be a positive integer."
    multiples = []
    for i in range(1, 16):
        multiples.append(i * n)
    return sum(multiples)
