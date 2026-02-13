from models.variant_type_model import VariantTypeModel

class VariantModel:
    def __init__(self):
        self.ID : int
        self.sku : str
        self.barcode : str
        self.buy_price : float
        self.sell_price : float
        self.stock_quantity : int
        self.vat_included : bool
        self.vat_rate : float
        self.variant_type : VariantTypeModel = VariantTypeModel()
        
