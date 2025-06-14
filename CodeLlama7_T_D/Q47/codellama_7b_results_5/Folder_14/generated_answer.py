
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 10
    end_index = 74

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each character in the substring
    for i in range(start_index, end_index + 1):
        # Check if the current character is a palindrome of length 6 to 8
        if string[i - 6:i] == string[i - 6:i][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i - 6:i])

    # Return the set of all palindromes found in the specified index range
    return palindromes
