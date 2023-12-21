
def find_sum_of_multiples(n):
    if n < 1:
        return 0

    multiples = []

    for i in range(1, 17):
        multiples.append(i * n)

    return sum(multiples)
