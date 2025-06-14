
def find_primes_between_indices(my_list):
    # Find the first prime number in the range
    start = 14
    while not is_prime(start):
        start += 1

    # Find the last prime number in the range

    end = 68
    while not is_prime(end):
        end -= 1

    # Return the sorted list of prime numbers between the indices

    return sorted([num for num in my_list[start:end+1] if is_prime(num)], reverse=True)

# Check if a number is prime

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
