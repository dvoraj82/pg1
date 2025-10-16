#def my_range(start, stop, step=1):
#    result = []
#    zatim = start
#
#    while zatim < stop:
#        cisla.append(zatim)
#        zatim += step
#    return result

def while_enumerate(iterable, start=0):
    result = []
    index = 0
    while len(iterable) >  index:
        result.append( (start + index, iterable[index]) )
        index += 1

    return result


def for_enumerate(iterable, start=0):
    result = []
    index = start
    for x in iterable:
        result.append( (index,x))
        index += 1
        
    return result



if __name__ == "__main__":

    #print(list(range(1,5,)))
    #print(list(range(1,5,2)))

    text = "abcdef"
    print(list(enumerate(text, 10)))
    print(while_enumerate(text, 10))
    print(for_enumerate(text, 10))  

    #print(list(range(1,10,2)))
    #print(my_range(2,11,2))