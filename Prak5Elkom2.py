print("---------------Hitung Gaji Harian------------")
jammasuk=input("Jam Masuk Kerja:")
jamkeluar=input("Jam Keluar Kerja:")
def greetings(waktu): 
    if float (waktu) > 00.00 and float (waktu) <= 12.00:
        print(waktu,"Selamat Pagi")
    if float (waktu) > 12.00 and float (waktu) <= 15.00: 
        print(waktu,"Selamat Siang")
    if float (waktu) > 15.00 and float (waktu) <= 18.00:
        print(waktu,"Selamat Sore")
    if float (waktu) > 18.00 and float (waktu) <= 24.00:
        print(waktu,"Selamat Malam")

def waktukerja(jammasuk,jamkeluar):
    jammasuk=jammasuk.split(".")
    jamkeluar=jamkeluar.split(".")
    jamin=int(jammasuk[0])
    jamout=int(jamkeluar[0])
    menitin=int(jammasuk[1])
    menitout=int(jamkeluar[1])
    if menitout<menitin:
        menitout=menitout+60
        jamout=jamout-1
    menit=menitout-menitin
    jam=jamout-jamin
    if menit<10:
        menit="0"+str(menit)
    if jam<10:
        jam="0"+str(jam)
    print("waktu kerja:",jam,'.',menit)

greetings(jammasuk)
greetings(jamkeluar)
waktukerja(jammasuk,jamkeluar)
print("----------------Rincian Gaji-----------------")
waktukerja= float(jamkeluar)-float(jammasuk)
gajiperhari=175000
print("Gaji Perhari:Rp.",gajiperhari)
jamlembur= waktukerja-8
lembur= jamlembur *15000
print("Uang Lembur:Rp.",lembur)
totalgaji= gajiperhari+lembur
print("Total Gaji:Rp.",totalgaji)

