import requests
import json

class API:
    def __init__(self, ticker:str) -> None:
        self.ticker = ticker.upper()
        self.period = 5
        self.api_key:str = None
        self.base_url:str = None
        file = open("api.txt", "r")
        self.base_url:str = file.readline().rstrip()
        self.api_key:str = file.readline().rstrip() 
        file.close()

    def get_data(self, method:str=None, custum_url:str=None) -> json:
        try:
            try: 
                if custum_url: 
                    req = requests.get(custum_url)
                else:
                    req = requests.get("{}{}/{}?limit={}&apikey={}"
                        .format(self.base_url, method, self.ticker, self.period, self.api_key))
                res = req.json()
                if len(res)<1: raise NameError
            except requests.exceptions.RequestException as error:
                print("Error:", error)
            except NameError:
                print("Ticker do not exist")
            else: return res
            finally:
                req.close()
        except: 
            print("make sure you created the file <api.txt> and its content is in the right format.") 

    def get_income_statement(self) -> json: #
        return self.get_data(method="income-statement")
    
    def get_balance_sheet(self) -> json: #
        return self.get_data(method="balance-sheet-statement")
    
    def get_cash_flow(self) -> json: #
        return self.get_data(method="cash-flow-statement")

    # def get_enterprise_value(self) -> json:
    #     return self.get_data(custum_url="https://financialmodelingprep.com/api/v3/enterprise-values/{}?limit=40&apikey=e508676e6cd038b7bbe3ed9490104dee".format(self.ticker))
    
    def get_info(self) -> json:
        return self.get_data(method="profile")
    
    # def get_ratios(self) -> json:
    #     return self.get_data("ratios")

    def data(self) -> dict:
        return dict(income_statement=self.get_income_statement(), balance_sheet=self.get_balance_sheet(), cash_flow=self.get_cash_flow(), profile=self.get_info())
    
    
# if __name__=="__main__":
#     test = API("lly")
#     print(test.data())