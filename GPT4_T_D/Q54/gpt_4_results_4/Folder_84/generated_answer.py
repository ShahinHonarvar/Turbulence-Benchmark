
def all_right_truncatable_prime(arr):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = n // 10
            if not is_prime(n):
                return False
        return True

    x = arr[630]
    result = [i for i in range(x) if is_right_truncatable(i)]
    return sorted(result, reverse=True)
