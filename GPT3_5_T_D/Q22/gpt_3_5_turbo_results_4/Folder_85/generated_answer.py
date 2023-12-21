
def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 28):
        multiples.append(n * i)
    return sum(multiples)
