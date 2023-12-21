
def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 96, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set  
