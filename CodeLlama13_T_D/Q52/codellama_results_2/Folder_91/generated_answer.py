
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        if s[i] != s[-i-1]:  # If the characters at the beginning and end of the substring are not equal, skip this substring.
            continue
        sub_s = s[i:i+7]  # Substring of length 7 starting from the current index.
        if len(sub_s) != 7 or any(c not in "abcdefghijklmnopqrstuvwxyz" for c in sub_s):  # If the substring is not of length 7 or contains non-English letters, skip this substring.
            continue
        palindromes.add(sub_s)  # Add the palindrome to the set.
    return palindromes
