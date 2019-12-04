import re

"""
* It is a six-digit number. 

* The value is within the range given in your puzzle
input. 

* Two adjacent digits are the same (like 22 in 122345). 

* Going from left to right, the digits never decrease; they only ever increase
  or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

* 111111 meets these criteria (double 11, never decreases). 

* 223450 does not meet these criteria (decreasing pair of digits 50). 123789
  does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet
these criteria?

246515-739105

not 547
"""

re_double = re.compile(r"^(.)\1{1,}$")

def check_double(value):
    """
    # checks the digits by converting to string, and then checking adjacent values

    # doctests
    >>> check_double(111111)
    True

    >>> check_double(123789)
    False

    >>> check_double(113456)
    True

    >>> check_double(123356)
    True

    >>> check_double(123451)
    False

    >>> check_double(121456)
    False
    """

    string = str(value)
    for i in range(len(string)-1):
        # print()
        if re_double.match(string[i] + string[i+1]):
            return True
    
    return False


def check_desc(value):
    """
    >>> check_desc(223450)
    False
    >>> check_desc(111111)
    True
    >>> check_desc(123789)
    True
    """
    string = str(value)
    for i in range(len(string)-1, 0, -1):
        if int(string[i]) < int(string[i-1]):
            return False
    
    return True


def has_only_double(value):
    """
    >>> has_only_double(112233)
    True

    >>> has_only_double(123444)
    False

    >>> has_only_double(111122)
    True

    >>> has_only_double(124444)
    False

    >>> has_only_double(113444)
    True
    """

    only_double = False
    string = str(value)
    prev_string = ''
    match_count = 0
    for i in range(len(string)):
        if string[i] == prev_string:
            match_count += 1
        else:
            if match_count == 1:
                return True
            match_count = 0

        if match_count == 1:
            only_double = True

        if match_count > 1:
            only_double = False

        prev_string = string[i]

    return only_double

if __name__ == "__main__":
    import doctest 
    print(doctest.testmod())
 

count_qualify = 0
for i in range(246515, 739105, 1):
    if (check_double(i) == True and check_desc(i) == True):
        count_qualify += 1
        print('.', end='')

print('\ncount qualify: {}'.format(count_qualify))

count_qualify = 0
print("\n")
for i in range(246515, 739105, 1):
    if (has_only_double(i) == True and check_desc(i) == True):
        count_qualify += 1
        print('.', end='')

print('\ncount qualify part 2: {}'.format(count_qualify))