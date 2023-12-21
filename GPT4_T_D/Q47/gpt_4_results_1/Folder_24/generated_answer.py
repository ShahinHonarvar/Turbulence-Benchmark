
def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+42, min(i+78, len(s)+1)):
            if all(char in valid_chars for char in s[i:j]):
                if s[i:j] == s[i:j][::-1]:
                    palindrome_set.add(s[i:j])
    return palindrome_set
