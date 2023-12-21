
def palindrome_of_length_at_least_n(string, n):
    return {palindrome for palindrome in re.findall(r"([a-zA-Z]{" + str(n) + ",})", string) if len(palindrome) == len(set(palindrome))}
