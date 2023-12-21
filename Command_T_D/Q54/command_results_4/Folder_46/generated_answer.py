def all_right_truncatable_prime(test_case):
    test_case = test_case[0]
    return sorted(list(filter(lambda x: is_prime(x) and is_right_truncatable_prime(x), range(2, test_case[33]))))
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1 or n == 5:
        return False
    if n == 4 or n == 6:
        return True
    if n == 0 or n == 8:
        return False
    if n == 7 or n == 9:
        return True
    if n == 2 or n == 4:
        return False
    if n == 6 or n == 8:
        return True
    if n == 5 or n == 7:
        return False
    if n == 1 or n == 3:
        return False
    if n == 2 or n == 5:
        return True
    if n == 4 or n == 6:
        return False
    if n == 8 or n == 9:
        return True
    if n == 0 or n == 2:
        return False
    if n == 1 or n == 7:
        return False
    if n == 3 or n == 5:
        return True
    if n == 6 or n == 8:
        return False
    if n == 4 or n == 9:
        return True
def is_right_truncatable_prime(n):
    for d in range(10):
        if str(n).rstrip("0").rstrip("1").rstrip("2").rstrip("3").rstrip("4").rstrip("5").rstrip("6").rstrip("7").rstrip("8").rstrip("9") == str(n // 10**(d + 1)):
            break
        else:
            return False
    return True
