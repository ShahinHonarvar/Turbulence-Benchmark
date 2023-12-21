
def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 275):
        substring = string[i:i+276]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
