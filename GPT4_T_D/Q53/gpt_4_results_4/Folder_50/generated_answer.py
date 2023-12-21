
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+91, len(string)+1):
            segment = string[i:j]
            if segment == segment[::-1]: 
                if segment.isalpha():
                    palindromes.add(segment)
    return palindromes
