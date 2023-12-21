
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    count = 0

    for i in range(1, 367):
        if count == 366:
            break
        if i % n == 0:
            sum_of_multiples += i
            count += 1

    return sum_of_multiples
