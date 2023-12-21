
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 92 + 1) if string[i:i+92].isalpha() and string[i:i+92] == string[i:i+92][::-1]}
