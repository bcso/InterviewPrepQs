# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = raw_input().split()
farmArray = []
ver = int(a)
hor = int(b)

for yVal in xrange(ver):
    farmArray.append(list(raw_input()))

    
def checkBounds(farmArray):
    for y in xrange(len(farmArray)):
        if (y == 0) or (y == len(farmArray)-1):
            for item in farmArray[y]:
                if item == 'x':
                    print "impossible"
                    return 0
        else:
            count = 0
            for item in farmArray[y]:
                if ((count == 0) or (count == len(farmArray[y]))) and (item =='x'):
                    print "impossible"
                    return 0
                count += 1
    print 2*hor + 2*(ver-2)
    return 0
                    
            
                
checkBounds(farmArray)

        