# import discord
# from secrets import discord_bot_token
from access import Access
from item import Item
from fakedb import fakedb

# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run(discord_bot_token)

if __name__ == '__main__':
    access = Access()

    # 1
    # Obtain AH prices
    auctions = access.get_auctions()

    # 1.5
    # Find out which items are profitable to craft
    items_to_craft = set()
    for item_id, item_json in fakedb.items():
        print(item_id)
        print(item_json)
        if item_json['components'] is None:
            continue
        print('lebork')
        item_obj = Item(item_id)
        price = item_obj.price(auctions)
        if price[1] == 'CRA':
            items_to_craft.add(item_obj)


    print(items_to_craft)



    # 2
    # calculate the amount of ingredients that are below the "break even price'


    # 2.1 calculate the "break even price" (BEP)

