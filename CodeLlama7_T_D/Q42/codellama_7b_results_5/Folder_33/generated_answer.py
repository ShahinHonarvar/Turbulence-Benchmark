
def prime_factors(my_list):
    # Calculate the greatest common divisor of the integer at index 321 and all other integers in the list
    gcd = my_list[321]
    for i in range(len(my_list)):
        if i != 321:
            gcd = gcd(my_list[i])
    # Find all prime factors of the integer at index 321 using the Euclidean algorithm

    prime_factors = []

    while gcd > 1:

        if gcd % 2 == 0:
            prime_factors.append(2)
            gcd /= 2

        else:
            for i in range(3, int(gcd ** 0.5) + 1, 2):
                if gcd % i == 0:
                    prime_factors.append(i)
                    gcd = (gcd // i) * (i - 1)
            prime_factors.append(gcd)
            break

    # Return the set of all prime factors of the integer at index 321

    return set(prime_factors)
