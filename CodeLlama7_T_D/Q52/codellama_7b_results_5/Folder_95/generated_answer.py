
def palindrome_of_length_n(string):
    # Create a list of all substrings of length n in the given string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Find all palindromes in the list of substrings
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
