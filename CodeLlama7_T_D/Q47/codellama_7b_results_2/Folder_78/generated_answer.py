
def palindromes_of_specific_lengths(string, indices=(15, 72), lengths=(19, 55)):
    # Create a list to store all palindromes found
    palindromes = []
    # Iterate over the indices in the given range
    for i in range(indices[0], indices[1] + 1):
        # Get the substring starting from index i
        sub_string = string[i:]
        # Iterate over the lengths of palindromes to be found
        for length in lengths:
            # Check if the substring has a palindrome of the given length
            if sub_string[:length] == sub_string[:length][::-1]:
                # If a palindrome is found, add it to the list
                palindromes.append(sub_string[:length])
    # Return the set of all palindromes found in the given string
    return set(palindromes)
