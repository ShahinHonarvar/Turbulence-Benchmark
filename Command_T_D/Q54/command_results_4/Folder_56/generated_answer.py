def all_right_truncatable_prime(test_list):
    res = []
    for i in test_list:
        x = i**2
        while x <= test_list[30]:
            if is_prime(x):
                break
            x = x // 10
        else:
            continue
        for _ in range(10):
            y = x // 10
            if y == 0:
                break
            if is_prime(y):
                break
            else:
                x = y
    return res
def is_prime(x):
    return all(x % d != 0 for d in range(2, x//2 + 1))
