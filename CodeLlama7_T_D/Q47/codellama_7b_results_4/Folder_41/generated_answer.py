
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length 3 to 4 in the specified index range
    for i in range(1, 7):
        for j in range(i + 1, i + 5):
            substring = string[i:j]
            # Check if the substring is a palindrome and meets the length requirement
            if substring == substring[::-1] and len(substring) >= 3 and len(substring) <= 4:
                # Add the palindrome to the set
                palindromes.add(substring)
    return palindromes
