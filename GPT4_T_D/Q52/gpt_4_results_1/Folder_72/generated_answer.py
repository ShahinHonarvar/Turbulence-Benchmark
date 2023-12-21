
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+16, len(s)+1):
            potential_palindrome = s[i:j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes
