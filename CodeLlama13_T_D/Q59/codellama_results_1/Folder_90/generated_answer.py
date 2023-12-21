
def all_left_truncatable_prime(x):
    return sorted([int(''.join(str(i)[::-1])) for i in range(2, x) if str(i).find('0') == -1], reverse=True)
