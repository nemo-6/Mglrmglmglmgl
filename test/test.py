from model.item import Item


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
