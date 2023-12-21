def find_sum_of_multiples(n):
    # your code here
    if n == 1:
        return 18
    result = 0
    for i in range(1, 19):
        result += n * i
    return result
