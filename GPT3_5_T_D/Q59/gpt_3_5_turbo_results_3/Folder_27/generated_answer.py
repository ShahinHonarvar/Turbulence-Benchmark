
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[79]
    result = []
    for num in range(x-1, 0, -1):
        if '0' not in str(num):
            num_str = str(num)
            is_left_truncatable = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(num)
    return sorted(result, reverse=True)
