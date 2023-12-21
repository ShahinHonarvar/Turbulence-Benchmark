
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    for length in range(150, len(s) + 1):
        for start in range(0, len(s) - length + 1):
            possible_palindrome = s[start:start + length]
            if possible_palindrome == possible_palindrome[::-1] and possible_palindrome.isalpha():
                palindromes.add(possible_palindrome)

    return palindromes
