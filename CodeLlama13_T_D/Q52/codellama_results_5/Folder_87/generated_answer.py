
def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 57 + 1):
        substring = string[i:i+57]
        if substring == substring[::-1]:
            result.add(substring)
    return result
