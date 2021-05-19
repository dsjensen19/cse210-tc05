class parachute():
    """This class sotres an imamge of a man on a parachute
        changes that image as the game plays out.
        
        Atributes:
        Parachute_Askii = string[]

        """

        """Initilizes the parachute askii picture"""
        def __init__(self):
            parachute_askii = []
            parachute_askii.append(" ___")
            parachute_askii.append("/___\\")
            parachute_askii.append("\\   /")
            parachute_askii.append(" \\ /")
            parachute_askii.append("  0")
            parachute_askii.append(" /|\\")
            parachute_askii.append(" / \\")
            self.parachute_askii = parachute_askii

        """if there are more than three lines returns true"""
        def can_cut_layer(self):
            if len(self.parachute_askii) >= 3:
                return True
            else:
                return False:

        """removes the top layer of the parachute askii picture"""
        def cut_layer(self):
            self.parachute_askii.pop()
            if self.can_cut_layer():
                self.parachute_askii[0] = "  X"

        """prints out the parachute askii"""
        def display(self):
            for line in self.parachute_askii():
                print(line)
            print()
            print("^^^^^^^")