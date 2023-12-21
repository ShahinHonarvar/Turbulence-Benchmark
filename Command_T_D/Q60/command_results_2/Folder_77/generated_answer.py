
def all_left_right_truncatable_prime(x):
    def check(n):
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                return False
            if n % i == 1 and n / i == i:
                return False
        return True
    d = str(x)
    for i in range(len(d) - 1, -1, -1):
        if d[i] == '0':
            continue
        n = int(d[0:i] + d[i+1:])
        if check(n):
            yield n
            break
    return
