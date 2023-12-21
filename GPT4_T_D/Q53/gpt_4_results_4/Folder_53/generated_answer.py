
def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    for i in range(len(s)):
        for j in range(i + 64, len(s) + 1):
            potential_palindrome = s[i:j]
            if potential_palindrome == potential_palindrome[::-1]:
                palindrome_set.add(potential_palindrome)
    return palindrome_set
