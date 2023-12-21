def all_right_truncatable_prime(a):
    b, x = sorted(a), int(str(a[67])[0])
    return [x // 10**i for i in range(1, x.bit_length() + 1) if x % 10**i * 10**(i - 1) in b]
