
def all_left_right_truncatable_prime(tuple_of_numbers):
    x = tuple_of_numbers[24]
    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def left_right_prime(n):
        if '0' in str(n):
            return False
        return all(is_prime(int(str(n)[:i])) and is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))

    return sorted(filter(left_right_prime, filter(is_prime, range(10, x+1))))
