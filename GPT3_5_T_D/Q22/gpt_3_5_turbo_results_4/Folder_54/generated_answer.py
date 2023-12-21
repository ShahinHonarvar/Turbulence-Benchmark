
def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 30):
        multiples.append(num * i)
    return sum(multiples)
