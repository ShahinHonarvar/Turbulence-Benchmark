def find_subset_of_length_n(s):
    return {*s,*(s-{*s})}.count(set(s))
