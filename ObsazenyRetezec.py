print("JE PRVNÍ ŘETĚZEC OBSAŽEN V DRUHÉM?")
print("----------------------------------")

prvniString = input('Zadej první řetězec: ').strip()
druhyString = input('Zadej druhý řetězec: ').strip()

prvniLower = prvniString.lower()
druhyLower = druhyString.lower()

obsahuje = prvniLower in druhyLower

if obsahuje:
    print("Ano, {} obsahuje {}!".format(druhyString, prvniString))

else:
    print("Ne, {} neobsahuje {}!".format(druhyString, prvniString))