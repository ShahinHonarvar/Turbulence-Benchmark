
def all_left_right_truncatable_prime(numbers):
    x = numbers[61]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if "0" in str_n[i:] or not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    result = [num for num in range(10, x + 1) if is_truncatable(num)]
    return sorted(result)
