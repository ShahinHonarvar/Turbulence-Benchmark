
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 65):
        sub_s = s[i:i+66]
        if sub_s == sub_s[::-1]:
            if sub_s.isalpha():
                palindromes.add(sub_s)
    return palindromes
