import nucData
import nucMix
from nucMix import printMix

print("Berechnen von Zerfallsketten")
print("---- input Mix ----")
printMix(nucMix.startMix)

print("---- new Mix ----")
nextMix = nucMix.iterateMix(nucMix.startMix)
printMix(nextMix)