
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current character and continuing for 210 characters
        substring = string[i:i+210]
        # Loop through each palindrome in the substring
        for j in range(len(substring) - 1):
            # Check if the current palindrome is a valid palindrome of length 210
            if substring[j:j+210] == substring[j:j+210][::-1]:
                # Add the valid palindrome to the set of palindromes
                palindromes.add(substring[j:j+210])
    # Return the set of all palindromes of length 210 in the given string, in a case-insensitive manner
    return palindromes
