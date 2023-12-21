
def palindromes_of_specific_lengths(string):
    substr = string[28:95]
    palindromes = set()
    for length in range(38, 50):
        for i in range(0, len(substr) - length + 1):
            potential_palindrome = substr[i:i+length]
            if (potential_palindrome == potential_palindrome[::-1] and
                    potential_palindrome.isalpha()):
                palindromes.add(potential_palindrome.lower())
    return palindromes
