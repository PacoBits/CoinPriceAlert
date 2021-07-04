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

a=0
while(True):
    cg = CoinGeckoAPI()
    data=cg.get_price(ids=COINTICKET, vs_currencies=VS_CURRENCIE)
    price=data[COINTICKET][VS_CURRENCIE]
    if float(price)<float(LIMITPRICE):
        response = requests.get('https://api.telegram.org/'+BOT+'/sendMessage?chat_id='+CHANNEL+'&text=Price '+COINTICKET +' lower than '+ str(LIMITPRICE)+ ' Value '+ str(price) )
    a=a+1        
    if a*(int(TIMESLEEP)/60/60/24)>1:
        response = requests.get('https://api.telegram.org/'+BOT+'/sendMessage?chat_id='+CHANNEL+'&text=Price  '+COINTICKET +' reminder limit '+ str(LIMITPRICE)+ ' Value '+ str(price) )
        a=0
    time.sleep(int(TIMESLEEP))

