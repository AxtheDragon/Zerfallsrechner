from nucClass import nuclide

H3 = nuclide("H-3", 12.3)
Cs137 = nuclide("Cs-137", 30.17)
U235 = nuclide("U-235", 7.038*10**8)
Ba133 = nuclide("Ba-133", 1/365)
Li3 = nuclide("Li-3", 0)

daughters = {Cs137 : Ba133, H3 : Li3}