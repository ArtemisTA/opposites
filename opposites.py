import random


#wordbank = {
 #   "hot" : "cold"
  #  "wet" : "dry"
   # "summer" : "winter"
    #"black" : "white"
    #"night" : "day"
    #"wise" : "naive"
    #"strong" : "weak"
    #"fast" : "slow"
    #"love" : "hate"
    #"sow" : "reap"
    #"cold" : "hot"
    #"frugal" : "impulsive"
    #"clever" : "stupid"
    #}
word = str()
wordbank = {}
boop = open("opposites.txt")
opposites = boop.read()
print(opposites)
lastword = str()
wordlist = []
for i in range (0,len(opposites)):
    if opposites[i] == " " or opposites[i] == "\n":
        if lastword == str():
            wordbank[word] = str()
            lastword = word
            wordlist.append(word)
        else:
            wordbank[lastword] = word
            lastword = str()
        word = str()
    else:
        word = word + opposites[i]
print(wordbank)
print(wordlist)

pickedbefore = []
for i in range(0,5):
    fli = True
    while fli == True:
        firstword = random.randint(0,12)
        if not wordlist[firstword] in pickedbefore:
            firstword = wordlist[firstword]
            pickedbefore.append(firstword)
            fli = False
    fli2 = True
    while fli2 == True:
        secondword = random.randint(0,12)
        if not wordlist[secondword] in pickedbefore:
            secondword = wordlist[secondword]
            pickedbefore.append(secondword)
            fli2 = False
    print( firstword + " is to " + wordbank[firstword] + " as " + secondword + " is to...")
    fli3 = True
    while fli3 == True:
        shazam = input()
        if shazam != wordbank[secondword]:
            print("WRONG")
        else:
            fli3 = False
print(pickedbefore)
            
        
    
