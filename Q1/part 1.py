def edgeLengthValidation(len):
    if len <= 0 :
        return False
    return True

def makePrintLine(num, len):
    space = " "
    star = "*"
    if num == 0:
        return (space * (len-1)) + star 
    elif num == len-1:
        return star * (2*len - 1)
    return (space * (len-num-1)) + (star) + ((2*num -1) * space) + (star)

def printTriangle(len):
    for i in range (len):
        line = makePrintLine(i, len)
        print (line)

if __name__ == "__main__":
    edge = int( input("Enter length of the edge:") )
    while not edgeLengthValidation(edge):
        edge = int( input("**Length is not valid** \nEnter length of the edge:") )
    printTriangle(edge)