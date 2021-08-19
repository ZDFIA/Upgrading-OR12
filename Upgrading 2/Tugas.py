#Fungsi
def fungsi() :
    print("Hai")
    for i in range(10) :
        print(i)

fungsi()


#Return
def penjumlahan(angka1, angka2) :
    hasil_in = angka1 + angka2
    print("Hasil dalam fungsi : {}".format(hasil_in))
    return hasil_in

hasil_out = penjumlahan(17, 5)
print("Hasil return fungsi : {}".format(hasil_out))


#Arguments
def arguments(nama) :
    print(nama + " Andanny")

arguments("Fadly Ihsan")


#Pass by Reference
def ubah(list) :
    list.append([0, 1, 2, 5, 7])
    print('Nilai dalam fungsi: {}'.format(list))

list = [17, 20]
ubah(list)
print('Nilai luar fungsi: {}'.format(list))


#Arbitary
def Arbitary(*angka) :
    print("Angka paling kanan adalah " + angka[4])

Arbitary("0", "1", "2", "5", "7")


#Keyword
def keyword(angka5, angka4, angka3, angka2, angka1) :
    print("Angka paling kanan adalah " + angka5)

keyword(angka1 = "0", angka2 = "1", angka3 = "2", angka4 = "5", angka5 = "7")


#Lambda
x = lambda angka1, angka2 : print(angka1+str(angka2))
print(x("17",5))