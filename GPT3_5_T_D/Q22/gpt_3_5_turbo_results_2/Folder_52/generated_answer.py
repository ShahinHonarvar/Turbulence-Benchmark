
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    count = 0
    num = 0
    while count < 423:
        if num % n == 0:
            sum_of_multiples += num
            count += 1
        num += 1
    return sum_of_multiples
