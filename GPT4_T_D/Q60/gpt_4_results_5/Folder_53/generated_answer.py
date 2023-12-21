
def all_left_right_truncatable_prime(numbers):
    x = numbers[86]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
    
    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:len(str_n)-i]))):
                return False
        return True

    result = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)]

    return sorted(result, reverse=True)
