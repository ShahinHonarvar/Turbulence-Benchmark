
def palindromes_of_specific_lengths(input_string):
    def is_palindrome(s):
        s = s.lower()
        return s.isalpha() and s == s[::-1]
    
    input_string = input_string[106:281]
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i+136, min(i+152, len(input_string)+1)):
            substring = input_string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
