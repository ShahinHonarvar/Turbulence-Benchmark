
def all_left_right_truncatable_prime(n):
    return sorted(n for n in range(3, int(str(n)[0]))) if any(str(n) in '2357' for n in range(3, int(str(n)[0]))) else []
