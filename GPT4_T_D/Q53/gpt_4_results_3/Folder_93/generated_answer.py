
def palindrome_of_length_at_least_n(text):
    def is_palindrome(sub_text):
        return sub_text == sub_text[::-1]
        
    text = ''.join(filter(str.isalpha, text)).lower()
    length = len(text)
    result = set()
    for i in range(length):
        for j in range(i+90, length+1):
            if is_palindrome(text[i:j]):
                result.add(text[i:j])
    return result
