
def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 55):
        multiples.append(n*i)
    return sum(multiples)
