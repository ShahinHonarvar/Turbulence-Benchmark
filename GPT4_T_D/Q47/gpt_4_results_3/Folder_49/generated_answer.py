
def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    result = set()
    for length in range(10, 51):
        for start in range(0, len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
