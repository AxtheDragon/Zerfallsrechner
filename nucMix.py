import nucData

def printMix(mix):
    for key,value in mix.items():
        print(key, value)

def iterateMix(mix):
    newNuclides = { }
    for key in mix.keys():
        daughter = nucData.daughters[key]
        if daughter in mix:
            print(daughter, "ist schon dabei")
        else:
            newNuclides[daughter] = 0
            print(daughter, "ist neu")
    mix.update(newNuclides)    
    return mix


startMix = {nucData.U235 : 100, nucData.Cs137 : 50, nucData.Th231 : 30}

