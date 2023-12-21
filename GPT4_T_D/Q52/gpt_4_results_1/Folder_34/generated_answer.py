
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s == s[::-1]
    
    s = "".join(char for char in s.lower() if char.isalpha())
    palindromes = set()

    for i in range(len(s) - 32):
        substring = s[i:i + 33]
        if is_palindrome(substring):
            palindromes.add(substring)

    return palindromes
