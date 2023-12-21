
def all_left_right_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(number):
    if number < 2 or (number % 2 == 0 and number != 2):
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
