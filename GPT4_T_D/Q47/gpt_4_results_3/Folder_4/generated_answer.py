
def palindromes_of_specific_lengths(s):
    s = s[12:93]
    result = set()
    for start in range(len(s)):
        for end in range(start, len(s)):
            substring = s[start:end+1]
            if 17 <= len(substring) <= 66 and substring.lower() == substring[::-1].lower():
                if substring.isalpha():
                    result.add(substring)
    return result
