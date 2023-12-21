
def find_sum_of_multiples(num):
    multiples = []
    i = 1
    while len(multiples) < 18:
        if i % num == 0:
            multiples.append(i)
        i += 1
    return sum(multiples)
