def all_left_truncatable_prime(n):
    primes = []
    x = n[25]
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return primes
def is_left_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if str(n)[i] == '0':
            return False
        elif str(n)[i] == '1':
            break
        elif str(n)[i] == '2':
            for j in range(2, 10):
                if str(n)[i+j] == '0':
                    return False
        elif str(n)[i] == '3':
            for j in range(2, 10):
                if str(n)[i+j] == '0':
                    return False
        elif str(n)[i] == '5':
            for j in range(2, 10):
                if str(n)[i+j] == '0':
                    return False
        elif str(n)[i] == '7':
            for j in range(2, 10):
                if str(n)[i+j] == '0':
                    return False
        elif str(n)[i] == '9':
            for j in range(2, 10):
                if str(n)[i+j] == '0':
                    return False
    return True
