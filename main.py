import requests
from yugiohprices import YuGiOhPrices

if __name__ == "__main__":

    prices = YuGiOhPrices()
    prices.searchCardPrice_name("Blue-Eyes White Dragon")