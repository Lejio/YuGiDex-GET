import requests

class YuGiOhPrices:
    
    def __init__(self) -> None:
        
        self.URL = "https://yugiohprices.com/api/"
        self.__GET_CARD_PRICES_NAME = "get_card_prices/"
        self.__GET_CARD_PRICES_TAG = "get_card_prices_tag/"
        self.__PRICE_HISTORY = "price_history/"
        self.__SET_DATA = "set_data/"
        self.__CARD_SETS = "card_sets"
        self.__CARD_SUPPORT = "card_support/"
        
        
    def searchCardPrice_name(self, name:str):
        
        URL = self.URL + self.__GET_CARD_PRICES_NAME + self.__stringProcessor(name=name)
        
        rsp = requests.get(url=URL)
        
        if str(rsp.status_code) == "200":
            print("Response recieved.")
        else:
            print("Oops! Something went wrong.")
            print(rsp.status_code)
            exit()
        
        data = rsp.json()
        
        print(data)
        for r in data['data']:
            print(r['name'] + " " + r['print_tag'] + " " + r['rarity'])
        
        
    def __stringProcessor(self, name:str) -> str:
        
        return name.replace(" ", "%20")