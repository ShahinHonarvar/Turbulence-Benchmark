
def palindromes_of_specific_lengths(input_string):
    import string
    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    palindromes = set()
    substring = input_string[63:71]
    for length in range(4, 6):
        for i in range(0, len(substring) - length + 1):
            s = substring[i:i+length]
            if s.isalpha() and is_palindrome(s):
                palindromes.add(s)
    return palindromes
