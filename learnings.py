def enumerateLearn():
    print("Enumerate adds a counter to an iterable and returns it")
    languages = ['Python', 'Java', 'JavaScript']
    enumeratedLanguages = enumerate(languages)
    print(list(enumeratedLanguages))
    #Specify list in print because otherwise it just showcases enumerated object location

    #Enumerate syntax is such that enumerate(iterable, start), start default is 0 and optional

def setLearn():
    print("Sets are unordered, unchangeable*, and unindexed")
    myset = {"apple", "banana", "cherry"}
    #Sets cannot contain duplicate values

enumerateLearn()
