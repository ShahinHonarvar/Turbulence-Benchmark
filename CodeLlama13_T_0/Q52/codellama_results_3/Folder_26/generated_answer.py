
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 365) if string[i:i+366].isalpha() and string[i:i+366][::-1] == string[i:i+366]}
