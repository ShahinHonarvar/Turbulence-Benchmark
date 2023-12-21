
def palindrome_of_length_n(str):
    str = str.lower()
    palindrome_set = set()
    for i in range(len(str)):
        for j in range(i+68, len(str)+1):
            substring = str[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                palindrome_set.add(substring)
    return palindrome_set
