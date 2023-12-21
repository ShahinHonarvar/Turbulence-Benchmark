
def all_left_right_truncatable_prime(x):
    return sorted(list(filter(left_right_truncatable_prime, range(2, x + 1))), reverse=True)

def left_right_truncatable_prime(n):
    for d in range(3, int(str(n ** .5) + .5) + 1):
        if n % d == 0:
            break
    if n == 1:
        return True
    if n == 2:
        return True
    if str(n) == '2' + '0' * (len(str(n)) - 1):
        return True
    if str(n) == '2' + '0' * (len(str(n)) - 2):
        return True
    if str(n) == '2' + '0' + '2' + '0' * (len(str(n)) - 3):
        return True
    return all(int(i) for i in str(n))
