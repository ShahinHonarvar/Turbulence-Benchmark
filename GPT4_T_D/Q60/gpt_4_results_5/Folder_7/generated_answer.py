
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        
        while i * i <= n:
            if n % i == 0:
                return False

            i += w
            w = 6 - w

        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = numbers[803]
    return sorted([i for i in range(x+1) if is_prime(i) and is_left_right_truncatable(i)])
