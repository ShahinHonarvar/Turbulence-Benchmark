
def find_sum_of_multiple(n):
    if n > 0:
        return sum(n*i for i in range(1, 174))
