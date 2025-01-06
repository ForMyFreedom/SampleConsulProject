from ProductModel import ProductModel
from App import db
from LogInfra import sendToLog
from Domain import Product, InfraResponse

def AddProductInDB(data: Product) -> InfraResponse:
    try:
        item = ProductModel.create(data)
        db.session.add(item)
        db.session.commit()
        return InfraResponse(item, None)
    except Exception as e:
        sendToLog({'event': 'item_add_error', 'error': str(e)})
        return InfraResponse(None, str(e))


def SendProductRegisterActionLog(item: Product):
    sendToLog({'event': 'item_added', 'item_id': item.id, 'name': item.name})
