
def palindrome_of_length_n(s):
    return {ss for i in range(len(s)-90) if ss[::-1] == s[i:i+90].lower()}
