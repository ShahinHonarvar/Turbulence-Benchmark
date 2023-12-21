
def palindrome_of_length_n(string, n):
    return set((x[1:-1],) for x in re.findall(r'(\w{' + str(n) + r'}[\w\s]*?\b[\w\s]{' + str(n) + r'}\b)', string))
