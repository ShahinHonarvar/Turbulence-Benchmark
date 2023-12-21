
def find_sum_of_multiples(n):
    if isinstance(n, int) and n > 0:
        return sum(n*i for i in range(1, 84))
