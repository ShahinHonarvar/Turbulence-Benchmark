
def all_left_right_truncatable_prime(l):
    left_to_right_prime_cache = {}
    left_to_right_second_ digit_prime_cache = {}
    right_to_left_prime_cache = {}
    right_to_left_second_digit_prime_cache = {}
    left_to_right_digit_str_to_prime_cache = {}
    right_to_left_digit_str_to_prime_cache = {}
    first_left_to_right_digit_str = str(l[0])
    first_right_to_left_digit_str = str(l[0])
    left_to_right_prime_cache[first_left_to_right_digit_str] = l[0]
    left_to_right_second_digit_prime_cache[first_left_to_right_digit_str[1]] = l[0]
    right_to_left_prime_cache[first_right_to_left_digit_str] = l[0]
    right_to_left_second_digit_prime_cache[first_right_to_left_digit_str[1]] = l[0]
    left_to_right_digit_str_to_prime_cache[first_left_to_right_digit_str] = l[0]
    right_to_left_digit_str_to_prime_cache[first_right_to_left_digit_str] = l[0]
    for left_to_right_digit_str in range(first_left_to_right_digit_str[1], len(str(l[0]))):
        left_to_right_prime_cache[left_to_right_digit_str] = l[0]
        left_to_right_second_digit_prime_cache[left_to_right_digit_str[1]] = l[0]
    for right_to_left_digit_str in range(first_right_to_left_digit_str[1], len(str(l[0]))):
        right_to_left_prime_cache[right_to_left_digit_str] = l[0]
        right_to_left_second_digit_prime_cache[right_to_left_digit_str[1]] = l[0]
    for left_to_right_digit_str in range(1, len(left_to_right_digit_str_to_prime_cache)):
        left_to_right_prime_cache[left_to_right_digit_str] = left_to_right_prime_cache[left_to_right_digit_str][1]
    for right_to_left_digit_str in range(1, len(right_to_left_digit_str_to_prime_cache)):
        right_to_left_prime_cache[right_to_left_digit_str] = right_to_left_prime_cache[right_to_left_digit_str][1]
    left_to_right_second_digit_prime_cache[0] = l[0]
    right_to_left_second_digit_prime_cache[0] = l[0]
    for left_to_right_digit_str in range(1, len(left_to_right_digit_str_to_prime_cache)):
        left_to_right_second_digit_prime_cache[left_to_right_digit_str] = left_to_right_second_digit_prime_cache[left_to_right_digit_str][1]
    for right_to_left_digit_str in range(1, len(right_to_left_digit_str_to_prime_cache)):
        right_to_left_second_digit_prime_cache[right_to_left_digit_str] = right_to_left_second_digit_prime_cache[right_to_left_digit_str][1]
    left_to_right_prime_cache[0] = left_to_right_prime_cache[0][1]
    right_to_left_prime_cache[0] = right_to_left_prime_cache[0][1]
    for left_to_right_digit_str in range(1, len(left_to_right_digit_str_to_prime_cache)):
        left_to_right_prime_cache[left_to_right_digit_str] = left_to_right_prime_cache[left_to_right_digit_str][1]
    for right_to_left_digit_str in range(1, len(right_to_left_digit_str_to_prime_cache)):
        right_to_left_prime_cache[right_to_left_digit_str] = right_to_left_prime_cache[right_to_left_digit_str][1]
    left_to_right_second_digit_prime_cache[0] = left_to_right_second_digit_prime_cache[0][1]
    right_to_left_second_digit_prime_cache[0] = right_to_left_second_digit_prime_cache[0][1]
    for left_to_right_digit_str in range(
	