print("MOCNINATOR")
print("----------")

vypis = "{i} na druhou je {naDruhou}"

for i in range(20):
    naDruhou = pow(i,2)
    print(vypis.format(i=i, naDruhou=naDruhou))