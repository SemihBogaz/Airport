from datetime import datetime
from random import randint

c = """Adana
Adıyaman
Afyon 
Ağrı 
Amasya
Ankara
Antalya
Artvin
Aydın
Balıkesir
Bilecik
Bingöl
Bitlis
Bolu
Burdur
Bursa
Çanakkale
Çankırı
Çorum
Denizli
Diyarbakır
Edirne
Elazığ
Erzincan
Erzurum
Eskişehir
Gaziantep
Giresun
Gümüşhane
Hakkari
Hatay
Isparta
İçel
İstanbul
İzmir
Kars
Kastamonu
Kayseri
Kırklareli
Kırşehir
Kocaeli
Konya
Kütahya
Malatya
Manisa
K.maraş
Mardin
Muğla
Muş
Nevşehir
Niğde
Ordu
Rize
Sakarya
Samsun
Siirt
Sinop
Sivas
Tekirdağ
Tokat
Trabzon
Tunceli
Şanlıurfa
Uşak
Van
Yozgat
Zonguldak
Aksaray
Bayburt
Karaman
Kırıkkale
Batman
Şırnak
Bartın
Ardahan
Iğdır
Yalova
Karabük
Kilis
Osmaniye
Düzce"""

cities = c.splitlines()


class Cities:
    def __init__(self, name: str):
        self.__Name = name
        self.__Temperature = randint(18, 25)
        self.__Weather = ["Sunny", "Rainy", "Foggy", "Windy"][randint(0, 3)]

    def get_name(self):
        return self.__Name

    def set_name(self, name):
        self.__Name = name

    def get_temp(self):
        return self.__Temperature

    def get_weather(self):
        return self.__Weather

    def __str__(self):
        return self.__Name

    # did not create setter methods for temp & weather
