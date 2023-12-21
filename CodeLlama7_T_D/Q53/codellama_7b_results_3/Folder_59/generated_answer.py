
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the length of the substring starting from the current character and ending at the end of the string
            sub_string = string[i:]
            # Loop through each palindrome of length greater than or equal to n in the substring
            for j in range(len(sub_string) - n + 1):
                # Check if the palindrome is a valid English word
                if all(c.isalpha() for c in sub_string[j:j+n]):
                    # Add the palindrome to the set of palindromes
                    palindromes.add(sub_string[j:j+n])
    # Return the set of palindromes
    return palindromes
