import nucData
import nucMix
from nucMix import printMix

print("Berechnen von Zerfallsketten")
print(nucData.H3.name)
print(nucData.H3.hwz_years())
print(nucData.U235)
print(nucData.U235.hwz_years())
print(nucData.daughters[nucData.Cs137].name)

printMix(nucMix.startMix)