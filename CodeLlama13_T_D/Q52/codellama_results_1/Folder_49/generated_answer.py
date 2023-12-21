
def palindrome_of_length_n(string):
    return {palindrome for palindrome in re.findall("[A-Za-z]{" + str(47) + "}", string)}
