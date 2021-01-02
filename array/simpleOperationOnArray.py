
def deepCopy() :
    print('Deep copy')
    # simple operation of list
    simList = [13, 1]
    print(simList)
    newSimList = simList.copy() # this make the array deep copied
    newSimList[0] = 0
    print(newSimList)
    print(simList)
    

def shallowCopy(): 
    print('Shallow copy')
    simList = [13, 1]
    print(simList)
    newSimList = simList
    newSimList[0] = 0
    print(newSimList)
    print(simList)


switcher = {
    'deep': deepCopy, 
    'shallow': shallowCopy
    }


# run shallow copy example
switcher['shallow']()

# run deep copy example
switcher['deep']()