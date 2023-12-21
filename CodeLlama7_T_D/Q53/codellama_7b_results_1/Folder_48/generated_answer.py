
def palindrome_of_length_at_least_n(s, n):
    # Create a dictionary to store the palindromes
    palindromes = {}

    # Iterate over the characters in the string
    for i in range(len(s)):
        # Check if the character is an English letter
        if s[i].isalpha():
            # Create a variable to store the reverse of the string
            reversed_string = ""

            # Iterate over the characters in the string from the current index to the end
            for j in range(i, len(s)):
                # Add the character to the reverse of the string
                reversed_string += s[j]

            # Check if the reverse of the string is a palindrome
            if reversed_string == s[i:]:
                # Add the palindrome to the dictionary
                palindromes[s[i:]] = len(palindromes) + 1

    # Return the set of all palindromes of length greater than or equal to n that exist in the given string
    return set(palindromes.keys())
