import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
Weather_dict = json.loads(r.text)
w = (Weather_dict['current']['temp_c'])
t = (Weather_dict['current']['last_updated'])
say = wincom.Dispatch("SAPI.SpVoice")
say.speak(f"The current weather of {city} is {w} degrees and last updated is {t}")