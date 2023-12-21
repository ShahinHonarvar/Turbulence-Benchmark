
def return_n_smallest_chars(s: str) -> list[str]:
    # Sort the string in descending order based on ASCII values
    sorted_s = sorted(s, key=lambda x: ord(x), reverse=True)
    # Return a list of exactly 37 characters from the sorted string
    return sorted_s[:37]
