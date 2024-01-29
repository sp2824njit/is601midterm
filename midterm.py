import argparse

parser = argparse.ArgumentParser()
parser.add_argument('orders_file', help='file containing orders')
args = parser.parse_args()
orders_file_path = args.orders_file
