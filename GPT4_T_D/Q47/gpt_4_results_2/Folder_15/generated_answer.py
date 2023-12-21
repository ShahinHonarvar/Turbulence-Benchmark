
def palindromes_of_specific_lengths(s):
    s = s[0:7].lower()
    palindromes_set = set()

    for length in range(3, 7):
        for start in range(len(s) - length + 1):
            substring = s[start:start+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes_set.add(substring)
                
    return palindromes_set
