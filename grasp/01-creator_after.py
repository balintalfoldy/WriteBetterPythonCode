from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int


@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())

    # The Sale class is responsible to create the SaleLineItems
    def add_line_item(self, product: ProductDescription, quantity: int):
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDescription(price=5_000, description="Gaming headset")
    keyboard = ProductDescription(price=7_500, description="Mechanical gaming keyboard")

    # Now, we don't need to know how the Sale class is structured, we simply 
    # have to know that we can order products with quantities
    sale = Sale()
    sale.add_line_item(product=headset, quantity=2)
    sale.add_line_item(product=keyboard, quantity=3)

    print(sale)


if __name__ == "__main__":
    main()
