
def all_left_truncatable_prime(tuple):
    x = tuple[55]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and not contains_zero(str(i)):
            left_truncatable_prime = True
            for j in range(1, len(str(i)) - 1):
                if not is_prime(int(str(i)[j:] + str(i)[:j])):
                    left_truncatable_prime = False
                    break
            if left_truncatable_prime:
                prime_list.append(i)
    return sorted(prime_list)
