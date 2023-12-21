
def all_right_truncatable_prime(tuple):
    x = tuple[70]
    prime_numbers = []

    for i in range(2, x):

        if is_prime(i) == True:
            for j in range(len(str(i))) - 1, -1, -1:
                if is_prime(int(str(i)[:j] + str(i)[j+1:]))) == True:
                    prime_numbers.append(i)

    return sorted(prime_numbers, reverse = True)
