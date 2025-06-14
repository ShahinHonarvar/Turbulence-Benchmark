
def find_sum_of_multiples(n):
    if n < 1:
        return None

    multiples = []

    for i in range(1, n + 1):
        if i % n == 0:
            multiples.append(i)

    return sum(multiples[:2])
