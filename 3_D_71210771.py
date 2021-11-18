DB = str(input("Masukkan daftar belanja Anda : ")).title().split(",")
print("Daftar belanja : ", DB)
TBH = input("Masukan barang yang ingin ditambahkan : ").lower()

if TBH.title() in DB :
    print("Barang", TBH.upper(), "sudah berada dalam daftar belanja")
else :
    DB.append(TBH.upper())
    print("Hasil penambahan pada daftar belanja", DB)

