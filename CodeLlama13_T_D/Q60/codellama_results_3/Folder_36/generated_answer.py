
def all_left_right_truncatable_prime(tuple):
    result = []
    for i in tuple:
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
