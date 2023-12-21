
def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 29):
        multiples.append(n * i)
    return sum(multiples)
