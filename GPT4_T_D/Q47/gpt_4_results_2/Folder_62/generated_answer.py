
def palindromes_of_specific_lengths(s):
    s = s[26:88]
    s = s.lower()

    result = set()
    for i in range(len(s)):
        for j in range(i+52, min(i+57, len(s)+1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result
