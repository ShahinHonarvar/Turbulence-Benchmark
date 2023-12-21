
def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(5):
        for j in range(i+3, min(i+5, 5)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
