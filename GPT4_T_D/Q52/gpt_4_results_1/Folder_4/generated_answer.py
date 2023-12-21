
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = 15
    for i in range(len(s)):
        for j in range(i+length, len(s)+1):
            sub_string = s[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes
