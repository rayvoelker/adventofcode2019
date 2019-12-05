# day 05
from array import array

def final_state(input_intcode, is_slice=False, parameter_mode=False):
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

    >>> final_state(array('l', [1002,4,3,4,33]), is_slice=False, parameter_mode=True)
    array('l', [1002, 4, 3, 4, 99])

    """
    # for i in range(0, len(input_intcode)-4, 4):
    i = 0
    # set the number of intcode to jump based ont he op_code
    jump = 0
    while i < (len(input_intcode) - jump):
        if parameter_mode:
            # position mode: 0
            # immediate mode: 1

            # Parameters that an instruction writes to will never be in
            # immediate mode. (so, op codes 3, 4?)
            string = str(input_intcode[i])
            op_code = int(string[-2:])
            mode_input_1 = int(string[-3:-2])
            mode_input_2 = int(string[-4:-3])
            # mode_input_3 = 0 # should be unused
        else:
            op_code = input_intcode[i]
            mode_input_1 = 0
            mode_input_2 = 0

        input_one = None
        input_two = None

        if op_code == 1:
            # add
            if mode_input_1 == 0: 
                input_one = input_intcode[input_intcode[i+1]]
            else:
                input_one = input_intcode[i+1]

            if mode_input_2 == 0:
                input_two = input_intcode[input_intcode[i+2]]
            else:
                input_two = input_intcode[i+2]

            input_intcode[input_intcode[i+3]] = input_one + input_two
            jump = 4
        elif op_code == 2:
            # multiply
            if mode_input_1 == 0:
                input_one = input_intcode[input_intcode[i+1]]
            else:
                input_one = input_intcode[i+1]

            if mode_input_2 == 0:
                input_two = input_intcode[input_intcode[i+2]]
            else:
                input_two = input_intcode[i+2]
            
            input_intcode[input_intcode[i+3]] = input_one * input_two
            jump = 4
        elif op_code == 3:
            # takes a single integer as input and saves it to the position given
            # by its only parameter
            input_intcode[input_intcode[i+1]] = input_intcode[i+1]
            jump = 2
        elif op_code == 4:
            input_one = input_intcode[input_intcode[i+1]]
            input_intcode[0] = input_one
            jump = 2
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

print( )

filename = 'day_05_input.txt'
intcode = array('l', [int(value) for value in open(filename).read().split(",")])

