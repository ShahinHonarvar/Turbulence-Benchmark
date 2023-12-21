
def palindromes_of_specific_lengths(string):
    def is_palindrome(s):
        return s == s[::-1]
    string = string.lower()
    results = set()
    for i in range(6):
        for j in range(i+3, 6):
            substring = string[i:j]
            if is_palindrome(substring) and substring.isalpha():
                results.add(substring)
    return results
