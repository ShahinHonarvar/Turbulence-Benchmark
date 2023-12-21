
def all_neg_ints_exclusive(int_list):

    # Get the portion of the list from index 599 to 766 (both inclusive)
    portion = int_list[599:767]

    # Filter out all non-negative integers
    negatives = [x for x in portion if x < 0]
    
    return negatives
