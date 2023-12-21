
def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+50, min(i+54, len(s)+1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindrome_set.add(s[i:j])
    return palindrome_set
