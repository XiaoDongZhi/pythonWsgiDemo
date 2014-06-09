# controller example

class InventoryItem:
    def __init__(self):
        pass

    sku = ""
    price = 0
    quantity = 0


def list_inventory(self):
    sku1 = InventoryItem()
    sku1.price = 3.25
    sku1.quantity = 200
    sku1.sku = "ARABIC-001"

    sku2 = InventoryItem()
    sku2.price = 4.75
    sku2.quantity = 100
    sku2.sku = "GUAT-001"

    return [sku1, sku2]
