
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        ans = True
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                ans = False
        return ans

    def is_left_right_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:len(n)-i])):
                return False
        return True

    x = numbers[758]
    result = []
    for i in range(10, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)
