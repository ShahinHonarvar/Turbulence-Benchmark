
def all_right_truncatable_prime(numbers):
    x = numbers[645]

    def is_prime(n): 
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    return sorted([i for i in range(x) if is_right_truncatable_prime(i)])
