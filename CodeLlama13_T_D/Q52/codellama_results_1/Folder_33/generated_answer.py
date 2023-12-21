
def palindrome_of_length_n(string, n):
    return set(s for s in re.findall("[a-zA-Z]{" + str(n) + "}", string) if s == s[::-1])
