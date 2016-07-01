
def square_colour(hour, min):
    colour_dict = {
        0 : ['0', '0', '0', '0', '0'],
        1 : ['0', '0', '0', '0', '1'],
        2 : ['0', '0', '0', '1', '1'],
        3 : ['0', '0', '1', '1', '0'],
        4 : ['0', '0', '1', '1', '1'],
        5 : ['0', '1', '1', '0', '0'],
        6 : ['0', '1', '1', '1', '0'],
        7 : ['0', '1', '1', '1', '1'],
        8 : ['1', '1', '0', '0', '0'],
        9 : ['1', '1', '0', '1', '0'],
        10 : ['1', '1', '1', '0', '0'],
        11 : ['1', '1', '1', '1', '0'],
        12 : ['1', '1', '1', '1', '1']
        }
    return (list(colour_dict[hour]), list(colour_dict[min]))

def and_gate(hr_colour, min_colour):
    if (hr_colour == '0') and (min_colour == '0'):
        return white  # OFF
    elif (hr_colour == '0') and (min_colour == '1'):
        return blue   # MINS only
    elif (hr_colour == '1') and (min_colour == '0'):
        return red    # HRS only
    else:
        return green  # HRS + MINS


def main():



    hour = int(input("enter HOUR number between 1 & 12: "))
    print(hour)
    min = int(input("enter MINS number between 1 & 12: "))
    print(min)

    hr_colour, min_colour = square_colour(hour, min)
    print(hr_colour, min_colour)

# TODO: need a loop through fib_series = [1,1,2,3,5]

    light_col = and_gate(hr_colour, min_colour)
    print(light_col)


if __name__ == '__main__':
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0, 125)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    main()


'''
print(colour_dict)
print(list(colour_dict))
print(list(colour_dict.keys()))
print(list(colour_dict.values()))
print(list(colour_dict[11]))

print(list(colour_dict.keys())[list(colour_dict.values()).index(['1', '1', '1', '1', '1'])])
#print(list(colour_dict.keys().index[12])[list(colour_dict.values())]) # stupid - just use list(colour_dict[11])
'''