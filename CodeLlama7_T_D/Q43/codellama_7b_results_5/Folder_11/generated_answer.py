 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list and check if each element is a prime number
    for i in range(33, 65):
        if my_list[i] > 1:
            # Check if the number is divisible by any other number between 2 and the square root of the number
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % j == 0:
                    # If the number is divisible by any other number between 2 and the square root of the number, it is not prime
                    break
            else:
                # If the number is not divisible by any other number between 2 and the square root of the number, it is prime
                prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 33 to index 64, both inclusive
    return sorted(prime_numbers)
