
import itertools

def all_left_right_truncatable_prime(n):
    left_digits = {str(x) for x in range(2, n) if x > 1}
    right_digits = {str(x) for x in range(2, n) if x not in left_digits}
    all_left_right_truncatable_prime = []
    for prime in itertools.permutations(left_digits & right_digits):
        if prime[0] == '2':
            continue
        if prime[0] == '3':
            continue
        if prime[-1] == '2':
            continue
        if prime[-1] == '3':
            continue
        for j in range(1, len(prime)):
            if prime[j] == '0':
                break
            elif prime[j] == '5':
                continue
            elif prime[j] == '7':
                continue
            elif prime[j] == '9':
                continue
            elif prime[j] == '4':
                continue
            elif prime[j] == '6':
                continue
            elif prime[j] == '8':
                continue
            elif prime[j] == '2':
                continue
            elif prime[j] == '3':
                continue
            elif prime[j] == '5':
                continue
            elif prime[j] == '7':
                continue
            elif prime[j] == '9':
                continue
            elif prime[j] == '4':
                continue
            elif prime[j] == '6':
                continue
            elif prime[j] == '8':
                continue
        all_left_right_truncatable_prime.append(int(prime))
    return sorted(set(all_left_right_truncatable_prime))
