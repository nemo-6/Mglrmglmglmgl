from model.item import Item
from model.price import Price


def test_cheaper():
    test_cheaper_to_craft = [
        {'id': 1635157914, 'item': {'id': 173058}, 'quantity': 1, 'unit_price': 375 + 2, 'time_left': 'VERY_LONG'},
        {'id': 1635157914, 'item': {'id': 173056}, 'quantity': 1, 'unit_price': 1, 'time_left': 'VERY_LONG'},
    ]
    test_cheaper_to_buy = [
        {'id': 1635157914, 'item': {'id': 173058}, 'quantity': 1, 'unit_price': 375, 'time_left': 'VERY_LONG'},
        {'id': 1635157914, 'item': {'id': 173056}, 'quantity': 1, 'unit_price': 1, 'time_left': 'VERY_LONG'},
    ]
    umbral_ink = Item(173058)

    assert umbral_ink.get_cheapest_price(test_cheaper_to_buy).source == 'AH'
    assert umbral_ink.get_cheapest_price(test_cheaper_to_craft).source == 'CRA'


def test_price():
    price100 = Price(100, 'NPC')
    price200 = Price(200, 'CRA')
    price2 = Price(2, 'AH')
    assert min([price100, price2]) == price2
    assert min([price100, price200]) == price100
    assert max([price100, price2]) == price100
    assert max([price100, price200]) == price200
