laporan_minuman = [
    {
        'nama': 'kopi',
        'harga': '11000',
        'terjual': '10',
        'modal_satuan': '6000',
    },
    {
        'nama': 'teh_ES',
        'harga': '6000',
        'terjual': '12',
        'modal_satuan': '3500',
    },
    {
        'nama': 'jus',
        'harga': '10000',
        'terjual': '7',
        'modal_satuan': '6000',
    },
] # tidak ada yg perlu dibuah dsn

# isi list makanan dan untuk nama, harga, terjual, modal satuan bebas tetapi diinput melalui terminal (cukup 2 makanan)
laporan_makanan = [
    {
        'nama': input("Nama Makanan 1 :"),
        'harga': input("Harga Makanan 1 :"),
        'terjual': input("Banyak Makanan 1 Telah Terjual :"),
        'modal_satuan': input("Modal Makanan 1 :"),
    },
    {
        'nama': input("Nama Makanan 2 :"),
        'harga': input("Harga Makanan 2 :"),
        'terjual': input("Banyak Makanan 2 Telah Terjual :"),
        'modal_satuan': input("Modal Makanan 2 :"),
    }

] # format makanan samad dengan minuman
# """
# format makanan
# {
#         'nama': '',
#         'harga': '',
#         'terjual': '',
#         'modal_satuan': ,
# }
# """

penjualan = {
    'minuman': laporan_minuman,
    'makanan': laporan_makanan,
    'summary': {
        'total_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':''
        },
        'keuntungan_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':'',
        },
        'special_case':'total_semua_penjualan+total_semua_keuntungan_penjualan+special_value+10000' # juga tidak ada yg perlu diubah dsn
    }
}

# lakukan programn didalam fungsi ini
def main():
    global minuman, makanan, penjualan
    special_value =  2011512010
    print("Semangat Upgrading, Machine Learning Semangat")







    total_semua_penjualan = penjualan['summary']['total_penjualan']['semua'] # juga tidak ada yg perlu diubah dsn
    total_semua_keuntungan_penjualan = penjualan['summary']['keuntungan_penjualan']['semua'] # juga tidak ada yg perlu diubah dsn
    special_case = penjualan['summary']['special_case'] # perlu sedikit penambahan

if __name__ == "__main__":
    main()
