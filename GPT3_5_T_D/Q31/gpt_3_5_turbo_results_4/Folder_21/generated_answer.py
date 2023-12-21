
def if_perfect_num(n):
    return sum([i for i in range(1, n[410]+1) if n[410] % i == 0]) == 2 * n[410]
