#M.Fadya Amar Fadilah

#Masukan Variabel Nama Barang
#Masukan Variabel Harga Barang 
#Masukan Variabel Persentasi harga
#Input nama barang 
#Input harga barang 
#Menghitung harga barang
#Harga barang * persen / 100
#Print harga barang beserta nama barang 

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input ('Masukan Nama Barang :')
    harga_barang =int(input('Masukan Harga Barang : Rp.'))
    persen =int(input('Masukan Besaran Untung: '))
    barang_terjual = int(input ('Masukan Jumlah Barang terjual :'))

    
    keuntungan_persen =(harga_barang *persen/100)

    harga_jual = int(harga_barang + keuntungan_persen)

    #menghitung modal
    modal = harga_barang * barang_terjual
    #menghitung modal keseluruha
    modal_keseluruhan = modal_keseluruhan + modal

    #menghitung laba
    laba = harga_keuntungan = modal_keseluruhan + modal

    #menghitung laba keseluruhan 
    laba_keseluruhan = harga_keuntungan + laba

    print('Barang' , nama_barang)
    print('Harga', harga_barang)
    print('Keuntungan Per Barang' ,harga_keuntungan)
    print('Dijual Dengan Harga', harga_jual)
    print('Terjual', barang_terjual)
    print('Modal' , modal)
    print('Laba' , laba)

    apakah_lanjut = input('Apakah akan menghitung barang lain ? Y Lanjut N Tidak : ')
    if(apakah_lanjut != 'Y'):
        break

print('----------------------------')
print('modal keseluruhan' , modal_keseluruhan)
print('laba keuntungan',laba_keseluruhan)