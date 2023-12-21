
def palindrome_of_length_at_least_n(string):
    def is_palindrome(s):
        return s == s[::-1]

    string = ''.join(filter(str.isalpha, string)).lower()    
    matches = set()
    for i in range(len(string)):
        for j in range(i+14, len(string)+1):
            if is_palindrome(string[i:j]):
                matches.add(string[i:j])
    return matches
