from models.variant_model import VariantModel
from datetime import datetime,timezone


class ProductModel:
    def __init__(self):
        self.ID : int
        self.is_active : bool = None
        self.name  : str
        self.description  : str = ""
        self.main_category_ID  : int
        self.categories_IDs : list[int]
        self.brand_ID : int
        self.supplier_ID : int
        self.images : list
        self.sale_unit : str
        self.variants : list[VariantModel] = []
        self.created_at : datetime


