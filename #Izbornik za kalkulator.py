#Izbornik za kalkulator
print("             ")
print("Izbornik za kalkulator")
print("       ")
print("1.izračunaj napon struje")
print("2. Izračunaj otpor struje")
print("3. Izračunaj jakosti struje")
print("4. Zbroj serijskih otpora")
print("5.zbroj paralelnih otpora")
print("    ")
opcija = int(input("Izaberite operaciju (1/2/3):"))
#struktura grananja
if opcija == 1:
    print("Izračun napona struje")
    jakost = int(input("Upiši jakost struje:  "))
    otpor = int(input("Upiši otpor:   "))
    napon = jakost*otpor
    print(f"Napon struje je:  {napon} V")
elif opcija == 2:
    print("Izračun otpora struje")
    napon = int(input("Upiši napon:  "))
    jakost = int(input("Upiši jakost struje: "))
    otpor = napon/jakost
    print(f"Otpor je {otpor} ohm")
elif opcija== 3:
    print("Izračunaj jakosti struje")
    napon = int(input("Upiši napon:  "))
    otpor = int(input("Upiši otpor:  "))
    jakost = napon/otpor
    print(f"Jakost struje je: {jakost} A")
elif opcija == 4:
    print("Izračun serijskog otpora")
    otpor1 = int(input("Upiši otpor1:  "))
    otpor2 = int(input("Upiši otpor2:  "))
    otpor = otpor1+otpor2
    print(f"otpor otpornika je: {otpor} ohm")
elif opcija == 5:
    

else:
    print("Pogrešan unos")
