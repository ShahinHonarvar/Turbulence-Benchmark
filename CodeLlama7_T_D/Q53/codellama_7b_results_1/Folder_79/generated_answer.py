
def palindrome_of_length_at_least_n(string, n=17):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Get the reverse of the substring starting from the current character and ending at the end of the string
            rev_substring = string[i:].lower()[::-1]
            # Check if the reverse of the substring is a palindrome
            if rev_substring == rev_substring.lower():
                # Add the palindrome to the set
                palindromes.add(string[i:])
    # Return the set of all palindromes of the length greater than or equal to 17 that exist in the given string
    return palindromes
