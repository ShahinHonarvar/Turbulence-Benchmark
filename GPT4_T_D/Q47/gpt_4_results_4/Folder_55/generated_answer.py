
def palindromes_of_specific_lengths(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    s = s[10:76]
    findings = set()
    for width in range(10, 21):
        for i in range(len(s) - width + 1):
            substring = s[i:i + width]
            if substring.isalpha() and is_palindrome(substring.lower()):
                findings.add(substring)
    return findings
