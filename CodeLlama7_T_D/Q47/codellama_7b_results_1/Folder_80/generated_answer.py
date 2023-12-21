
def palindromes_of_specific_lengths(string):
    # Define the index range for consideration
    start_index = 35
    end_index = 88
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the specified index range
    for i in range(start_index, end_index + 1):
        # Check if the character at position i is a letter
        if string[i].isalpha():
            # Define the substring starting from position i to the end of the string
            substr = string[i:]
            # Iterate over the characters in the substring
            for j in range(len(substr)):
                # Check if the character at position j is a letter
                if substr[j].isalpha():
                    # Define the palindrome as the substring starting from position i to position j (exclusive)
                    palindrome = substr[:j]
                    # Check if the palindrome has the desired length and consists only of English letters
                    if len(palindrome) in range(24, 34) and all(char.isalpha() for char in palindrome)):
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes found
    return palindromes
