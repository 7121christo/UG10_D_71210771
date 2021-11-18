H1 = int(input("Harga makanan sebesar Rp "))
H2 = int(input("Harga snack sebesar Rp "))
H3 = int(input("Harga minuman sebesar Rp "))
Uang = int(input("Uang yang anda bawa sebesar Rp "))

total = H1+H2+H3
utang = Uang-total
kembalian = Uang-total

print("\nTotal yang harus anda bayar sebesar RP ", total)

if Uang == total :
    print("uang anda pas! Tidak ada kembalian dan Utang : D")
elif Uang < total :
    print("Uang anda kurang! Anda memiliki utang sebesar Rp ", utang)
elif Uang > total :
    print("Anda memiliki kembalian sebesar Rp ", kembalian)
else :
    print("error")
