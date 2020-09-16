import log as logMod
try:
    end = 0
    while(end < 1):
        kisi1=input("Kişinin ismini giriniz -->  ")
        telefonNo=int(input(kisi1+" kisisine telefon numarasını giriniz :  "))
        yas=int(input(kisi1+" kisisine yaşini giriniz :  "))
        adrsBitis=0
        kisiadres1=input(kisi1+" kisisine  adres giriniz :  ")
        logMod.kisiAdres(kisi1,kisiadres1)
        while(adrsBitis < 1):
            istek=input("daha fazla adres girmek istermisiniz evet ise (e) hayır ise (h)")
            if istek == "e":
                moreAdres=input(kisi1+" kisisine  adres giriniz :  ")
                logMod.kisiAdres(kisi1,moreAdres)
            elif istek == "h":
                adrsBitis = 2
        logMod.Kisiler(k1=kisi1,telNo=telefonNo,yas=yas)
        dgr=input("Bitirmek istiyormusun evet ise (e) hayır ise (h)")
        if dgr == "e":
            break
        elif dgr == "h":
            continue
except ValueError:
    d=print("yaş kısmına ve telefon numarası kısmına sadece sayı giriniz.")
    logMod.HataLog(kisi1,ValueError)
   




    
