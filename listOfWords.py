sentence = 'i am a very goood lad i know that. that  is why i love indomie'
splitWord = sentence.split(' ')
print (splitWord)

countDict = {}
for word in splitWord:
    if word in countDict:
        countDict[word]+=1
    else:
        countDict[word] = 1
print(countDict)