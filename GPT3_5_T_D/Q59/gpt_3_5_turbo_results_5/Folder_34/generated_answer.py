
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[18]
    result = []
    for i in range(x - 1, 1, -1):
        num_str = str(i)
        if '0' in num_str:
            continue
        truncatable = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[j:])):
                truncatable = False
                break
        if truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result
