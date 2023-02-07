import requests
from yugiohprices import YuGiOhPrices
from ygoprodeck import YGOProDeck

if __name__ == "__main__":

    # prices = YuGiOhPrices()
    # prices.searchCardPrice_name("Blue-Eyes White Dragon")
    
    payload = {'name':'Blue-Eyes White Dragon'}
    
    prices = YGOProDeck()
    prices.searchCard(payload=payload)
