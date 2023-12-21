
def all_left_right_truncatable_prime(numbers):
    x = numbers[43]

    def is_prime(n):
        if n <= 1: return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0: return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        return all(is_prime(int(n_str[i:])) and is_prime(int(n_str[:-i-1])) for i in range(len(n_str)))

    def has_zero(n):
        return '0' in str(n)

    return sorted(num for num in range(x+1) if is_prime(num) and not has_zero(num) and is_truncatable(num))
