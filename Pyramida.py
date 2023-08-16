print("PYRAMIDA HVĚZD")
print("------------- ")

while True:
    vstup = input("Zadej počet pater pyramidy: ")
    try:
        patro = int(vstup)
        break
    except ValueError:
            print("Zadaná hodnota není číslo! Zkus to znovu", end = "!!\n") 

# vykreslí pyramidu
for x in range (0, patro + 1):
    print ((patro - x) * ' ' + x * "* ")