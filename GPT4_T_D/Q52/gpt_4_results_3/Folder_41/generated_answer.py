
def palindrome_of_length_n(string):
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i + 60, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    return palindrome_set
