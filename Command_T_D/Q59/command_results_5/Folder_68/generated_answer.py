def all_left_truncatable_prime(test_case):
    primes = []
    for prime in range(test_case[0], test_case[1], -1):
        if prime in primes:
            continue
        if prime < 10:
            primes.append(prime)
            continue
        if is_prime(str(prime)):
            primes.append(prime)
            continue
        else:
            break
    return primes
def is_prime(str_num):
    if len(str_num) == 1:
        return True
    if str_num[0] == '0':
        return False
    if str_num[0] == '1':
        return True
    if str_num[0] == '2':
        return True
    if str_num[0] == '3':
        return True
    if str_num[0] == '5':
        return True
    if str_num[0] == '6':
        return True
    if str_num[0] == '7':
        return True
    if str_num[0] == '8':
        return False
    if str_num[0] == '9':
        return False
    return all(is_prime(str_num[1:]))
