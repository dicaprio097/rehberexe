from application.ultraconsole import UltraConsole as UC


menu_items = ["Kişi Ekle", "Kişileri Listele", "Kişi Ara", "Kişiyi Güncelle", "Kişiyi Sil"] + ["Geri Dön"]
def rehber(**kwargs):
    anamenu()

def anamenu():
    
    while True:


        secim = UC.create_frame("Rehber", menu_items, "menu")

        if secim == "1":
            ekleme()
        elif secim == "2":
            listele()
        elif secim == "3":
            arama()
        elif secim == "4":
            guncelle_site()
        elif secim == "5":
            sil()
        elif secim == "6":
            print("Çıkılıyor...")
            exit()  
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
        
       
        # input("Ana menüye dönmek için Enter'a basın...")

def ekleme():
    site = UC.create_frame("Site", "Lütfen gireceginiz site ismini giriniz(örnek gmail.com,hotmail.com): ", "")
    sifre = UC.create_frame("Şifre","Lutfen güçlü bir şifre giriniz(max 8 karakter): ", "")
    user = UC.create_frame("Kullanıcı","Lütfen kullanıcı adınızı giriniz: ", "")
    
    if len(sifre) < 8:
        UC.create_frame("Şifre","Şifre en az 8 karakterli olmalı!!!", "")
    else:
        with open("dosya.txt", "a", encoding="utf8") as x:
            x.write(f"{site}|{sifre}|{user}\n")
            UC.create_frame("Şifre",f"{site} için şifre başarıyla oluşturuldu....", "info")

def listele():
    with open("dosya.txt", "r", encoding="utf8") as x:
        z = x.readlines()

    print("SİTE:          ŞİFRE :          KULLANICI ADI:")
    print("-----------------------------------------------------------")

    for satir in z:
        if not satir.strip():
            continue

        try:
            site, sifre, user = satir.strip().split("|")
            print(f"{site:<15} {sifre:<15} {user:<15}")
        except ValueError:
            print(f"Hata: {satir.strip()} formati yanlış. Lütfen dosyayı kontrol et")

def arama():
    anahtar = input("Herhangi birisini giriniz(Site ismi), (Şifre), (Kullanıcı ismi): ")
    
    with open("dosya.txt", "r", encoding="utf8") as x:
        bulundu = False
        z = x.readlines()
        
        for satir in z:
            if anahtar in satir:
                site, sifre, user = satir.strip().split("|")
                print(f"Site:{site} | Şifre:{sifre} | Kullanıcı adı:{user}")
                bulundu = True

        if not bulundu:
            print("╔══════════════════════════╗")
            print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
            print("╚══════════════════════════╝")

def guncelle_site():
    site_guncelle = input("Lütfen şifresini güncelleyeceğiniz Siteyi giriniz: ")
    
    with open("dosya.txt", "r", encoding="utf8") as w:
        z = w.readlines()

    yeni_satirlar = []
    bulundu = False

    for satir in z:
        satir = satir.strip()

        if not satir or '|' not in satir:
            yeni_satirlar.append(satir + '\n')
            continue

        try:
            site, sifre, user = satir.split("|")
        except ValueError:
            print(f"Hatalı satır atlandı: {satir}")
            yeni_satirlar.append(satir + '\n')
            continue

        if site_guncelle == site:
            yeni_sifre = input("Lütfen yeni şifreyi giriniz: ")
            yeni_satir = f"{site}|{yeni_sifre}|{user}\n"
            bulundu = True  
        else:
            yeni_satir = satir + '\n'

        yeni_satirlar.append(yeni_satir)

    if not bulundu:
        print("╔══════════════════════════╗")
        print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
        print("╚══════════════════════════╝") 
        return  

    with open("dosya.txt", "w", encoding="utf8") as dosya:
        dosya.writelines(yeni_satirlar)

    print("Şifreniz başarıyla güncellendi!")

def sil():
    site_sil = input("Lütfen silmek istediğiniz adresi yazın: ")

    with open("dosya.txt", "r", encoding="utf8") as f:
        satirlar = f.readlines()

    yeni_satirlar = []
    bulundu = False

    for satir in satirlar:
        satir = satir.strip()

        if not satir or '|' not in satir:
            yeni_satirlar.append(satir + '\n')
            continue

        try:
            site, sifre, user = satir.split("|")
        except ValueError:
            print(f"Hatalı format: {satir}")
            yeni_satirlar.append(satir + '\n')  
            continue  

        if site_sil == site:
            bulundu = True
            print(f"{site} silindi.")
        else:
            yeni_satirlar.append(satir + '\n')

    if not bulundu:
        print(f"Site {site_sil} bulunamadı.")

    with open("dosya.txt", "w", encoding="utf8") as f:
        f.writelines(yeni_satirlar)


anamenu()
# .