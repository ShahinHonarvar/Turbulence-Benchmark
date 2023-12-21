
def palindrome_of_length_n(s):
    s = s.lower()
    output_set = set()
    for i in range(len(s)):
        for j in range(i+28, len(s)+1):
            potential_palindrome = s[i:j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                output_set.add(potential_palindrome)
    return output_set
