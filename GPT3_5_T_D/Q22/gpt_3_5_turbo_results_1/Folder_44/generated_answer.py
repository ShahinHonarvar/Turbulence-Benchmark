
def find_sum_of_multiples(num):
    multiples = []
    i = 1
    while len(multiples) < 445:
        multiple = num * i
        multiples.append(multiple)
        i += 1
    return sum(multiples)
