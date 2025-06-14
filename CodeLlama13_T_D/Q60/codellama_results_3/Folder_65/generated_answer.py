
def all_left_right_truncatable_prime(x):
    x = list(set(x))
    primes = []
    for i in range(len(x)):
        if is_prime(x[i]) and not any([str(x[i]).count('0') > 0, ''.join(str(x[i]).split()[:-1]).isdigit(), str(x[i]).split()[-2:].isdigit()]):
            primes.append(x[i])
    return sorted(primes)
