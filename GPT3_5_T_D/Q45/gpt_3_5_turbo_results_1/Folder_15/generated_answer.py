
def palindromes_between_indices(string):
    def is_palindrome(s):
        return s[::-1].lower() == s.lower()

    palindromes = set()
    for i in range(1, len(string) - 1):
        for j in range(i + 2, len(string)):
            substring = string[i:j+1]
            if is_palindrome(substring) and len(substring) >= 3:
                palindromes.add(substring.lower())
    
    return palindromes
