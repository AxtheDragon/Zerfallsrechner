import nuclide_Data

print("Berechnen von Zerfallsketten")

print("---- input Mix ----")
printMix(nucMix.startMix)

print("---- new Mix ----")
nextMix = nucMix.iterateMix(nucMix.startMix)
printMix(nextMix)
