toplam_saniye=int(input('süreyi giriniz '))
saat=toplam_saniye//3600
kalan_saniye=toplam_saniye % 3600
dakika=kalan_saniye//60
son_kalan_saniye=kalan_saniye%60
print(str(saat)+" saat ," , str(dakika)+" dakika ," , str(son_kalan_saniye)+" saniye")



