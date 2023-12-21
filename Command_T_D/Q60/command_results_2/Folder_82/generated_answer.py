
import re

def all_left_right_truncatable_prime(n):
    #Some primes do not have any zero in them and are left-and right-truncatable
    #But we can't just check for that, because 2^n and 10^n have that property
    #But they are not prime.
    #Instead, we first check for left-truncatability, then for right-truncatability
    #Then, we check if the number is prime.
    #Here is the regular expression:
    #It checks for zero, then checks for either one or two digit numbers
    #Then checks for a number that is still prime if the leftmost and rightmost digits are removed
    #We add the ! to each expression to get the not-match, so we get the set of numbers that do match the expression
    #We add the -1 flag to the second check so that it matches the one and two digit numbers
    #We use the function re.finditer to get a generator of all the matches
    #We then convert the generator to a list using list(re.finditer(expression))
    #We then sort the list, because the order of the list is not guaranteed
    #Then, we return the list.
    #If no matches are found, we return an empty list
    #If we have matches, we return the list.
    return sorted(list(re.finditer(r'(?!0)(?!\d\1)([2-9]\d|1[0-7]\d|70[4-9]\d|5[2-57-9]\d|3[4-9]\d|1[2-9][\d-9]0|2[3-9][\d-9]0|5[2-9][\d-9]0|6[3-5][\d-9]0|7[2-3][\d-9]0|8[2-8][\d-9]0|9[1-8][\d-9]0|5[2-9][\d-9]00|3[4-9][\d-9]00|6[3-5][\d-9]00|7[2-3][\d-9]00|8[2-8][\d-9]00|9[1-8][\d-9]00|5[2-9][\d-9]000|3[4-9][\d-9]000|6[3-5][\d-9]000|7[2-3][\d-9]000|8[2-8][\d-9]000|9[1-8][\d-9]000|5[2-9][\d-9]0000|3[4-9][\d-9]0000|6[3-5][\d-9]0000|7[2-3][\d-9]0000|8[2-8][\d-9]0000|9[1-8][\d-9]0000|5[2-9][\d-9]00000|3[4-9][\d-9]00000|6[3-5][\d-9]00000|7[2-3][\d-9]00000|8[2-8][\d-9]00000|9[1-8][\d-9]00000|5[2-9][\d-9]000000|3[4-9][\d-9]000000|6[3-5][\d-9]000000|7[2-3][\d-9]000000|8[2-8][\d-9]000000|9[1-8][\d-9]000000|5[2-9][\d-9]0000000|3[4-9][\d-9]0000000|6[3-5][\d-9]0000000|7[2-3][\d-9]0000000|8[2-8][\d-9]0000000|9[1-8][\d-9]0000000|5[2-9][\d-9]00000000|3[4-9][\d-9]00000000|6[3-5][\d-9]00000000|7[2-3][\d-9]00000000|8[2-8][\d-9]00000000|9[1-8][\d-9]00000000|5[2-9][\d-9]000000000|3[4-9][\d-9]000000000|6[3-5][\d-9]000000000|7[2-3][\d-9]000000000|8[2-8][\d-9]000000000|9[1-8][\d-9]000000000|5[2-9][\d-9]0000000000|3[4-9][\d-9]0000000000|6[3-5][\d-9]0000000000|7[2-3][\d-9]0000000000|8[2-8][\d-9]0000000000|9[1-8][\d-9]0000000000|5[2-9][\d-9]00000000000|3[4-9][\d-9]00000000000|6[3-5][\d-9]00000000000|7[2-3
