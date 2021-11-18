A = int(input("Nilai a : "))
B = int(input("Nilai b : "))
C = int(input("Nilai c : "))

D = (B**2)-4*A*C
x1 = -B-(D**0.5)/2*A
x2 = -B+(D**0.5)/2*A

if D < 0 :
    print("Fungsi tersebut tidak memiliki akar riil")
elif D > 0 :
    print("Akar akar dari persamaan tersebut adalah ", x1, "dan", x2)
elif D == 0 :
    print("Fungsi tersebut memiliki akar kembar yaitu ", x1)


