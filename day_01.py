import math

filename = 'day_01_input.txt'
input = open(filename).read().split("\n")

# for value in input:
#     print(value, end=", ")

"""
For example:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

    A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2
    divided by 3 and rounded down is 0, which would call for a negative fuel),
    so the total fuel required is still just 2.

    At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires
    216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires
    21 fuel, which requires 5 fuel, which requires no further fuel. So, the
    total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 =
    966.

    The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192
    + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
"""

def calc_mass(input):
    """
    # doctests:
    >>> calc_mass(12)
    2
    >>> calc_mass(14)
    2
    >>> calc_mass(1969)
    654
    >>> calc_mass(100756)
    33583

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

    """
    result = (input // 3) - 2
    if (result <= 0):
        return 0
    else:
        return result


def calc_fuel_mass(input):
    """
    At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires
    216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires
    21 fuel, which requires 5 fuel, which requires no further fuel. So, the
    total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 =
    966.

    >>> calc_fuel_mass(654)
    312
    """
    sum_fuel_masses = 0
    current_fuel = calc_mass(input)
    sum_fuel_masses += current_fuel

    while (calc_mass(current_fuel) != 0):
        current_fuel = calc_mass(current_fuel)
        sum_fuel_masses += current_fuel

    return sum_fuel_masses


if __name__ == "__main__":
    import doctest 
    print(doctest.testmod())

# part one
running_sum = 0

for value in input:
    result = calc_mass(int(value))
    running_sum += result

print('fuel required for mass of all modules: {}'.format(running_sum))


# part two
running_sum = 0
for value in input:
    value = int(value)
    result_module = calc_mass(value)
    result_fuel = calc_fuel_mass(result_module)

    running_sum += (result_module + result_fuel)

print('final values with fuel masses: {}'.format(running_sum))