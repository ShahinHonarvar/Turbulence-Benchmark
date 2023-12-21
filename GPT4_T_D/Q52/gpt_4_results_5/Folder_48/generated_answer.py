
def palindrome_of_length_n(string):
    string = string.lower()
    substrings = set()
    length = 186
    
    for i in range(len(string)):
        if i + length > len(string):
            break
        substring = string[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            substrings.add(substring)
    return substrings
