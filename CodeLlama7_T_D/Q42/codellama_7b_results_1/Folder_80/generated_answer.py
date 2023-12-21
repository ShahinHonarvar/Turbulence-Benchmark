
def prime_factors(my_list):
    # Find the prime factor of the integer at index 746
    prime_factor = 2
    while prime_factor ** 0.5 <= my_list[746]:
        if my_list[746] % prime_factor == 0:
            break

        else:

            prime_factor += 1

    return {prime_factor}
