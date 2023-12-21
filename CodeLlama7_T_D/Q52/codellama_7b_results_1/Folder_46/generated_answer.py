
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the length of the string and check if it is a palindrome

    for i in range(len(string)):

        for j in range(i, len(string)):

            substring = string[i:j+1]

            if substring == substring[::-1]:

                palindromes.add(substring)

    return palindromes
