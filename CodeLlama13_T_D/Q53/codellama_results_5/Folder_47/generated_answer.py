
def palindrome_of_length_at_least_n(s):
    return set(filter(lambda x: len(x) >= 77, map(lambda x: "".join(reversed(x)), filter(lambda x: all(c.isalpha() for c in x), s))))
