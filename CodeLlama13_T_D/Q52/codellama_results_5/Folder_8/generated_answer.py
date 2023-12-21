
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 49 + 1) for palindrome in (string[i:i+49] if string[i:i+49].lower() == string[i:i+49][::-1].lower() else [])}
