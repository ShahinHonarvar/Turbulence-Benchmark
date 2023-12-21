
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(43, 95 + 1):
        substr = string[i - 43:i - 42 + 1]
        if is_palindrome(substr) and len(substr) >= 18 and len(substr) <= 47:
            palindromes.append(substr)
    return set(palindromes)

def is_palindrome(string):

    # Check if the given string is a palindrome

    return string == string[::-1]
