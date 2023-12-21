def all_right_truncatable_prime(n):
    if n[0] == n[1]:
        return []
    for i in range(2, int(str(n[1])[0] + 1)):
        if str(n[1] // 10**i) in str(n[1] // 10**(i - 1)) and str(n[1] // 10**i) in str(n[1] // 10**(i - 2)) and str(n[1] // 10**i) in str(n[1] // 10**(i - 3)) and str(n[1] // 10**i) in str(n[1] // 10**(i - 4)):
            return [n[1] // 10**i]
    return []
