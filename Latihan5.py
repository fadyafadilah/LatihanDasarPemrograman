#M. FADYA AMAR FADILAH

#Masukan Variabel Nama Barang
#Masukan Variabel Harga Barang 
#Masukan Variabel Persentasi Untung
#Input Nama Barang
#Input Harga Barang
#Menghitung Harga Barang
#Harga Barang * Persen /100
#Print Harga Barang Beserta Nama Barang



#----------------------------------------------------------------#

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input('Masukan Nama Barang : ')
    harga_barang = int(input('Masukan Harga Barang : Rp.'))
    persen = int(input('Masukan Persenan Untung : '))
    barang_terjual = int(input('Masukan Jumlah Barang Terjual : '))

    keuntungan_persen = harga_barang * persen / 100
    harga_jual = harga_barang + keuntungan_persen

    #Menghitung Modal
    modal = harga_barang * barang_terjual 

    #Menghitung Modal Keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    #Menghitung Laba
    laba = keuntungan_persen * barang_terjual

    #Menghitung Laba Keseluruhan 
    laba_keseluruhan = laba_keseluruhan + laba


    print('------------------------------------------')
    print('Barang :', nama_barang)
    print('Harga Barang : Rp. ', harga_barang)
    print('Keuntungan Per Barang : Rp. ', keuntungan_persen)
    print('Dijual Dengan Harga : Rp. ', harga_jual)
    print('Barang Terjual : ', barang_terjual)
    print('Modal : Rp. ', modal)
    print('laba : Rp. ', laba)

    apakah_lanjut = input('Apakah ingin input barang lain ? Y Lanjut N Tidak ')
    if(apakah_lanjut!='Y') :
        break

print('------------------------------------------')
print('Modal Keseluruhan',modal_keseluruhan)
print('Laba Keseluruhan',laba_keseluruhan)



