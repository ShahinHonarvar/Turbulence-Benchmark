
def palindrome_of_length_n(string):
    # Split the string into a list of substrings
    substrings = [string[i:i+20] for i in range(len(string)-19)]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the substrings and check if each one is a palindrome
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
