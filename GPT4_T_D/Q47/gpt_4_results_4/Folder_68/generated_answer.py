
def palindromes_of_specific_lengths(s):
    s = s[0:51]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if 50 <= len(substring) <= 100 and substring == substring[::-1]:
                sanitized_substring = ''.join(filter(str.isalpha, substring))
                if sanitized_substring.lower() == sanitized_substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes
