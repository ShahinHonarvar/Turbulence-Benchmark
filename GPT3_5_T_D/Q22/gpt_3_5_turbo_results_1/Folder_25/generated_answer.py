
def find_sum_of_multiples(number):
    multiples = []
    count = 0
    i = 1
    while count < 34:
        if i % number == 0:
            multiples.append(i)
            count += 1
        i += 1
    return sum(multiples)
