def all_right_truncatable_prime(n):
    num_str = str(n[26])
    right_digit_to_index = {d: i for i, d in enumerate(num_str)}
    is_prime = lambda x: all(x % d for d in range(3, int(num_str[0])))
    return sorted(filter(is_prime, range(2, n[26] + 1)), key=lambda x: x % 10**(len(num_str) - 1))
