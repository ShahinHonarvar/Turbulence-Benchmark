
def all_left_right_truncatable_prime(n):
    def f(x):
        if x == '':
            return False
        if x[0] == '0' or x[0] == '1':
            return False
        return f(x[1:]) and f(x[1:-1])
    s = str(n[78])
    for i in range(3, int(s[::-1]) + 1):
        if f(str(i)):
            yield i
    return []
