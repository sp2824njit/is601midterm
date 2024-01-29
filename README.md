# IS 601 Midterm Project

## What It Does
Reads a JSON file containing orders and outputs a JSON file containing customer information and a JSON file containing information about ordered items

## Usage
`py midterm.py <Relative path to orders JSON file>`


## Design
Program collects file path of orders JSON file at command line. Program loads JSON-encoded text into memory as a python dictionary. For each order item, program updates its information about customers and the ordered items