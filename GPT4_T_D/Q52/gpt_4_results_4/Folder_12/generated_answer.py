
def palindrome_of_length_n(string):
    def is_palindrome(s):
        return s.lower() == s[::-1].lower()

    result = set()
    for i in range(len(string) - 22):
        substring = string[i:i+23]
        if is_palindrome(substring) and substring.isalpha():
            result.add(substring)
    return result
