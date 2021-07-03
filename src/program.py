from pycoingecko import CoinGeckoAPI
import requests,time,os
from dotenv import load_dotenv




load_dotenv()
COINTICKET=os.getenv("COINTICKET")
VS_CURRENCIE=os.getenv("VS_CURRENCIE")
TIMESLEEP=os.getenv("TIMESLEEP")
LIMITPRICE=os.getenv("LIMITPRICE")
BOT=os.getenv("BOT")
CHANNEL=os.getenv("CHANNEL")


while(True):
    cg = CoinGeckoAPI()
    data=cg.get_price(ids=COINTICKET, vs_currencies=VS_CURRENCIE)
    price=data[COINTICKET][VS_CURRENCIE]
    if float(price)<float(LIMITPRICE):
        print("alert")
        response = requests.get('https://api.telegram.org/'+BOT+'/sendMessage?chat_id='+CHANNEL+'&text=Price lower than '+ str(LIMITPRICE)+ ' Value '+ str(price) )
    else:
        print("Correct")
    time.sleep(int(TIMESLEEP))

