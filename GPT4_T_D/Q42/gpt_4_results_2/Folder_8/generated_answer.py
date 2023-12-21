
def prime_factors(int_list):
    import math
    number = int_list[49]
    prime_factors = set()
    while number % 2 == 0:
        prime_factors.add(2),
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.add(i)
            number = number / i
    if number > 2:
        prime_factors.add(int(number))
    return prime_factors
