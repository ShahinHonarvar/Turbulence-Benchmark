
def all_left_truncatable_prime(numbers):
    x = numbers[37]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            left_truncated = [int(j) for j in str(i)]
            while len(left_truncated) > 0:
                if not is_prime(int("".join(map(str, left_truncated)))):
                    break
                prime_list.append(int("".join(map(str, left_truncated))))
                left_truncated = left_truncated[:-1]
    return sorted(prime_list, reverse=True)
