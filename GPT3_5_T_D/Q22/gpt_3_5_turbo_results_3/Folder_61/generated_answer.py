
def find_sum_of_multiples(n):
    multiples = []
    i = 1
    while len(multiples) < 5:
        multiple = n * i
        multiples.append(multiple)
        i += 1
    return sum(multiples)
