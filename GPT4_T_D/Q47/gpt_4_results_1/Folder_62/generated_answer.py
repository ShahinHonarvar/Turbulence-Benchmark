
def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 52, min(i + 57, len(s) + 1)):
            possible_palindrome = s[i:j]
            if possible_palindrome == possible_palindrome[::-1] and possible_palindrome.isalpha():
                result.add(possible_palindrome)
    return result
