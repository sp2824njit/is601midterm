import argparse
import json


def update_customers_obj(order_obj: dict, customers_obj: dict):
    """Scans the order dictionary for customer data and adds the customer
    data to the customers dictionary

    Args:
        order_obj (dict): The dictionary containing order information
        customers_obj (dict): The dictionary containing all customer information
    """
    customers_obj[order_obj['name']] = order_obj['phone']


def update_items_obj(order_obj: dict, items_obj: dict):
    """Scans the order dictionary for ordered items and adds the ordered 
    items to the items dictionary

    Args:
        order_obj (dict): The dictionary containing order information
        items_obj (dict): The dictionary containing all ordered items
    """
    for ordered_item in order_obj['items']:
        ordered_item_name = ordered_item['name']
        ordered_item_price = ordered_item['price']
        if ordered_item_name in items_obj:
            items_obj[ordered_item_name]['orders'] =  items_obj[ordered_item_name]['orders'] + 1
        else:
            items_obj[ordered_item_name] = {
                'price': ordered_item_price,
                'orders': 1
            }

parser = argparse.ArgumentParser()
parser.add_argument('orders_file', help='file containing orders')
args = parser.parse_args()
orders_file_path = args.orders_file

with open(orders_file_path) as f:
    orders_list = json.load(f)

customers_obj = {}
items_obj = {}
for order_obj in orders_list:
    update_customers_obj(order_obj, customers_obj)
    update_items_obj(order_obj, items_obj)
