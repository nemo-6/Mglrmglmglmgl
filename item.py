from math import inf
from fakedb import fakedb


class Item:
    def __init__(self, item_id):
        self.item_id = item_id
        item = fakedb[item_id]
        self.name = item['name']
        self.components = item['components']
        self.npc_price = item['npc_price']

    # Best price overall, [source, price(s)] in a recursive tree
    def price(self, auction_list):
        possible_prices = []
        # Auction house price
        specific_auction_list = [auction for auction in auction_list if auction['item']['id'] == self.item_id]
        if len(specific_auction_list) > 0:
            cheapest_auction = min(specific_auction_list, key=lambda auction: auction['unit_price'])
            possible_prices.append([self.item_id, 'AH', cheapest_auction['unit_price']])

        # Crafting price
        if self.components:
            total = 0
            price_list = list()
            for item_id, amount in self.components.items():
                item = Item(item_id)
                item_price = item.price(auction_list)
                price_list.append(item_price)
                total += item_price[2] * amount
            possible_prices.append([self.item_id, 'CRA', total, price_list])

        # Npc price
        if self.npc_price:
            possible_prices.append([self.item_id, 'NPC', self.npc_price])

        cheapest_price = min(
            possible_prices,
            key=lambda x: x[2]
        )

        return cheapest_price
