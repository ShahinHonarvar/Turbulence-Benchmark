
def palindromes_of_specific_lengths(string):
    # Define the range of indexes for the substring
    start_index = 43
    end_index = 95
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = (end_index - start_index) + 1
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over each character in the substring, starting from index i and ending at index end_index
            for j in range(i, end_index + 1):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Append the character at index j to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome has the required length and consists only of letters
            if len(palindrome) >= 18 and len(palindrome) <= 47 and all(char.isalpha() for char in palindrome)):
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
