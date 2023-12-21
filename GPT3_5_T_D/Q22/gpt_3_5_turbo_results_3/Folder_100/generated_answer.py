
def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 92):
        multiples.append(n * i)
    return sum(multiples)
