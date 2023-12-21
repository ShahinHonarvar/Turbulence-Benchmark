 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (not a space or other non-letter character)
        if char.isalpha():
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Get the character at index j
                rev_char = string[j]
                # Check if the character is a letter (not a space or other non-letter character)
                if rev_char.isalpha():
                    # If the character at index i and the character at index j are the same, add the palindrome to the set
                    if char == rev_char:
                        palindromes.add(string[i:j+1])
            # Once all the characters in the reversed string have been checked, check if there are any palindromes of length greater than or equal to n
            for palindrome in palindromes:
                if len(palindrome) >= n:
                    return palindromes
    # If no palindromes were found, return an empty set
    return set()
