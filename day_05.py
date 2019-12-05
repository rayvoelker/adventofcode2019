# day 05
from array import array

def final_state(input_intcode, is_slice=False):
    """
    # doctests
    >>> final_state(array('l', [1,9,10,3,2,3,11,0,99,30,40,50]))
    array('l', [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

    >>> final_state(array('l', [2,3,0,3,99]))
    array('l', [2, 3, 0, 6, 99])

    >>> final_state(array('l', [2,4,4,5,99,0]))
    array('l', [2, 4, 4, 5, 99, 9801])

    >>> final_state(array('l', [1,1,1,4,99,5,6,0,99]))
    array('l', [30, 1, 1, 4, 2, 5, 6, 0, 99])

    """
    # for i in range(0, len(input_intcode)-4, 4):
    i = 0
    jump = 4
    while i < (len(input_intcode) - jump):
        op_code = input_intcode[i]
        input_one = input_intcode[input_intcode[i+1]]
        input_two = input_intcode[input_intcode[i+2]]

        if op_code == 1:
            # add
            input_intcode[input_intcode[i+3]] = input_one + input_two
        elif op_code == 2:
            # multiply
            input_intcode[input_intcode[i+3]] = input_one * input_two
        elif op_code == 99:
            # end
            break
        else:
            break

        i += jump

    if is_slice:
        return input_intcode[0]
    else:
        return input_intcode

# run the tests
if __name__ == "__main__":
    import doctest 
    print(doctest.testmod())


filename = 'day_02_input.txt'

intcode = array('l', [int(value) for value in open(filename).read().split(",")])

"""
before running the program, replace position 1 with the value 12 and replace
position 2 with the value 2. What value is left at position 0 after the program
halts?
"""
intcode[1] = 12
intcode[2] = 2

# send a slice to keep the data intact
print(final_state(intcode[:], is_slice=True))

for noun in range(0, 100):
    for verb in range(0, 100):
        intcode[1] = noun
        intcode[2] = verb

        if final_state(intcode[:], is_slice=True) == 19690720:
            print("noun, verb: 100 * {} + {} = {}".format(noun, verb, (100*noun+verb)))

            break