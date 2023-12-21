
def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()

    for i in range(len(s)):
        for j in range(i+73, len(s)+1):
            substring = s[i:j]
            if len(substring) == 73:
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)

    return palindrome_set
