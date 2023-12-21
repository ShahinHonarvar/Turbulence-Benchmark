
def palindromes_of_specific_lengths(s):
    target_substr = s[103:277]
    palindromes = set()
    for start in range(len(target_substr)-169):
        for length in range(100, 170):
            substring = target_substr[start:start+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes
