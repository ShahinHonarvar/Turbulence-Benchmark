
def palindromes_of_specific_lengths(s):
    s = s[32:72]
    palindromes = set()
    for length in range(21, 33):
        for index in range(len(s) - length + 1):
            potential_palindrome = s[index:index+length]
            if potential_palindrome.lower() == potential_palindrome[::-1].lower() and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes
