def find_sum_of_multiples(n):
    # write your code here
    s = 0
    for i in range(1, 475):
        s += n*i
    return s
