
def palindrome_of_length_n(string):
    string = string.lower()
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) == 181 and substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
