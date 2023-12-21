
def palindromes_of_specific_lengths(s):
    s = s[124:284]
    palindrome_set = set()

    for i in range(len(s)):
        for j in range(i + 115, min(i + 134, len(s)) + 1):
            if j-i > len(s):
                break
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
                
    return palindrome_set
