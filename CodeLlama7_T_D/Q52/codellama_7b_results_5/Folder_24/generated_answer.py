
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the string
    for i in range(len(string)):
        # Calculate the length of the substring starting at index i
        substring_length = len(string) - i

        # If the length is greater than or equal to 29, continue
        if substring_length < 29:
            continue

        # Loop through each character in the substring
        for j in range(i, i + 29):
            # Check if the substring is a palindrome
            if string[j] == string[j + 28]:
                # Add the palindrome to the set
                palindromes.add(string[j:j + 29])

    # Return the set of palindromes
    return palindromes
