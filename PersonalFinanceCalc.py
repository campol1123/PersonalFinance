grossIncome = 0
natIns = 0
netIncome = 0
taxedsf = 0

#user enters gross annual income
grossIncome = int(input("enter gross income: £"))

totalIncome = grossIncome
taxedsf = grossIncome
home = ((grossIncome*0.26)*25)
rent = (grossIncome/12)*(33333/100000)

#calulates income tax
for x in range(totalIncome):
    if taxedsf < 12501:
        grossIncome -= 1
        netIncome += 1
        taxedsf -= 1
    else:
        if taxedsf < 50001:
            grossIncome -= 1
            netIncome += 0.8
            taxedsf -= 1
        else:
            if taxedsf < 150000:
                grossIncome -= 1
                netIncome += 0.6
                taxedsf -= 1
            else:
                if taxedsf > 150000:
                    grossIncome -= 1
                    netIncome += 0.55
                    taxedsf -= 1
                    
#calculates national insurance
taxedsf = totalIncome
for x in range(totalIncome):
    if taxedsf < 9500:
        grossIncome -= 1
        taxedsf -= 1
    else:
        if 9500 < taxedsf < 50000:
            grossIncome -= 1
            natIns += 0.12
            taxedsf -= 1
        else:
            if taxedsf > 50000:
                grossIncome -= 1
                natIns += 0.02
                taxedsf -= 1


netIncome = netIncome-natIns


#prints info

print("net income is: £" + str(round(netIncome, 2)))
cp = netIncome*0.6
print("max car price is: £" + str(round(cp, 2)))
print("max rent price is: £ " + str(round(rent, 2)))
print("max home price is: £ " + str(round(home, 2)))
