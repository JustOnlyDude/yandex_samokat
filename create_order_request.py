import configuration
import requests
import data

def get_order_body (first_name, last_name, address, metro_station, phone, delivery_date, comment = 'null'):
    current_order_body = data.order_body.copy()
    current_order_body["firstName"] = first_name
    current_order_body["lastName"]= last_name
    current_order_body["address"] = address
    current_order_body["metroStation"] = metro_station
    current_order_body["phone"] = phone
    current_order_body["deliveyDate"] = delivery_date
    current_order_body["comment"] = comment

    return current_order_body


def create_order(body):
    return requests.post(configuration.URL_BASE + configuration.ORDER_CREAT, json=body, headers=data.headers)


def get_order_by_track(track):
     return requests.get(configuration.URL_BASE + configuration.ORDER_BY_TRACK, params={'t': track})
