
def all_left_right_truncatable_prime(numbers):
    def find_truncatable_prime(num):
        if num < 10:
            if num in [2, 3, 5, 7]:
                return True
            else:
                return False
        if num % 10 in [2, 3, 5, 7] and (num // 10) % 10 in [2, 3, 5, 7]:
            truncatable = True
            for i in range(len(str(num))-1):
                if not is_prime(int(str(num)[i:])):
                    truncatable = False
                    break
            return truncatable

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[175]
    results = []
    for i in range(2, x + 1):
        if find_truncatable_prime(i):
            results.append(i)
    return results
