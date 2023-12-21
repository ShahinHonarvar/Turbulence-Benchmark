
def return_n_greatest_chars(s):
    assert len(set(s)) >= 79, "String should have at least 79 distinct characters."
    sorted_s = sorted(set(s), reverse=True)
    return sorted_s[:79]
