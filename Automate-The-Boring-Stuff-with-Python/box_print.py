"""
******
*    *
*    *
******
"""


def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('"symbol" need to be a string of length 1')
    if width < 2 or  height < 2:
        raise Exception('"width" and "height" must be greater than or equal to 2')

    
    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol) 

    print(symbol * width)


boxPrint('*', 15, 1)

boxPrint('**', 15, 5)
