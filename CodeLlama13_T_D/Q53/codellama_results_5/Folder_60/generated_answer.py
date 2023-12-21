
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(80, len(string)):
        if string[i-80:i+1].lower() == string[i-80:i+1][::-1].lower():
            palindromes.add(string[i-80:i+1])
    return palindromes
