
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 96) if string[i:i+97] == string[i:i+97][::-1]}
