B1 = int(input("Masukkan bilangan 1 : "))
B2 = int(input("Masukkan bilangan 2 : "))
B3 = int(input("Masukkan bilangan 3 : "))

if B1>B2>B3 :
    print("Urutan bilangan dari yang terbesar adalah", B1, B2, B3)
elif B1>B3>B2 :
    print("Urutan bilangan dari yang tebesar adalah", B1, B3, B2)
elif B2>B3>B1 :
    print("Urutan bilangan dari yang terbesar adalah", B2, B3, B1)
elif B2>B1>B3 :
    print("Urutan bilangan dari yang terbesar adalah", B2, B1, B3)
elif B3>B2>B1 :
    print("Urutan bilangan dari yang terbesar adalah", B3, B2, B1)
elif B3>B1>B2 :
    print("Urutan bilangan dari yang terbesar adalah", B3, B1, B2)
elif B1==B2>B3 :
     print("Urutan bilangan dari yang terbesar adalah", B1, B2, B3)
elif B1==B3>B2 :
     print("Urutan bilangan dari yang terbesar adalah", B1, B3, B2)
elif B2==B1>B3 :
     print("Urutan bilangan dari yang terbesar adalah", B2, B1, B3)
elif B2==B3>B1 :
     print("Urutan bilangan dari yang terbesar adalah", B2, B3, B1)
elif B3==B1>B2 :
     print("Urutan bilangan dari yang terbesar adalah", B3, B1, B2)
elif B3==B2>B1 :
     print("Urutan bilangan dari yang terbesar adalah", B3, B2, B1)
elif B1>B2==B3 :
     print("Urutan bilangan dari yang terbesar adalah", B1, B2, B3)
elif B2>B3==B1 :
     print("Urutan bilangan dari yang terbesar adalah", B2, B3, B1)
elif B3>B1==B2 :
     print("Urutan bilangan dari yang terbesar adalah", B3, B1, B2)
else :
    print("error")
