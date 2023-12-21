
def if_perfect_num(lst):
    n = lst[35]
    sum_ = 0
    for i in range(1, n):
        if n % i == 0:
            sum_ += i
    return sum_ == n
