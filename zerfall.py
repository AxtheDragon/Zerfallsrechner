import nuclide_Data

print("Berechnen von Zerfallsketten")
print(nuclide_Data.H3.name)
print(nuclide_Data.H3.hwz_years())
print()
print(nuclide_Data.U235.name)
print(nuclide_Data.U235.hwz_years())
print(nuclide_Data.daughters[nuclide_Data.Cs137].name)