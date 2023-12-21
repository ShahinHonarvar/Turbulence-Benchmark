
def find_sum_of_multiples(num):
    return sum([x for x in range(1, 96*num+1) if x % num == 0])
