
def palindrome_of_length_at_least_n(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i+90, length+1):
            segment = s[i:j]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes
