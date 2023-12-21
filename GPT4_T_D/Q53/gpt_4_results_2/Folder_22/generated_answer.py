
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    all_palindromes = set()

    for i in range(len(s)):
        for j in range(i + 97, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                all_palindromes.add(substring)
    
    return all_palindromes
