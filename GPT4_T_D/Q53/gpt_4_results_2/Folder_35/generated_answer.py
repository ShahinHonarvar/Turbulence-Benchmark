
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes_set = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) >= 26:
                if substr.isalpha():
                    palindromes_set.add(substr)
    return palindromes_set
