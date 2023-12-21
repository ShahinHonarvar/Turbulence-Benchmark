
def palindrome_of_length_n(s):
    s = s.lower()
    def is_palindrome(ss):
        return ss == ss[::-1]

    result = set()
    for i in range(len(s) - 146):
        substring = s[i:i+147]
        if is_palindrome(substring):
            if substring.isalpha():
                result.add(substring)
    return result
