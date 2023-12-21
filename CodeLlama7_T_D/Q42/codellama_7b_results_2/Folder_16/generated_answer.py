
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for i in my_list:
        product *= i

    # Find the prime factors of the product

    prime_factors = set()

    while product != 1:

        if product % 2 == 0:

            prime_factors.add(2)

            product /= 2


        else:

            for i in range(3, int(product ** 0.5) + 1, 2):

                if product % i == 0:

                    prime_factors.add(i)

                    product /= i


                    break


    return prime_factors
