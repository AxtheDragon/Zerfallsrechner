import nucData
import nucMix
from nucMix import printMix

print("Berechnen von Zerfallsketten")
print("---- input Mix ----")
printMix(nucMix.UranMix)

thisMix = nucMix.UranMix
for i in range(0,9):
    print("---- new Mix", i, " ----")
    nextMix = nucMix.iterateMix(nucMix.UranMix)
    printMix(nextMix)
    thisMix = nextMix