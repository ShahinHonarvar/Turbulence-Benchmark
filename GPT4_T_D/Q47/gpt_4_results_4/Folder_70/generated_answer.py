
def palindromes_of_specific_lengths(s):
    s = s[10:71]
    result = set()
    for i in range(len(s)):
        for j in range(i+24, min(i+53, len(s)+1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result
