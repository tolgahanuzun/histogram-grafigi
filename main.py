import matplotlib.pyplot as plt # lib

adres = raw_input() # kullanicidan metin adresi isteniyor.
veri = open(adres,'r') # dosta islemleri

dizi = veri.read() #dosya okunuyor
uzunluk = len(dizi.split())  # uzunluk hesaplaniyor

#diziler yaratiliyor
yenix = [[0 for x in range(1)] for x in range(int(uzunluk/2))]
yeniy = [[0 for x in range(1)] for x in range(int(uzunluk/2))]

#veriler isleniyor ve gereksiz karekterler yok ediliyor.
yeni =  dizi.split()

#x ve y eksenleri ayristiriliyor
say=0
for i in range(1, uzunluk, 2):
	yenix[say] = int(yeni[i])
	say=say+1
	
say=0
for j in range(0, uzunluk, 2):
	yeniy[say] =int(yeni[j])
	say=say+1
	

#goruntu olusturma kismi
plt.bar(yenix,yeniy,width = 1)
plt.title('Histogram')
plt.grid(True)
plt.show() 

