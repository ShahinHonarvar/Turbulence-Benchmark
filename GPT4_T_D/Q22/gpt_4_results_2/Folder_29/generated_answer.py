
def find_sum_of_multiples(n):
    if n <= 0:
        return 0
    sum_of_nums = sum(i*n for i in range(1, 95))
    return sum_of_nums
