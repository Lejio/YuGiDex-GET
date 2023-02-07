import requests
from yugiohprices import YuGiOhPrices
from ygoprodeck import YGOProDeck

if __name__ == "__main__":

    prices = YuGiOhPrices()
    prices.searchCardPrice_name("Tornado Dragon")
    
    # payload = {'name':'Tornado Dragon'}
    
    # prices = YGOProDeck()
    # prices.searchCard(payload=payload)
    # prices.searchCard(payload=payload)