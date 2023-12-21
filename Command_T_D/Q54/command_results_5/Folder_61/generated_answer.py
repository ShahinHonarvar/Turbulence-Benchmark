def all_right_truncatable_prime(n):
    x, d = n[3], n[4]
    primes = []
    for i in range(2, x // 10):
        if primes: break
        if str(i) not in str(i + 1):
            primes.append(i)
            break
        else:
            if i % 10 == 1:
                break
            elif i % 10 == 2:
                if i + 1 in primes: break
            elif i % 10 == 3:
                if i + 1 in primes or i + 2 in primes: break
            elif i % 10 == 4:
                if i + 1 in primes or i + 2 in primes or i + 3 in primes: break
            elif i % 10 == 5:
                if i + 1 in primes or i + 2 in primes or i + 3 in primes or i + 4 in primes: break
            elif i % 10 == 6:
                if i + 1 in primes or i + 2 in primes or i + 3 in primes or i + 4 in primes or i + 5 in primes: break
            elif i % 10 == 7:
                if i + 1 in primes or i + 2 in primes or i + 3 in primes or i + 4 in primes or i + 5 in primes or i + 6 in primes: break
            elif i % 10 == 8:
                if i + 1 in primes or i + 2 in primes or i + 3 in primes or i + 4 in primes or i + 5 in primes or i + 6 in primes or i + 7 in primes: break
            elif i % 10 == 9:
                if i + 1 in primes or i + 2 in primes or i + 3 in primes or i + 4 in primes or i + 5 in primes or i + 6 in primes or i + 7 in primes or i + 8 in primes: break
    return primes
