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

from connector_type import TallyConnector, ZohoConnector, OddoConnector

connector = "oddo"

match connector:
    case "oddo":
        accounting = OddoConnector(payload=data, api_key="oddu_121", token=2763)
    case "tally":
        accounting = TallyConnector(payload=data, port = 9000, host = 'localhost')
    case "zoho":
        accounting =  ZohoConnector(payload=data, api_key="a9012")
    case _:
        accounting = TallyConnector(payload=data, port=6793, host="default")


accounting.push()

# zoho.push()

