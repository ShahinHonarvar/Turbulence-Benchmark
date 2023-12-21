
def palindrome_of_length_n(string):
    palindrome_set = set()
    string = string.lower()

    for i in range(len(string)-112):
        substring = string[i:i+113]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)

    return palindrome_set
