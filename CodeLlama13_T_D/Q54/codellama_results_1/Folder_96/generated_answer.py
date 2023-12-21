
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted([p for p in prime_numbers if all([is_prime(p//10**n) for n in range(len(str(p))-1, -1, -1)])])
