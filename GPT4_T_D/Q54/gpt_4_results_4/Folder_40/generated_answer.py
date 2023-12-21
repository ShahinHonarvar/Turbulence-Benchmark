
def all_right_truncatable_prime(arr):
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

    def is_right_truncatable_prime(n):
        num = str(n)
        for i in range(len(num)):
            if not is_prime(int(num[i:])):
                return False
        return True

    x = arr[10]
    prime_numbers = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
