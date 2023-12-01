nums = {'one' : '1','two': '2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
reversed = {'eno' : '1','owt': '2','eerht':'3','ruof':'4','evif':'5','xis':'6','neves':'7','thgie':'8','enin':'9'}

def main1():
    lst = inputAsList()
    sum = 0
    for str in lst:
        ints = ''.join(x for x in str if x.isdigit())
        sum += int(ints[0] + ints[len(ints)-1])
    return sum

def main2():
    lst = inputAsList()
    sum = 0
    for str in lst:
        first = getFirstNumber(str,nums)
        last = getFirstNumber(str[::-1],reversed)
        sum += int(''.join([first,last]))
    return sum

def getFirstNumber(string, number_dictionary):
    first = 0
    while(first == 0 and len(string) != 0):
        if(string[0].isdigit()):
            first = string[0]
        else:
            for key,value in number_dictionary.items():
                if string.startswith(key):
                    first = value
                    break
            string = string[1:]
    return first



def inputAsList():
    f = open('input')
    return list(f.read().split('\n'))


print(main1())
print(main2())
