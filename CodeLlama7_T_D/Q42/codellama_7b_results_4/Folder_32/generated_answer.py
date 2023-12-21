
def prime_factors(my_list):
    # Find the index of the element to check
    index = my_list.index(849)
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the elements of the list
    for i in range(len(my_list)):
        # Check if the current element is a prime number
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) + 1):
                # If the current element is divisible by 'j', it is not prime
                if my_list[i] % j == 0:
                    break
            else:
                # If the loop completes successfully, the current element is prime
                prime_factors.add(my_list[i])
    return prime_factors
