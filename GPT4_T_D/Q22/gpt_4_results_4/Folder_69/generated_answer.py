
def find_sum_of_multiples(n):
    multiple_list = [i*n for i in range(1, 473)]
    return sum(multiple_list)
