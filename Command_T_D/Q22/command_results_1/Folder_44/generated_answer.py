def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 445):
        if n % i == 0:
            sum += i
    return sum
