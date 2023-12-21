
def palindrome_of_length_at_least_n(string):
    palindrome_set = set()
    string = string.lower()
    for i in range(len(string) - 44 + 1):
        for j in range(i + 44, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
