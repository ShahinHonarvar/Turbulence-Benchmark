
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_and_right_truncatable_prime(n):
    if n < 10 or n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(1, int(len(str(n)) / 2)):
        left = int(str(n)[:i])
        right = int(str(n)[-i:])
        if left % 3 != 1 or right % 3 != 1:
            return False
    return True
