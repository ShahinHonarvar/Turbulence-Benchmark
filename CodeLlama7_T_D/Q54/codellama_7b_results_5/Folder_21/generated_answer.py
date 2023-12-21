 def all_right_truncatable_prime(tuple):
    x = tuple[175]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) == True:
            right_truncatable = True
            for j in range(1, len(str(i)))):
                if is_prime(int(str(i)[0:-j])) == False:
                    right_truncatable = False
                    break

            if right_truncatable == True:
                prime_numbers.append(i)

    return sorted(prime_numbers)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
