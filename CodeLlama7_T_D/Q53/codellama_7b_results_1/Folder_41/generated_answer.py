
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Create a copy of the string without the first character
            substr = string[i + 1:]
            # Check if the copy contains any palindromes of length greater than or equal to n
            for j in range(len(substr) - n + 1):
                substr_slice = substr[j:j + n]
                # Check if the slice is a palindrome
                if substr_slice == substr_slice[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(substr_slice)
    return palindromes
