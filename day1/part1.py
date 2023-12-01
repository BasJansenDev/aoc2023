number_dictionary = {'one' : '1','two': '2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def main1():
    input = input_as_list()
    sum = 0
    for line in input:
        # Get all integers in the string and put them in a list.
        integer_list = ''.join(x for x in line if x.isdigit())

        # Add the concatenated value of the first and last integer to the sum.
        sum += int(integer_list[0] + integer_list[len(integer_list)-1])
    return sum

def main2():
    input = input_as_list()
    sum = 0
    for line in input:

        # Get all the numbers from the list.
        numbers = get_numbers(line)

        # Add the concatenated first and last numbers to the sum
        sum += int(''.join([numbers[0],numbers[-1]]))
    return sum

# Retrieves the first number of a given string, which can either be a literal, or fully spelled out number.
# The dictionary provides the mapping of the numbers written as strings, mapped onto their literal value.
def get_numbers(string):
    number_list = []
    while(len(string) != 0):
        # If the string starts with a digit, that digit is added to the number list.
        if(string[0].isdigit()):
            number_list += string[0]

        # If the string starts with a number written out, the corresponding value is added to the number list.
        else:
            for key,value in number_dictionary.items():
                if string.startswith(key):
                    number_list += value
                    break

        # Repeat by removing the first character until a value is found.
        string = string[1:]
    return number_list


def input_as_list():
    f = open('input')
    return list(f.read().split('\n'))


print(main1())
print(main2())
