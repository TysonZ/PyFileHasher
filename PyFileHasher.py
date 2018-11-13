import hashlib

def getVars():
	try:
		print ("Name of the file to use?")
		fileLoc = input("> ")
		file = open(fileLoc)
		lines = file.readlines()
		file.close()
		return lines
	except FileNotFoundError as fnf_error:
		print ("ERROR: File not found!")
		exit()

def md5Hasher(lines):
    results = []
    for x in lines:
        if x.rstrip() != "": 
            xenc = x.rstrip().encode('utf-8')
            hx = hashlib.md5(xenc).hexdigest()
            results.append(x.rstrip() + ":" + hx)
    return results
	
def sha1Hasher(lines):
    results = []
    for x in lines:
        if x.rstrip() != "": 
            xenc = x.rstrip().encode('utf-8')
            hx = hashlib.sha1(xenc).hexdigest()
            results.append(x.rstrip() + ":" + hx)
    return results

def writeArray(results):
	resulstFileName = "results.txt"
	try:
		with open (resulstFileName,'w') as f:
			for result in results:
				f.write(result + "\n")
		print ("Completed successfully")
	except:
		print("ERROR: Error writing to file " + resulstFileName)

def selHash(hashList):
	
	print ("Select which hash function to use. (/list for more)")
	try:
	
		#Asking for user Input
		while True:
			hashInput = input("> ").lower()
			#If selected hash algorithm, break the loop (and return the algorithm to use)
			if hashInput in hashList:
				break
			#If the input is asking for help, return the list of supported hash algorithms. 
			elif hashInput in ["/list", "?", "/help", "list", "help"]:
				print ("Supported hash algorithms are:" + str(hashList))
			elif hashInput == "exit":
				exit()
			else:
				print ("Unsupported hash algorithm")
		#We only get here if the input is a valid hash
		return hashInput
	
	except Exception as e:
		print (e)
		exit

		
#Start
hashList = ["md5", "sha1"]
selHashList = selHash(hashList)
lines = getVars()
if selHashList == "md5":
	results = md5Hasher(lines)
elif selHashList == "sha1":
	results = sha1Hasher(lines)

writeArray(results)


