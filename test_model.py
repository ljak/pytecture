from datetime import date, timedelta
import pytest

from model import OrderLine, Batch

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
    st_batch = Batch("b001", "SMALL_TABLE", 20, today)
    st_ol = OrderLine("or001", "SMALL_TABLE", 2)

    st_batch.allocate(st_ol)
    assert st_batch.quantity == 18


def test_can_allocate_if_available_greater_than_required():
    st_batch = Batch("b001", "SMALL_TABLE", 20, today)
    st_ol = OrderLine("or001", "SMALL_TABLE", 2)

    assert st_batch.can_allocate(st_ol) is True


def test_cannot_allocate_if_available_smaller_than_required():
    st_batch = Batch("b001", "SMALL_TABLE", 1, today)
    st_ol = OrderLine("or001", "SMALL_TABLE", 2)

    assert st_batch.can_allocate(st_ol) is False


def test_can_allocate_if_available_equal_to_required():
    st_batch = Batch("b001", "SMALL_TABLE", 2, today)
    st_ol = OrderLine("or001", "SMALL_TABLE", 2)

    assert st_batch.can_allocate(st_ol) is True


def test_cannot_allocate_if_skus_do_not_match():
    st_batch = Batch("b001", "SMALL_TABLE", 2, today)
    st_ol = OrderLine("or001", "BIG_TABLE", 2)

    assert st_batch.can_allocate(st_ol) is False


def test_can_only_deallocate_allocated_lines():
    return True

@pytest.mark.skip
def test_prefers_warehouse_batches_to_shipments():
    pytest.fail("todo")


@pytest.mark.skip
def test_prefers_earlier_batches():
    pytest.fail("todo")
