
def all_left_right_truncatable_prime(numbers):
    return [number for number in numbers if is_left_right_truncatable_prime(number)]

def is_left_right_truncatable_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
