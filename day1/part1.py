number_dictionary = {'one' : '1','two': '2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
reversed_number_dictionary = {'eno' : '1','owt': '2','eerht':'3','ruof':'4','evif':'5','xis':'6','neves':'7','thgie':'8','enin':'9'}

def main1():
    input = inputAsList()
    sum = 0
    for line in input:
        # Get all integers in the string and put them in a list.
        integer_list = ''.join(x for x in line if x.isdigit())

        # Add the concatenated value of the first and last integer to the sum.
        sum += int(integer_list[0] + integer_list[len(integer_list)-1])
    return sum

def main2():
    input = inputAsList()
    sum = 0
    for line in input:

        # Get the first and last number from the list.
        first = getFirstNumber(line)
        last = getLastNumber(line)

        # Finally, the values are concatenated and summed.
        sum += int(''.join([first,last]))
    return sum

# Retrieves the first number of a given string, which can either be a literal, or fully spelled out number.
# The dictionary provides the mapping of the numbers written as strings, mapped onto their literal value.
def getFirstNumber(string, number_dict=number_dictionary):
    while(len(string) != 0):
        # If the string starts with a digit, that digit is returned.
        if(string[0].isdigit()):
            return string[0]

        # If the string starts with a number written out, the corresponding value is returned.
        else:
            for key,value in number_dict.items():
                if string.startswith(key):
                    return value

        # Repeat by removing the first character until a value is found.
        string = string[1:]
    return None

# Retrieves the last number from a list, which could be a literal digit or fully spelled out number.
def getLastNumber(line):
    # getFirstNumber is called, but both the line and dictionary are reversed, resulting in the last number of the line.
    return getFirstNumber(line[::-1], reversed_number_dictionary)


def inputAsList():
    f = open('input')
    return list(f.read().split('\n'))


print(main1())
print(main2())
