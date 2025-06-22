import data
import configuration
import create_order_request
import requests

def test_check_order_created():
    order_body=create_order_request.get_order_body("Васек", "Безымянный", "Без адресный", '204', '+7 800 555 35 35','2025-06-06')
    order_response=create_order_request.create_order(order_body)
    print(order_response.json())

    assert order_response.status_code==201, f"Ожидался статус 201, получили {order_response.status_code}"
    response_track = order_response.json()['track']
    order_done = create_order_request.get_order_by_track(response_track)










