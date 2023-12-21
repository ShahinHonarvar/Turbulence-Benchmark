
def palindrome_of_length_at_least_n(string, n=96):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at the end of the string
        substr = string[i:]
        # Loop through each character in the reversed substring
        for j in range(len(substr)-1, -1, -1):
            # If the character at index j is not a letter, continue to the next iteration
            if not substr[j].isalpha():
                continue

            # Get the substring starting at index 0 and ending at index j
            substr2 = substr[:j+1]
            # Check if the substring is a palindrome
            if substr2 == substr2[::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(substr2)
    # Return the set of palindromes
    return palindromes
