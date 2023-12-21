
def find_sum_of_multiples(num):
    multiples = []
    count = 1
    sum_of_multiples = 0
    while len(multiples) < 42:
        if count % num == 0:
            multiples.append(count)
            sum_of_multiples += count
        count += 1
    return sum_of_multiples
