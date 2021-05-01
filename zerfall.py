import nucData
import nucMix
from nucMix import printMix

print("---- input Mix ----")
printMix(nucMix.startMix)

print("---- new Mix ----")
nextMix = nucMix.iterateMix(nucMix.startMix)
printMix(nextMix)
