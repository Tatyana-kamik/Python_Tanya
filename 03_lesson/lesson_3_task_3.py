from address import Address
from mailing import Mailing


to_address = Address("109444", "Москва", "Сормовская", "1", "10")
from_address = Address("123456", "Санкт-Петербург", "Невский проспект", "2",
                       "5")


mailing = Mailing(to_address, from_address, 150, "TRK123456")


print(
    f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в {mailing.to_address.postal_code}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
