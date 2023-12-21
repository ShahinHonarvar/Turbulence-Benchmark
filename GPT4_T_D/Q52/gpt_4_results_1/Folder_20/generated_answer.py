
def palindrome_of_length_n(string):
    string = string.lower()
    palindrome_set = set()

    for i in range(len(string) - 52):
        substring = string[i : i + 53]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)

    return palindrome_set
