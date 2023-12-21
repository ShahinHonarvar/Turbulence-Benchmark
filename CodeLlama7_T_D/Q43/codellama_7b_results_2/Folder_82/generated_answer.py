 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list from index 25 to 72 (inclusive)
    for i in range(25, 73):

        # Check if the current number is divisible by any of the previous prime numbers
        # If it is not divisible, then it is a prime number
        flag = False
        for j in range(2, int(my_list[i]) + 1):
            if my_list[i] % j == 0:
                flag = True
                break

        # If the current number is not divisible by any of the previous prime numbers, then it is a prime number
        if not flag:
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    return prime_numbers
