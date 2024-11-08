# заголовки для HTTP - запроса, указывающие, что тела запроса будут в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные заказчика для создания нового заказа
order_body = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, ул.Пушкина дом Колотушкина",
    "metroStation": 88,
    "phone": "+74916123451",
    "rentTime": 3,
    "deliveryDate": "2024-11-25"
}

