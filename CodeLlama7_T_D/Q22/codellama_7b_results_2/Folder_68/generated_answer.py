
def find_sum_of_multiples(n):
    if n <= 0:
        return None

    multiples = []

    for i in range(1, 5):
        multiple = n * i
        multiples.append(multiple)

    sum_of_multiples = sum(multiples)

    return sum_of_multiples
