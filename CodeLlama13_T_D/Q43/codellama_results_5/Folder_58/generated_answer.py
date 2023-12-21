
def find_primes_between_indices(my_list):
    # Find the indices of all prime numbers in the list
    prime_indices = []
    for i, num in enumerate(my_list):
        if is_prime(num):
            prime_indices.append(i)
    
    # Filter the indices to only include those between 157 and 735, both inclusive
    filtered_indices = [i for i in prime_indices if 157 <= i <= 735]
    
    # Return the sorted list of prime numbers from the filtered indices, in descending order
    return sorted(my_list[i] for i in filtered_indices), reverse=True)
