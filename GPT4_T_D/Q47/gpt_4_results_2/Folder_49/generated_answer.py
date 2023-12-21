
def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    for length in range(10, 51):
        for i in range(10, 101 - length):
            possible_palindrome = s[i:i+length].lower()
            if possible_palindrome.isalpha() and possible_palindrome == possible_palindrome[::-1]:
                palindrome_set.add(possible_palindrome)
    return palindrome_set
