
def palindrome_of_length_at_least_n(string, n):
    # Convert the input string to lowercase for case-insensitive search
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the input string
    for i in range(len(string)):
        # Get the character at position i in the input string
        char = string[i]
        # If the character is not a letter, skip to the next iteration
        if not char.isalpha():
            continue

        # Iterate over the remaining characters in the input string, starting from position i + 1
        for j in range(i + 1, len(string)):
            # Get the character at position j in the input string
            other_char = string[j]
            # If the character is not a letter, skip to the next iteration
            if not other_char.isalpha():
                continue

            # Check if the substring starting at position i and ending at position j is a palindrome
            if char == other_char and string[i + 1:j] == string[i + 1:j][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:j + 1])
    # Return the set of palindromes with a length greater than or equal to n
    return palindromes
