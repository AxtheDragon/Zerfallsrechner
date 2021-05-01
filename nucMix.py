import nucData

def printMix(mix):
    for key,value in mix.items():
        print(key, value)

def iterateMix(mix):
    newNuclides = { }
    for key in mix.keys():
        daughter = nucData.daughters[key]
        if nucData.daughters[key] in mix:
            print(daughter, "ist schon dabei")
        else:
            newNuclides[daughter] = 0
            print(daughter, "ist neu")
    mix.update(newNuclides)    
    return mix


startMix = {"U-235" : 100, "Cs-137" : 50, "Th-231" : 30}

