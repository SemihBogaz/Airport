from datetime import datetime

from Airport.AirlinesCompany import Company
from Airport.Cities import Cities
from Airport.Customer import Customer


def Main():
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
    cities = list()

    for i in c.splitlines():
        cities.append(Cities(i))

    passenger = Customer("John", "Doe", 10987654321)
    company = Company()
    flight1 = company.add_flight(cities[1], cities[80], datetime(2019,8,8,5,30))
    ticket = company.add_ticket(passenger, flight1, "A4")
    print(ticket)
    company.tardiness(flight1, 150)
    print(ticket)


if __name__ == "__main__":
    Main()
