from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 15", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S23+", "+79268862256"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 6", "+79456789012"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79567890123"))


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}"
          )
