def find_sum_of_multiples(n):
    result = 0
    for i in range(1,85):
        result += n*(i-1)
    return result
