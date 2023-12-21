
def palindromes_of_specific_lengths(string):
    def is_palindrome(s):
        return s == s[::-1]

    string = string[45:99]
    result = set()
    for i in range(len(string)):
        for j in range(i+40, min(i+48, len(string)+1)): 
            substr = string[i:j]
            if substr.isalpha() and is_palindrome(substr.lower()):
                result.add(substr)
    return result
