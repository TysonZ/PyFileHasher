import hashlib

def getVars():
    fileLoc = input("File Name: ")
    file = open(fileLoc)
    lines = file.readlines()
    file.close()
    return lines

def hasher(lines):
    results = []
    for x in lines:
        if x.rstrip() != "": 
            xenc = x.rstrip().encode('utf-8')
            hx = hashlib.md5(xenc).hexdigest()
            results.append(x.rstrip() + ":" + hx)

    return results

def writeArray(results):
    with open ('results.txt','w') as f:
        for result in results:
            f.write(result + "\n")


#Start
print ("Program Start")
lines = getVars()
results = hasher(lines)
writeArray(results)
print ("Program End")


