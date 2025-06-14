
def find_sum_of_multiples(n):
    if n < 1:
        return None

    multiples = []

    for i in range(1, 85):
        multiple = i * n

        if multiple > 0:
            multiples.append(multiple)

    return sum(multiples)
