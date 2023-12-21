
def all_right_truncatable_prime(numbers):
    x = numbers[19]
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_right_truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    result = []
    for num in range(2, x):
        if is_right_truncatable(num):
            result.append(num)
    
    return sorted(result)
