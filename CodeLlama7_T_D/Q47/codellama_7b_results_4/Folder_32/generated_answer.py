
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 16
    end_index = 77
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(start_index, end_index + 1):
        # Check if the current character is a palindrome
        if string[i] == string[i]:
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over each character in the substring starting from the current index
            for j in range(i, i + 47):
                # Check if the current character is a palindrome
                if string[j] == string[j]:
                    # Add the current character to the palindrome
                    palindrome += string[j]
        # Check if the palindrome has the desired length
        if len(palindrome) >= 43 and len(palindrome) <= 47:
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
