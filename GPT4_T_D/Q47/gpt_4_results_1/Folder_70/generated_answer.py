
def palindromes_of_specific_lengths(s):
    s = s[10:71]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()

    for len_palindrome in range(24, 53):
        for start_index in range(len(s) - len_palindrome + 1):
            substring = s[start_index: start_index + len_palindrome]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
