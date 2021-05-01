class nuclide:
    
    #attribute
    def __init__(self, name, hwz):
        self.name = name
        self.hwz = hwz #Die HWZ soll in Jahren gespeichert werden

    def __str__(self):
        return self.name

    def __eq__(self,other):
        if self.name == other.name:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.name))

    #Methoden zur ausgabe der HWZ in verschiedenen Formaten
    def hwz_days(self):
        return self.hwz*365

    def hwz_years(self):
        return self.hwz


