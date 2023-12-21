 def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 31
    end = 91
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Create a copy of the substring starting from index i
            substr = string[i:]
            # Iterate over the characters in the copy of the substring
            for j in range(len(substr)):
                # Check if the character at index j is a letter
                if substr[j].isalpha():
                    # Create a palindrome by concatenating the letters from index i to index j
                    palindrome = string[i:j + 1]
                    # Check if the palindrome has a length between 50 and 53 (both inclusive)
                    if len(palindrome) >= 50 and len(palindrome) <= 53:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
