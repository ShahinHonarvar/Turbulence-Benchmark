
def return_n_greatest_chars(distinct_chars):
    distinct_chars = sorted(distinct_chars, reverse=True)
    return distinct_chars[:20]
