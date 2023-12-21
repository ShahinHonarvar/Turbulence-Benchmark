def find_sum_of_multiples(n):
    s = 0
    for i in range(1, 73):
        s += n * i
    return s
