
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    total = 1
    for i in my_list:
        total *= i

    # Find the prime factors of the total product

    prime_factors = set()

    while total != 1:

        if total % 2 == 0:

            prime_factors.add(2)

            total //= 2


        else:


            for i in range(3, int(total ** 0.5) + 1, 2):

                if total % i == 0:

                    prime_factors.add(i)

                    total //= i


                    break


    return prime_factors
