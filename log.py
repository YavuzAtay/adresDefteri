def Kisiler(k1,telNo,yas):
    gelenKisi= "kisi ismi {0}, kisi telefon numarasi {1}, kisi yas {2}".format(k1,telNo,yas)
    file=open("AdresDefteri/LogKayit/isimler.txt","a")
    file.write("\n")
    file.write(gelenKisi)
    file.close()
def kisiAdres(k1,*adres):
    gelenAdres="kisi {0} ,adresleri {1},".format(k1,*adres)
    file=open("AdresDefteri/LogKayit/Adresler.txt","a")
    file.write("\n")
    file.write(gelenAdres)
    file.close()



