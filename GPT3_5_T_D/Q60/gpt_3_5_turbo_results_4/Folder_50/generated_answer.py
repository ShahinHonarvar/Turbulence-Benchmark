
def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        digits = str(n)
        for i in range(len(digits)):
            truncated_number = int(digits[i:])
            if not is_prime(truncated_number):
                return False
        return True

    def is_right_truncatable_prime(n):
        digits = str(n)
        for i in range(len(digits)):
            truncated_number = int(digits[:len(digits)-i])
            if not is_prime(truncated_number):
                return False
        return True

    x = numbers[57] # Get the integer at index 57
    result = []

    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)

    return sorted(result, reverse=True)
