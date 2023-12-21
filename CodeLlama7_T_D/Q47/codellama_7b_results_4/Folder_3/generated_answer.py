 def palindromes_of_specific_lengths(string):
    # Define the index range for which we want to find palindromes
    start_index = 27
    end_index = 95
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(start_index, end_index + 1):
        # Check if the current character is a palindrome of length 49 to 51
        if string[i - 27:i - 26] == string[i - 26:i - 25][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i - 27:i - 26])
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
