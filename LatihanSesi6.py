#Program Penentuan Nilai Kelulusan
nama = input("\nMasukan Nama Mahasiswa :")
nilai = input("\nMasukan Nilai : ")
#input nilai
if (nilai.isnumeric() == True) :
    nilai_int = int(nilai)
    #kondisi percabangan   
    if nilai_int > 90 < 100 :
        grade = "A"
        predikat = "Nilai kamu bagus sekali , Minggu depan langsung skripsi"
    elif nilai_int >80 <89 :
        grade = "B"
        predikat = "Sangat Memuaskan"
    elif nilai_int >70 <79 :
        grade = "C"
        predikat = "Memuaskan"
    elif nilai_int >60 <69 :
        grade = "D"
        predikat = "Tidak Memuaskan"
    elif nilai_int >0 <59 :
        grade = "E"
        predikat = "Tidak LULUS"  
         
    #output
    print("\n=============================")
    print("Nama Mahasiswa  : " ,nama)
    print("Grade Anda      : " ,grade)
    print("Predikat        : " ,predikat)

else:
    print('Format yang anda masukan salah')