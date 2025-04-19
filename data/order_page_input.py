from pydantic import BaseModel


class OrderData(BaseModel):
    first_name: str
    last_name: str
    address: str
    subway_station: str
    phone_number: str
    date: str
    order_duration: int
    color: list[str]
    notes: str


class Orders:
    inputs = [
        OrderData(first_name='Иван',
                  last_name='Иванов',
                  address='Красная Площадь',
                  subway_station='Библиотека имени Ленина',
                  phone_number='89999999999',
                  date='09.05.2025',
                  order_duration=1,
                  color=['black'],
                  notes='пожалуйста'),
        OrderData(first_name='Петр',
                  last_name='Петрович',
                  address='Остановка у метро',
                  subway_station='Молодёжная',
                  phone_number='81234567899',
                  date='01.05.2025',
                  order_duration=4,
                  color=['black', 'grey'],
                  notes='быстрее')
    ]
