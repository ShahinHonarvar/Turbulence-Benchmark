
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    count = 0
    for i in range(1, 1000):
        if i % n == 0:
            sum_of_multiples += i
            count += 1
            if count == 40:
                break
    return sum_of_multiples
