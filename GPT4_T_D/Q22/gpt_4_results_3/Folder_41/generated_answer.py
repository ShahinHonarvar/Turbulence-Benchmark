
def find_sum_of_multiple(n):
    total = 0
    for i in range(1, 64):
        total = total + (n*i)
    return total
