# design a system where you are given data of the document and we need to pushe it to accounting softwares (design in such a way that it in future also it can support many external accounting softwares)

data = {
    "invoice_number": "INV-001",
    "date": "2023-10-01",
    "customer": "John Doe",
    "items": [
        {
            "name": "Product A",
            "quantity": 10,
            "rate": 100.00
        }
    ]
}

from connector_type import TallyConnector, ZohoConnector

tally = TallyConnector(payload=data, port = 9000, host = 'localhost')

zoho = ZohoConnector(payload=data, api_key="a9012")

tally.push()

# zoho.push()

