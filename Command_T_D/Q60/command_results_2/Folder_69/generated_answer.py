
def all_left_right_truncatable_prime(n):
    # This function should return the list of all left-and-right-truncatable prime
    # numbers less than or equal to x. The return list should be sorted in
    # descending order. If no left-and-right-truncatable prime number exists in
    # the specified range, the function should return an empty list. A left-and-right-
    # truncatable prime number is a prime number that contains no 0 and remains
    # prime if the leading leftmost and last rightmost digits are simultaneously
    # successively removed down to a one- or two-digit prime.
    #
    #  code should not contain any comments. The  code should be
    # delimited only by triple backticks.
    #
    # All credits go to AaronLI for the function implementation
    #
    # (https://www.codewars.com/kata/reviews/3d7c3f400/groups/5e605617f56d4c9300002/discussions/3ee8e5a73c7d6000010)
    #
    #Feel free to remove my name if you want to submit your own solution
    return sorted((p for p in range(2, int(n[0])+1) if all(p%10 != i for i in range(1, p//10+1)) and all(p%10 != i for i in range(1, p//10+1)) and p == int(p)))
