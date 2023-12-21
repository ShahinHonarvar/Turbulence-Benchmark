
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
