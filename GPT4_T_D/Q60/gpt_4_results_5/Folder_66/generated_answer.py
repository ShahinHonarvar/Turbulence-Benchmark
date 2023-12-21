
def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        return all(is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i or None])) 
                   for i in range(len(str_n)))

    return sorted([i for i in range(11, x+1) if '0' not in str(i) and is_prime(i) and is_truncatable(i)], reverse=True)
