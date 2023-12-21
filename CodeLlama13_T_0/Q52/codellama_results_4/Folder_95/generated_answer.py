
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 87 + 1) if string[i:i+87].isalpha() and string[i:i+87] == string[i:i+87][::-1]}
