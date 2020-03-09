yesil = "\033[42m"
normal = "\033[0m"
kirmizi = "\033[41m"
sari = "\033[43m"
dkirmizi = "\033[31m"

###

print("\033[7m"+"Beden Kitle Endeksi"+normal)
boy = float (input ("Boyunuzu giriniz (cm): " ))
kilo = float (input ("kilonuzu giriniz: " ))
boy = boy / 100.00
bki = kilo/(boy*boy)

print ("BKİ : " ,bki)


if bki <= 18.5:
    
    lbki = 18.5
    hbki = 25

    ##
    minog = lbki*(boy*boy)
    minog = round (minog,3)
    minal = minog - kilo
    minal = round(minal,3)
    
    manog = hbki*(boy*boy)
    manog = round(manog,3)
    manal = kilo - manog
    ##
    print (kirmizi+"ÇOK ZAYIF"+normal)
    print ("Minimum olması gereken ideal kilonuz:", minog,", ideal minimum kilonuza gelmek için almanız gereken kilo:", minal)
    print ("Maksimum olması gereken ideal kilonuz:", manog, ", ideal maksimum kilonuza gelmek için gereken kilo:", manal)
    if boy <=1.40:
        print("çocuklar için BKİ formülü farklıdır.")
        
elif bki <=25:
    
    print(yesil+"NORMAL KİLOLU"+normal)

elif bki <=30:
    
    lbki = 25
    hbki = 18.5
    
    ##
    minog = lbki*(boy*boy)
    minog = round (minog,3)
    minal = minog - kilo
    minal = round(minal,3)
    
    manog = hbki*(boy*boy)
    manog = round(manog,3)
    manal = kilo - manog
    ##
    print(sari+"FAZLA KİLOLU"+normal)
    
    print ("Minimum olması gereken ideal kilonuz:", minog,", ideal minimum kilonuza gelmek için vermeniz gereken kilo:", minal)
    print ("Maksimum düşmeniz gereken ideal kilonuz:", manog, ", ideal en düşük kilonuza gelmek için gereken kilo:", manal)
    
elif bki <=35:
    
    lbki = 25
    hbki = 18.5
    
    ##
    minog = lbki*(boy*boy)
    minog = round (minog,3)
    minal = minog - kilo
    minal = round(minal,3)
    
    manog = hbki*(boy*boy)
    manog = round(manog,3)
    manal = kilo - manog
    ##
    
    print(kirmizi+"I. DERECE OBEZ"+normal)
    
    print ("Minimum olması gereken ideal kilonuz:", minog,", ideal minimum kilonuza gelmek için vermeniz gereken kilo:", minal)
    print ("Maksimum düşmeniz gereken ideal kilonuz:", manog, ", ideal en düşük kilonuza gelmek için gereken kilo:", manal)
    
elif bki <=40:
    
    lbki = 25
    hbki = 18.5
    
    ##
    minog = lbki*(boy*boy)
    minog = round (minog,3)
    minal = minog - kilo
    minal = round(minal,3)
    
    manog = hbki*(boy*boy)
    manog = round(manog,3)
    manal = kilo - manog
    ##
    
    print(kirmizi+"II. DERECE OBEZ"+normal)
    
    print ("Minimum olması gereken ideal kilonuz:", minog,", ideal minimum kilonuza gelmek için vermeniz gereken kilo:", minal)
    print ("Maksimum düşmeniz gereken ideal kilonuz:", manog, ", ideal en düşük kilonuza gelmek için gereken kilo:", manal)
    
else:
    
    
    lbki = 25
    hbki = 18.5
    
    ##
    minog = lbki*(boy*boy)
    minog = round (minog,3)
    minal = minog - kilo
    minal = round(minal,3)
    
    manog = hbki*(boy*boy)
    manog = round(manog,3)
    manal = kilo - manog
    ##
    
    print(dkirmizi+"Kardeşim Dünya'yı mı yedin?"+normal)
    
    print ("Minimum olması gereken ideal kilonuz:", minog,", ideal minimum kilonuza gelmek için vermeniz gereken kilo:", minal)
    print ("Maksimum düşmeniz gereken ideal kilonuz:", manog, ", ideal en düşük kilonuza gelmek için gereken kilo:", manal)
    
    ### ödev bir kilo alma/verme hedefi oluşturmak