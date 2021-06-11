from nucClass import nuclide


H3 = nuclide("H-3", 12.3)
Cs137 = nuclide("Cs-137", 30.17)
U235 = nuclide("U-235", 7.038*10**8)
Ba133 = nuclide("Ba-133", 1/365)
Li3 = nuclide("Li-3", 0)
Th231 = nuclide("Th-231", 1)

#nuclides of the uranium-radium-chain
U238 = nuclide("U-238", 4468000000)
Th234 = nuclide("Th-234", 0.066)
Pa234m = nuclide("Pa-234m", 0.00000226) #hier habe ich den langsameren Zweig über Pa234 weggelassen, weil er nur einen Anteil von 0,16% hat
U234 = nuclide("U-234", 244500)
Th230 = nuclide("Th230", 75400)
Ra226 = nuclide("Ra-226", 1600)
Rn222 = nuclide("Rn-222", 0.0104)
Po218 = nuclide("Po-218", 0.0000058) #Ast über At218 weggelassen 0,1%
Pb214 = nuclide("Pb-214", 0.00005098)
Bi214 = nuclide("Bi-214", 0.0000378) #Ast über Tl210 weggelassen 0,02%
Po214 = nuclide("Po-214", 0.0000000000052)
Pb210 = nuclide("Pb-210", 22.3)
Bi210 = nuclide("Bi-210", 0.0137)
Po210 = nuclide("Po-210", 0.379)
Pb206 = nuclide("Pb-206", 0)

u238chain = {U238:Th234, Th234:Pa234m, Pa234m:U234, U234:Th230, Th230:Ra226, Ra226:Rn222, Rn222:Po218, Po218:Pb214, Pb214:Bi214, Bi214:Po214, Po214:Pb210, Pb210:Bi210, Bi210:Po210, Po210:Pb206}

#hwz = {"H-3": 12.3, "Cs-137": 30.17} #Ich glaube dieser Fix hat sich als unnütz herausgestellt
daughters = {Cs137 : Ba133, H3 : Li3, U235 : Th231, Th231 : H3} #Test-Zerfallsbeziehungen
daughters.update(u238chain) #Die Uran-Radium-Zerfallsreihe wird an das Test-Dictionary angehängt