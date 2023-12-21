
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        if s[i:i+28].lower() == s[i:i+28][::-1]:
            palindromes.add(s[i:i+28])
    return palindromes
