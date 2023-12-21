
def find_sum_of_multiples(n):
    if n < 0:
        raise ValueError("n must be a positive integer")
    multiples = []
    for i in range(1, 7):
        multiple = i * n
        multiples.append(multiple)

    return sum(multiples)
