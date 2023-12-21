
def prime_factors(my_list):
    # Find the prime factor of the integer at index 80
    prime_factor = 2
    while True:
        if my_list[80] % prime_factor == 0:
            break
        else:
            prime_factor += 1

    return {prime_factor}
