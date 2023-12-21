def all_right_truncatable_prime(x_tuple):
    x, tuples = x_tuple[0], x_tuple[1:]
    primes = []
    for t in tuples:
        p = str(t)
        if p[0] != '2' and p[1] != '5':
            for i in range(2, len(p)):
                if p[i] == '9':
                    break
                elif p[i] == '0' or p[i] == '1':
                    p = p[:i] + p[i+1:]
                elif p[i] != '2' and p[i] != '5':
                    p = p[:i] + p[i+1:]
                    break
            if all(int(p) for p in str(t)):
                primes.append(t)
    return sorted(primes, reverse=True)
