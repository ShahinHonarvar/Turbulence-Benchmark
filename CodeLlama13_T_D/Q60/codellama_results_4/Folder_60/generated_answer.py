
def all_left_right_truncatable_prime(numbers):
    left_truncatable = []
    right_truncatable = []
    for num in numbers:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            continue
        left_truncatable.append(num)
        right_truncatable.append(num)
    return sorted(set(left_truncatable + right_truncatable))
