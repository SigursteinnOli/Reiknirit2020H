import re
marglida = "-x2+2"
formerki = []

for x in marglida:
    if x == "-" or x == "+":
        formerki.append(x)

lidir = re.split("[-+]", marglida)
if lidir[0] == "":
    lidir.remove("")

def formulaVeldi(tala,listi):
    tala = round((tala**(float(listi[1])+1)) /(float(listi[1])+1), 2)
    return tala

def heildun(mork, telj = 0):
    telj+=1
    result = []
    for x in lidir:
        summa = mork
        lidur = re.split("[x]",x)
        while True:
            if len(lidur) >1:
                #Checkar hvort liðurinn sé X
                if lidur[0]=="" and lidur[1]=="":
                    summa = (summa**2)/2
                    result.append(summa)
                    break
                else:
                    #Reiknar veldið...
                    if lidur[1] != "" and lidur[1]:
                        summa = formulaVeldi(summa,lidur)
                        if lidur[0] != "":
                            summa = summa * float(lidur[0])
                            result.append(summa)
                            break
                    #Ef það er ekkert veldi
                    if lidur[0]!="":
                        summa = ((summa**2)/2)*float(lidur[0])
                        result.append(summa)
                        break
                    else:
                        result.append(summa)
                        break

            #ef lidurinn hefur ekkert veldi né margfeldi
            else:
                summa = summa * float(x)
                result.append(summa)
                break
    return result           







print("jafnan ",marglida)
em = int(input("Sláðu inn efrimörk: "))
nm = int(input("Sláðu inn neðrimörk: "))
emH = heildun(em)
nmH = heildun(nm)



formerki2 = []

for x in formerki:

    if x == "-":
        formerki2.append(-1)
    else:
        formerki2.append(1)
        


if len(emH)>1:
    breyta1 = (float(emH[0])*formerki2[0]) + (float(emH[1])*formerki2[1])
    breyta2 = (float(nmH[0])*formerki2[0]) + (float(nmH[1])*formerki2[1])
else:
    breyta1 = float(emH[0])
    breyta2 = float(nmH[0])
flatarmal = breyta1 - breyta2
print("Flatarmál: ", flatarmal)


