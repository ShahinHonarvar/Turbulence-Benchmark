
def find_n_th_smallest_num(distinct_numbers, n, start_idx, end_idx):
    """
    Finds the nth smallest number in a list of distinct numbers between indices start_idx and end_idx (inclusive).

    Args:
        distinct_numbers (list): A list of distinct numbers.
        n (int): The position of the smallest number to find.
        start_idx (int): The starting index from which to consider the sublist.
        end_idx (int): The ending index at which to consider the sublist.
    Returns:
        int: The nth smallest number in the sublist.
    """
    if not distinct_numbers or len(distinct_numbers) == 0:
        return None
    if start_idx < 0 or end_idx >= len(distinct_numbers):
        raise IndexError("Invalid indices")
    if n < 1 or n > end_idx - start_idx + 1:
        raise ValueError("n must be between 1 and the length of the sublist, inclusive")
    return sorted(distinct_numbers[start_idx:end_idx+1])[n-1]
