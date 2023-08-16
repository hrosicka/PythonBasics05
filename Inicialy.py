print("INICIÁLY")
print("--------")

jmeno = input('Zadej jméno: ').strip()
prijmeni = input('Zadej příjmení: ').strip()

jmenoPrvniVelke = jmeno[0].upper() + jmeno[1:]
prijmeniPrvniVelke = prijmeni[0].upper() + prijmeni[1:]
inicialy = jmeno[0].upper() + "." + prijmeni[0].upper() + "."

print("Iniciály pro {} {} jsou {}!".format(jmenoPrvniVelke, prijmeniPrvniVelke, inicialy))