 def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start_index = 15
    end_index = 94
    substr = string[start_index:end_index+1]
    # Initialize an empty set to store palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a letter (a-z or A-Z)
        if substr[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate through each character in the substring from the current index to the end of the substring
            for j in range(i, len(substr)):
                # Check if the current character is a letter (a-z or A-Z) and add it to the palindrome string
                if substr[j].isalpha():
                    palindrome += substr[j]
            # Check if the palindrome has the correct length and consists of only English letters
            if len(palindrome) >= 18 and len(palindrome) <= 73 and all(c.isalpha() for c in palindrome)):
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes found in the substring from index 15 to index 94, both inclusive
    return palindromes
