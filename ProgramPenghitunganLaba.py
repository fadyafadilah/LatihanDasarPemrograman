#M.Fadya Amar Fadilah

#Masukan Variabel Nama Barang
#Masukan Variabel Harga Barang 
#Masukan Variabel Persentasi harga
#Input nama barang 
#Input harga barang 
#Menghitung harga barang
#Harga barang * persen / 100
#Print harga barang beserta nama barang 

while(True):
    nama_barang = input ('Masukan Nama Barang :')
    harga_barang =int(input('Masukan Harga Barang :'))
    besar_untung =int(input('Masukan Besaran Untung :'))
    
    harga_keuntungan = int(harga_barang) * besar_untung/100
    harga_jual = int(harga_barang) + harga_keuntungan
    
    print (nama_barang, 'Dijual dengan Harga :' ,harga_jual)
    
    apakah_lanjut = input('Apakah akan menghitung barang lain ? Y Lanjut N Tidak : ')
    if(apakah_lanjut != 'Y'):
        break
