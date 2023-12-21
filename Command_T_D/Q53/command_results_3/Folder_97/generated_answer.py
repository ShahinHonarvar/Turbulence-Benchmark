def palindrome_of_length_at_least_n(s):
    return set(s.lower().replace(" ","").split("").lstrip("a").rstrip("z").split(""))
