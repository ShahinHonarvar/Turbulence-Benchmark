def find_sum_of_multiples(n):
    result = 0
    for i in range(1, 17):
        result += n * i
    return result
