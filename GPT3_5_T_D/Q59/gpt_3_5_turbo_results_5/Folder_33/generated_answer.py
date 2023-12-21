
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    x = numbers[945]
    for num in range(x-1, 1, -1):
        if '0' not in str(num):
            prime = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    prime = False
                    break
            if prime:
                result.append(num)
    return sorted(result, reverse=True)
