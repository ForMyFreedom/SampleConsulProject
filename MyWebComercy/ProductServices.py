from ProductInfra import AddProductInDB, SendProductRegisterActionLog

def AddProductService(data):
    item = AddProductInDB(data)
    if item.error:
        return item.error, 400
    else:
        SendProductRegisterActionLog(item.data)
        return {'message': 'Item added', 'item': item.data.toJSON()}, 201
