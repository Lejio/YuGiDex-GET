import requests

class YGOProDeck:
    
    def __init__(self) -> None:
        
        self.URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
        # self.__GET_CARD_PRICES_NAME = "get_card_prices/"
        # self.__GET_CARD_PRICES_TAG = "get_card_prices_tag/"
        # self.__PRICE_HISTORY = "price_history/"
        # self.__SET_DATA = "set_data/"
        # self.__CARD_SETS = "card_sets"
        # self.__CARD_SUPPORT = "card_support/"
        # https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Tornado%20Dragon

        
        
    def searchCard(self, payload: dict):
                
        # rsp = requests.get(url=self.URL, params=payload)
        rsp = requests.get(url="https://db.ygoprodeck.com/api/v7/cardinfo.php", params=payload)
        
        if str(rsp.status_code) == "200":
            print("Response recieved.")
        else:
            print("Oops! Something went wrong.")
            print(rsp.url)
            print(rsp.status_code)
            exit()
        
        data = rsp.json()
        
        # print(data)
        for r in data['data'][0]['card_sets']:
            # print(data['card_sets'][r])
            # print(r['card_sets'])
            print(r)
            
        for r in data['data'][0]['card_prices']:
            
            print(r)
        
        
    # def __stringProcessor(self, name:str) -> str:
        
    #     return name.replace(" ", "%20")