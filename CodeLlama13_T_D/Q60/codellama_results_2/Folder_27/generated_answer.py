
def all_left_right_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)
