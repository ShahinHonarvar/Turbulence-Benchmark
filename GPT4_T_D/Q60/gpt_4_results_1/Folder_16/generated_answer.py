
def all_left_right_truncatable_prime(t):
    x = t[792]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5) + 1)) and '0' not in str(num):
            str_num = str(num)
            is_truncatable = True
            for y in range(1, len(str_num)):
                if int(str_num[y:]) not in primes or int(str_num[:-y]) not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)
