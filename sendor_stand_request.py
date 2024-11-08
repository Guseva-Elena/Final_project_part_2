import configuration
import data
import requests

# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

# Получение заказа по номеру трека
def get_order(track_number):
    get_order_url = configuration.URL_SERVICE + configuration.GET_TRACK_ORDER.format(track=track_number)
    response = requests.get(get_order_url)
    return response

# автотест
# Создание заказа с номером трека
def test_create_order():
    order_body = data.order_body
    response = create_order(order_body)
    response_json = response.json()
    track_number = response_json["track"]
    print("Заказ создан. Номер трека заказа:", track_number)

# Получение заказа по номеру трека
    order_response = get_order(track_number)
    assert order_response.status_code == 200
    order_data = order_response.json()
    print("Код ответа:")
    print(order_response.status_code)
    print("Данные заказа:")
    print(order_data)
