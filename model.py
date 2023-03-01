from dataclasses import dataclass
from typing import Optional
from datetime import date


# normalization on the flight -> already given the order referenc
@dataclass
class OrderLine:
    order_reference: str
    SKU: str
    quantity: int


@dataclass
class Batch:
    reference: str
    SKU: str
    quantity: int
    eta: Optional[date]

    def allocate(self, order_line: OrderLine):
        assert self.SKU == order_line.SKU
        if self.quantity >= order_line.quantity:
            self.quantity -= order_line.quantity
        return True
