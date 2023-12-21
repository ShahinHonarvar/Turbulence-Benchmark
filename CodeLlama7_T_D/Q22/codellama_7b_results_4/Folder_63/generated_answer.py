
def find_sum_of_multiples(n):
    if n < 1:
        return 0

    multiples = []

    for i in range(1, 19):
        multiple = n * i
        multiples.append(multiple)

    return sum(multiples)
