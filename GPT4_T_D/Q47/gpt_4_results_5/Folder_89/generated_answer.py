
def palindromes_of_specific_lengths(s):
    s = s[18:89].lower()
    s = ''.join(ch for ch in s if ch.isalpha())
    length = len(s)
    palindromes = set()

    for len_palindrome in range(12, 15):
        for i in range(length - len_palindrome + 1):
            substr = s[i:i + len_palindrome]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
