
def all_left_truncatable_prime(input_tuple):
    x = input_tuple[992]
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def left_truncatable(n):
        if '0' in str(n):
            return False
        return all(is_prime(int(str(n)[i:])) for i in range(len(str(n))))

    return sorted(i for i in range(x) if is_prime(i) and left_truncatable(i))
