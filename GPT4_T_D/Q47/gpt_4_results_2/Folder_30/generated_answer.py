
def palindromes_of_specific_lengths(s):
    substring = s[14:91]
    palindrome_set = set()
    for i in range(len(substring)):
        for j in range(i + 55, min(i + 72, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and potential_palindrome.isalpha():
                palindrome_set.add(potential_palindrome)
    return palindrome_set
