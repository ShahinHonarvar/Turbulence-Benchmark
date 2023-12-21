
def palindrome_of_length_n(string):
    def is_palindrome(s):
        return s == s[::-1]
        
    string = "".join(filter(str.isalpha, string)).lower()
    palindromes = set()
    for i in range(len(string) - 38):
        substring = string[i:i+39]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes
