from fakedb import fakedb
from model.price import Price


class Item:
    def __init__(self, item_id):
        self.item_id = item_id
        item = fakedb[item_id]
        self.name = item['name']

        if len(item['components']) > 0:
            self.components = item['components']
        else:
            self.components = None

        if item['npc_price']:
            self.npc_price = Price(item['npc_price'], 'NPC')
        else:
            self.npc_price = None

    def get_ah_price(self, auction_list):
        specific_auction_list = [
            auction for auction in auction_list
            if auction['item']['id'] == self.item_id
        ]
        if len(specific_auction_list) > 0:
            cheapest_auction = min(specific_auction_list, key=lambda auction: auction['unit_price'])
            return Price(cheapest_auction['unit_price'], 'AH')

    def get_npc_price(self):
        return Price(self.npc_price, 'NPC')

    def get_crafting_price(self, auction_list):
        if self.components:
            total = 0
            price_list = list()
            for item_id, amount in self.components.items():
                item = Item(item_id)
                item_price = item.price(auction_list)
                price_list.append(item_price)
                total += item_price[2] * amount
            return Price(total, 'CRA')

    def get_cheapest_price(self, auction_list):
        prices = (
            self.get_npc_price(),
            self.get_ah_price(auction_list),
            self.get_crafting_price(auction_list)
        )
        prices = filter(None, prices)  # Filter out None types
        return min(prices)

    def get_components(self):
        return self.components
