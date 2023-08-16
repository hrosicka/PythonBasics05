print("MĚNIČ PÍSMEN")
print("------------")

slovo = input('Slovo: ')

while True:
            pozStr = input('Které písmeno zaměnit (počítá se od jedničky)? ')
            try:
                pozice = int(pozStr) - 1
                break
            except ValueError:
                print("Zadaná hodnota není číslo! Zkus to znovu", end = "!!\n") 

novyZnak = input('Nové písmeno (nebo skupina písmen): ')

noveSlovo = slovo[:pozice] + novyZnak + slovo[(pozice + 1):]

print("Slovo {} se změnilo na slovo {}.".format(slovo.upper(), noveSlovo.upper()))
