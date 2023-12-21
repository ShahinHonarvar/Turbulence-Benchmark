
def all_left_right_truncatable_prime(tuple_of_integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i-1])):
                return False
        return True

    x = tuple_of_integers[55]
    return sorted([n for n in range(x+1) if is_left_right_truncatable_prime(n)])
