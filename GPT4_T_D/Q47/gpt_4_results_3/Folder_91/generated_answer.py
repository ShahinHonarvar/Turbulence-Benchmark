
def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_set = set()
    for i in range(11):
        for j in range(3,6):
            if i + j <= 11:
                substring = s[i:i+j]
                if substring.isalpha() and substring == substring[::-1]:
                    valid_set.add(substring)
    return valid_set
