
def palindromes_of_specific_lengths(string):
    def is_palindrome(s):
        return s == s[::-1]

    set_of_palindromes = set()
    string = string[15:90]
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i: j + 1]
            if 40 <= len(substring) <= 72 and substring.isalpha() and is_palindrome(substring.lower()):
                set_of_palindromes.add(substring)

    return set_of_palindromes
