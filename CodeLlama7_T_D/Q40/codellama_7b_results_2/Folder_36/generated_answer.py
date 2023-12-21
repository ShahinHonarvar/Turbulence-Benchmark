
def return_n_smallest_chars(s: str, n=32) -> list[str]:
    """
    Return a list of exactly n smallest ASCII values
    from the given string s.

    Parameters
    ----------
    s : str
        A string of distinct characters
    n : int, default 32
        The number of smallest ASCII values to return

    Returns
    -------
    list[str]
        A list of exactly n smallest ASCII values from the given string s.

    Examples
    --------
    >>> return_n_smallest_chars("abcdef", 2)
    ['a', 'b']
    """

    # convert the string to a list of characters
    chars = list(s)

    # sort the list of characters by ASCII value
    chars.sort(key=ord)

    # return the first n elements of the sorted list
    return chars[:n]
