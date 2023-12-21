
def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[93]
    list_of_left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list_of_left_truncatable_primes.append(i)
    return sorted(list_of_left_truncatable_primes)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    string_of_n = str(n)
    for i in range(len(string_of_n)):
        if string_of_n[i] == "0":
            return False

        if not is_prime(int(string_of_n[:i] + string_of_n[i+1:])):
            return False

    return True
