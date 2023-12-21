
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 148):
        if n * i > n:
            break

        sum += n * i

    return sum
