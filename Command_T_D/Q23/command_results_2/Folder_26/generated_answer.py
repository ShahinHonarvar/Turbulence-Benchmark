def find_divisors_in_range(n):
    if n < 83 or n > 95:
        return []
    if n < 89:
        return [i for i in range(83, n + 1) if n % i == 0]
    if n == 89:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0]
    if n == 90:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0 or n % (i + 2) == 0]
    if n == 91:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0 or n % (i + 2) == 0 or n % (i + 3) == 0]
    if n == 92:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0 or n % (i + 2) == 0 or n % (i + 3) == 0 or n % (i + 4) == 0]
    if n == 93:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0 or n % (i + 2) == 0 or n % (i + 3) == 0 or n % (i + 4) == 0 or n % (i + 5) == 0]
    if n == 94:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0 or n % (i + 2) == 0 or n % (i + 3) == 0 or n % (i + 4) == 0 or n % (i + 5) == 0 or n % (i + 6) == 0]
    if n == 95:
        return [i for i in range(83, n + 1) if n % i == 0 or n % (i + 1) == 0 or n % (i + 2) == 0 or n % (i + 3) == 0 or n % (i + 4) == 0 or n % (i + 5) == 0 or n % (i + 6) == 0 or n % (i + 7) == 0]
