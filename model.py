from dataclasses import dataclass
from typing import Optional, Set
from datetime import date


# normalization on the flight -> already given the order reference
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
    # _allocations: Set[OrderLine] = set()

    def allocate(self, order_line: OrderLine):
        if self.can_allocate(order_line):
            self.quantity -= order_line.quantity

    def can_allocate(self, order_line: OrderLine) -> bool:
        return self.quantity >= order_line.quantity and self.SKU == order_line.SKU
