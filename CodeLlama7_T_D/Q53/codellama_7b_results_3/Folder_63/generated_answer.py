
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Check if the character is uppercase or lowercase
            if string[i].isupper():
                # Convert the character to lowercase
                lowercase_character = string[i].lower()
            else:
                # Keep the character as is (lowercase)
                lowercase_character = string[i]
            # Check if there are any palindromes of length greater than or equal to n that start with the current character
            if len(string) - i >= n and string[i:i + n].islower() == True and string[i:i + n][::-1] == string[i:i + n]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:i + n])
    # Return the set of all palindromes of length greater than or equal to 37 that exist in the given string
    return palindromes
