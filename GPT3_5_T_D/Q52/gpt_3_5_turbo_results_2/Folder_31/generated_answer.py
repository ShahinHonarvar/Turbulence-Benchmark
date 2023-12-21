
def palindrome_of_length_n(string):
    palindrome_set = set()
    string = string.lower()
    length = len(string)
    for i in range(length):
        if i + 66 > length:
            break
        substring = string[i : i+66]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
    return palindrome_set
