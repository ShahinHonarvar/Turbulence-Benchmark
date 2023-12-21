
def palindrome_of_length_n(string):
    # Split the string into substrings of length n
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate over the substrings and check if they are palindromes
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
