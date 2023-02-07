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
        
        # print(data)
        for r in data['data']:
            try:
                print(r['name'] + " " + r['print_tag'] + " " + r['rarity'] + " " + str(r['price_data']['data']['prices']['low']))
            except:
                print(r)
        
        
    def __stringProcessor(self, name:str) -> str:
        
        return name.replace(" ", "%20")
    
    # {'name': 'Yu-Gi-Oh! Power of Chaos: Kaiba the Revenge promotional cards', 'print_tag': 'PCK-001', 'rarity': 'Prismatic Secret Rare', 'price_data': {'status': 'success', 'data': {'listings': [], 'prices': {'high': 199.98, 'low': 14.99, 'average': 54.87, 'shift': -0.00254499181966915, 'shift_3': 0.0159229772264395, 'shift_7': 0.00476103277787951, 'shift_21': -0.0186013235557145, 'shift_30': -0.0870216306156406, 'shift_90': 0.0399924184988628, 'shift_180': -0.387884872824632, 'shift_365': -0.466556484542096, 'updated_at': '2023-02-07 02:46:46 -0500'}}}}