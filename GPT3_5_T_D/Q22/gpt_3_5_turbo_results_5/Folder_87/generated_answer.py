
def find_sum_of_multiples(n):
    if n <= 0:
        return 0
    else:
        count = 0
        sum_of_multiples = 0
        i = 1
        while count < 57:
            if i % n == 0:
                sum_of_multiples += i
                count += 1
            i += 1
        return sum_of_multiples
