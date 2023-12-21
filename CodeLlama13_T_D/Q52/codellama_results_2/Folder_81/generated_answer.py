
def palindrome_of_length_n(string, n):
    return {x for x in re.findall('(?i)(?<=^|[^A-Za-z])([A-Za-z]{%s})(?!=[A-Za-z])' % n, string) if len(x) == n}
