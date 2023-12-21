
def prime_factors(my_list):
    # Find the integer at index 453 in the list
    num = my_list[453]
    # Initialize an empty set to store the prime factors

    prime_factors = set()

    # Check if the number is prime itself

    if num > 1:

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:

                prime_factors.add(i)

                while num % i == 0:

                    num //= i

        if num > 1:

            prime_factors.add(num)

    return prime_factors
