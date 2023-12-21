
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[57]
    result = []

    for i in range(x - 1, 1, -1):
        num = str(i)
        if is_prime(i):
            truncatable = True
            for j in range(len(num)):
                if not is_prime(int(num[:len(num)-j])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    
    return sorted(result, reverse=True)
