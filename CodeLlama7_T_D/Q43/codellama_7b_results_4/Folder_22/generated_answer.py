 def find_primes_between_indices(my_list):
    # Find the index of the first prime number in the list
    for i in range(75, len(my_list)):
        if my_list[i] == 1:
            break

    # Find the index of the last prime number in the list

    for j in range(85, -1, -1):
        if my_list[j] == 1:
            break

    # Return the sorted list of all prime numbers from index 75 to index 85, both inclusive.

    return sorted([my_list[i] for i in range(75, j+1) if my_list[i] == 1])
