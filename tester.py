from models.product_model import ProductModel
from controllers.product_controller import ProductController

product_1 = ProductModel()
product_controller = ProductController(product_1)
product_controller.create_product(
    name="Test Product",
    description="This is a test product.",
    main_category_ID=1,
    categories_IDs=[1, 2],
    brand_ID=1,
    supplier_ID=1,
    images=["image1.jpg", "image2.jpg"],
    sale_unit="piece"
)
product_controller.add_variant(
    sku="TESTSKU001",
    barcode="1234567890123",
    buy_price=10.0,
    sell_price=15.0,
    stock_quantity=100,
    vat_included=True,
    vat_rate=18.0,
    variant_type_ID=1,
    variant_type_name="Color",
    variant_type_values=["Red", "Blue", "Green"]
)
product_controller.add_variant(
    sku="TESTSKU002",
    barcode="1234567890124",
    buy_price=12.0,
    sell_price=18.0,
    stock_quantity=50,
    vat_included=True,
    vat_rate=18.0,
    variant_type_ID=1,
    variant_type_name="Color",
    variant_type_values=["Yellow", "Black", "White"]
)
product_controller.add_variant(
    sku="TESTSKU003",
    barcode="1234567890125",
    buy_price=15.0,
    sell_price=20.0,
    stock_quantity=30,
    vat_included=True,
    vat_rate=18.0,
    variant_type_ID=1,
    variant_type_name="Color",
    variant_type_values=["Purple", "Orange", "Pink"]
)
print(product_controller.get_product_data().name)
print(product_controller.get_product_data().description)
print(product_controller.get_product_data().main_category_ID)
print(product_controller.get_product_data().categories_IDs)
print(product_controller.get_product_data().brand_ID)
print(product_controller.get_product_data().supplier_ID)

for variant in product_controller.get_product_data().variants:
    print(variant.sku)
    print(variant.barcode)
    print(variant.buy_price)
    print(variant.sell_price)
    print(variant.stock_quantity)
    print(variant.vat_included)
    print(variant.vat_rate)
    print(variant.variant_type.name)
    print(variant.variant_type.values)
