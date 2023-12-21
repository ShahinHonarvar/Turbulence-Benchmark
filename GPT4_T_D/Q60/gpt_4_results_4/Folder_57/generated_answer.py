
def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    primes = []

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        str_i = str(i)
        for j in range(len(str_i)):
            if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:len(str_i)-j])):
                break
        else:
            primes.append(i)

    primes.sort(reverse=True)
    return primes
