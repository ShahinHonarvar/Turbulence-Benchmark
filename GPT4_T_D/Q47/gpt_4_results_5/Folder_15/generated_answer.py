
def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    alphanumeric_s = ''.join(ch for ch in s if ch.isalpha())
    set_of_palindromes = set()
    for i in range(len(alphanumeric_s)):
        for j in range(i+3, min(i+7, len(alphanumeric_s)+1)):
            substring = alphanumeric_s[i:j]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes
