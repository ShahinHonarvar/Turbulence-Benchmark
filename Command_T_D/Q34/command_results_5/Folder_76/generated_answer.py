def find_original_set(x):
    # Write your code here. Read input from STDIN. Print output to STDOUT
    original_set = set()
    for s in x:
        original_set |= s
    return original_set
