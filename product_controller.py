from models.product_model import ProductModel
from models.variant_model import VariantModel
from models.variant_type_model import VariantTypeModel

class ProductController:
    def __init__(self, model : ProductModel = None):
        if model is None:
            raise Exception("ProductModel instance is required")
        else:
            self.product_model = model
    
    def create_product(self, name, description, main_category_ID, categories_IDs, brand_ID, supplier_ID, images, sale_unit):
        self.product_model.name = name
        self.product_model.description = description
        self.product_model.main_category_ID = main_category_ID
        self.product_model.categories_IDs = categories_IDs
        self.product_model.brand_ID = brand_ID
        self.product_model.supplier_ID = supplier_ID
        self.product_model.images = images
        self.product_model.sale_unit = sale_unit
    
    def add_variant(self, sku, barcode, buy_price, sell_price, stock_quantity, vat_included, vat_rate, variant_type_ID, variant_type_name, variant_type_values):
        variant = VariantModel()
        variant.sku = sku
        variant.barcode = barcode
        variant.buy_price = buy_price
        variant.sell_price = sell_price
        variant.stock_quantity = stock_quantity
        variant.vat_included = vat_included
        variant.vat_rate = vat_rate
        variant.variant_type.ID = variant_type_ID
        variant.variant_type.name = variant_type_name
        variant.variant_type.values = variant_type_values
        self.product_model.variants.append(variant)
    
    def validate_product(self):
        try:
            self.product_model.validate()
            for variant in self.product_model.variants:
                variant.validate()
            return True, "Product is valid."
        except ValueError as e:
            return False, str(e)
    
    def get_product_data(self):
        return self.product_model
    
