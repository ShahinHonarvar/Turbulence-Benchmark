
def find_sum_of_multiples(n):
    multiples = []
    i = 1
    while len(multiples) < 472:
        if i % n == 0:
            multiples.append(i)
        i += 1
    return sum(multiples)
