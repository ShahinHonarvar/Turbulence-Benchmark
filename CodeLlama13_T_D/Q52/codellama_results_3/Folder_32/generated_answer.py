
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 112):
        substr = string[i:i+113]
        if len(substr) == 113 and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes
