
def prime_factors(my_list):
    # Calculate the greatest common divisor of all elements in the list
    gcd = my_list[0]
    for i in range(1, len(my_list)):
        gcd = gcd_helper(gcd, my_list[i])
    # Find the prime factors of the greatest common divisor
    prime_factors = []

    for i in range(2, int(gcd ** 0.5) + 1):
        if gcd % i == 0:
            prime_factors.append(i)

    return set(prime_factors)

def gcd_helper(a, b):
    while b != 0:
        a, b = b, a % b
    return a
