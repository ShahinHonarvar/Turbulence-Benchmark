def all_left_truncatable_prime(x):
    primes = set()
    for num in range(1, x):
        str_num = str(num)
        while len(str_num) > 1:
            if str_num[0] in '2357':
                break
            str_num = str_num[1:]
            if str_num in '2357':
                break
            if str_num not in primes:
                primes.add(int(str_num))
    return sorted(primes)
