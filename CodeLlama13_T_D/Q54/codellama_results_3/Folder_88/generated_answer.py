
def all_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        prime_list = []
        for i in range(2, x+1):
            if is_prime(i) and is_right_truncatable_prime(i):
                prime_list.append(i)
        result.extend(sorted(prime_list))
    return result
