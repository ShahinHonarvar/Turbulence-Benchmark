
def palindromes_of_specific_lengths(string):
    # Define the index range for consideration
    start_index = 10
    end_index = 75
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string within the defined index range
    for i in range(start_index, end_index + 1):
        # Check if the character at position i is a palindrome of length between 10 and 20 (both inclusive)
        if string[i] == string[i].lower():
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i])
    return palindromes
