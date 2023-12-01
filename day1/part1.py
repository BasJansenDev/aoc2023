number_dictionary = {'one' : '1','two': '2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def main(part2):
    input = input_as_list()
    sum = 0
    for line in input:
        number_list = []
        while(len(line) != 0):
            # If the line currently starts with a digit, that digit is added to the number list.
            if(line[0].isdigit()):
                number_list += line[0]

            # Only for part two:
            # If the line currently starts with a number written out, the corresponding value is added to the number list.
            elif(part2):
                for key,value in number_dictionary.items():
                    if line.startswith(key):
                        number_list += value
                        break

            # Repeat by removing the first character until no characters are left.
            line = line[1:]

        # Finally, the first and last number from the current line are concatenated and added to the total sum.
        sum += int(''.join([number_list[0],number_list[-1]]))
    return sum

def input_as_list():
    f = open('input')
    return list(f.read().split('\n'))

print(main(False))
print(main(True))
