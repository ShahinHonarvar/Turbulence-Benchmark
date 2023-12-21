
def palindrome_of_length_at_least_n(string, n):
    return {palindrome for palindrome in re.findall("[a-zA-Z]{" + str(n) + ",}", string) if palindrome == palindrome[::-1]}
