
def find_sum_of_multiples(n):
    if n < 1:
        return 0

    multiples = []

    for i in range(1, 17):
        multiple = n * i
        multiples.append(multiple)

    sum_of_multiples = sum(multiples)
    return sum_of_multiples
