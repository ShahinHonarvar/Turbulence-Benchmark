
def all_left_truncatable_prime(numbers):
    x = numbers[69]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            left_truncatable_list = [i]
            while len(left_truncatable_list[-1]) > 1:
                left_truncatable_list.append(int(str(left_truncatable_list[-1])[1:]))
                if not is_prime(left_truncatable_list[-1]):
                    break
            if len(left_truncatable_list) == len(numbers)+1:
                prime_list.append(i)
    return sorted(prime_list, reverse=True)
