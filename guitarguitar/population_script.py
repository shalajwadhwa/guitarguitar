import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guitarguitar.settings')
import django
django.setup()

from datetime import datetime
import json
import requests

from team20.models import Customer, Orders, Products

## Scrape the data from the given urls
def scrape_info(url):
    res = requests.get(url)
    res_json = json.loads(res.text)
    return res_json

def populate():
    ## Populate the database with the scraped data
    for customer in scrape_info('https://guitarguitar.co.uk/hackathon/customers/'):
        cust = Customer.objects.get_or_create(
            customer_id=customer['Id'],
            first_name=customer['first_name'],
            last_name=customer['last_name'],
            email=customer['email'],
            phone_number=customer['phone_number'],
            avatar=customer['avatar'],
            address=customer['address'],
            loyalty_level=customer['LoyaltyLevel']
        )[0]
        cust.save()

    for order in scrape_info('https://guitarguitar.co.uk/hackathon/orders/'):
        #  date is in format “2021-08-15T05:52:00” so need to convert to date
        date_created = order['DateCreated'].split('T')[0]
        # convert date_created to python date object
        date_created = datetime.strptime(date_created, '%Y-%m-%d').date()
        ord = Orders.objects.get_or_create(
            order_id=order['Id'],
            customer_id=Customer.objects.get(customer_id=order['CustomerId']),
            shipping_address=order['ShippingAddress'],
            products=order['Products'],
            date_created=date_created,
            order_total=order['OrderTotal'],
            order_status=order['OrderStatus']
        )[0]
        ord.save()
    
    for product in scrape_info('https://guitarguitar.co.uk/hackathon/products/'):
        date_created = order['DateCreated'].split('T')[0]
        # convert date_created to python date object
        date_created = datetime.strptime(date_created, '%Y-%m-%d').date()
        prod = Products.objects.get_or_create(
            sku_id=product['SKU_ID'],
            asn=product['ASN'],
            category=product['Category'],
            online=product['Online'],
            item_name=product['ItemName'],
            brand_name=product['BrandName'],
            description=product['Description'],
            product_detail=product['ProductDetail'],
            sales_price=product['SalesPrice'],
            picture_main=product['PictureMain'],
            qty_in_stock=product['QtyInStock'],
            qty_on_order=product['QtyOnOrder'],
            colour_option=product['Colour'],
            pickup_option=product['Pickup'],
            created_on=date_created,
            body_shape=product['BodyShape']
        )[0]
        prod.save()

    print("Database populated successfully")

if __name__ == '__main__':
    print("Starting population script...")
    populate()

