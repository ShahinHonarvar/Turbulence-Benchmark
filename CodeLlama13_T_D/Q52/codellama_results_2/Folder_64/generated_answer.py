
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:i+9]
        if len(substr) == 9 and substr.lower() == substr[::-1].lower():
            palindromes.add(substr)
    return palindromes
