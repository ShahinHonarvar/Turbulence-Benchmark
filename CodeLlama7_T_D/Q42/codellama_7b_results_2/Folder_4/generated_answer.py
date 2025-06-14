
def prime_factors(my_list):
    # Find the number to factorize
    num = my_list[15]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        # If i is a factor of num, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
            # If i*i is less than or equal to num, it is also a prime factor
            if i * i <= num:
                prime_factors.add(i * i)
    return prime_factors
