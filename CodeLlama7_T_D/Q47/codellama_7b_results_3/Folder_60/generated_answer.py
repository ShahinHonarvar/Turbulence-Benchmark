 def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 23
    end_index = 82
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the specified substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index 'i' is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Define the lowercase version of the character at index 'i'
            lowercase = string[i].lower()
            # Iterate over the characters in the substring starting from index 'i' and ending at index 'end_index' (inclusive)
            for j in range(i, end_index + 1):
                # Check if the character at index 'j' is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Define the lowercase version of the character at index 'j'
                    lowercase2 = string[j].lower()
                    # Check if the characters at indices 'i' and 'j' are the same (ignoring case)
                    if lowercase == lowercase2:
                        # Define the palindrome as the substring starting from index 'i' and ending at index 'j' (inclusive)
                        palindrome = string[i:j+1]
                        # Check if the length of the palindrome is between 32 and 34 (both inclusive)
                        if len(palindrome) >= 32 and len(palindrome) <= 34:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(palindrome)
    return palindromes
