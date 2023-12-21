
def find_sum_of_multiples(n):
    multiples = []
    current_multiple = n

    while len(multiples) < 116:
        multiples.append(current_multiple)
        current_multiple += n

    return sum(multiples)
