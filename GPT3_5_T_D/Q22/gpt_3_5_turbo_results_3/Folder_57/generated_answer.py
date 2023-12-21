
def find_sum_of_multiples(n):
    total = 0
    count = 0
    for i in range(1, 1000000):
        if i % n == 0:
            total += i
            count += 1
            if count == 59:
                return total
