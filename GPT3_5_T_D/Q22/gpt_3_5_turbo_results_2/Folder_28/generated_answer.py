
def find_sum_of_multiples(integer):
    multiples = []
    count = 1
    while len(multiples) < 43:
        multiples.append(integer * count)
        count += 1
    return sum(multiples)
