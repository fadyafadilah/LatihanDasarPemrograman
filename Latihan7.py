#Program Aplikasi Penghitung Rumus
#M.FADYA AMAR FADILAH

print("Program Kalkulator Sederhana")

while (True):
    print(" \n========================================")
    print("Menu")
    print(" 1. Hitung Luas Segitiga")
    print(" 2. Hitung Luas Persegi Panjang")
    print(" 3. Tentukan number ganjil genap")
    print(" 4. Quit")

    print(" \n----------------------------------------")

    listMenu = input("Masukan Pilihan : ")

    if listMenu == "1":
        print("Menu -- Hitung Luas Segitiga")
        alas = int(input("\nMasukan Panjang Alas : "))
        tinggi = int(input("Masukan Tinggi : "))

        rumus1 = 1/2 * alas * tinggi
        print("\nLuas Segitiga : ", rumus1)
        print("\n=== === === === ===")
        
        
        
        
        
        
        
        
        

    elif listMenu == "2":
        print("Menu -- Hitung Luas Persegi Panjang")
        panjang = int(input("\nMasukan Panjang : "))
        lebar = int(input("Masukan Lebar : "))

        rumus2 = panjang * lebar
        print("\nLuas Persegi Panjang : ", rumus2)
        print("\n=== === === === ===")

    elif listMenu == "3":
        print("Menu -- Tentukan number ganjil genap")
        angka = int(input("\nMasukan Angka : "))

        if (angka % 2 == 0):
            print("\nAngka", angka, "merupakan angka Genap.")
        else:
            print("\nAngka", angka, "merupakan angka Ganjil.")

        print("\n=== === === === ===")

    else:
        menu = input("\n\-----------")
        print("--- --- --- --- ---")
        break