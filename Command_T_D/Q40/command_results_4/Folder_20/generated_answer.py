def return_n_smallest_chars(s):
    return [x for x in s if x.isalpha()] + [x for x in s if x.isdigit()] + [x for x in s if x.isupper()] + [x for x in s if x.islower()] + [x for x in s if x.isspace()]
