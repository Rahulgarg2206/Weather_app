try:
     from illusionanime import *
     from illusioncolor import *
     import requests
except:
     _ = os.system('pip install illusionanime illusioncolor requests' if os.name == 'nt' else 'pip3 install illusionanime illusioncolor requests')
from illusionanime import *
from illusioncolor import *
import requests

class logo:
    logo1=f"""
    {Red}</tool> {LightGreen}Weather App {Red}</tool>
{Grey} __      __               __  .__                  
/  \    /  \ ____ _____ _/  |_|  |__   ___________ 
\   \/\/   // __ \\__  \\   __\  |  \\_/ __ \_  __ \\
 \        /\  ___/ / __ \|  | |   Y  \  ___/|  | \/
  \__/\  /  \___  >____  /__| |___|  /\___  >__|   
       \/       \/     \/          \/     \/       
     {Red}</dev> {Blue}Rahul Garg{Red}</dev>
        """
    def clearscr():
        os.system('cls' if os.name=='nt' else 'clear')
        
    def print_logo():
        logo.clearscr()
        print(logo.logo1)
        
        
        
class mainfunction:
    def get_weather(city):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q": city}

        headers = {
            "X-RapidAPI-Key": "27e022f707msha54016e886de827p104c16jsn1adb33f4df47",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        return data

    def display_weather(data):
        if data and "error" not in data:
            city = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]
            writeway(f"{Purple}Weather in {city}, {country}:\n\n",0.01)
            writeway(f"{Yellow}Condition {Red}: {Cyan1}{condition}\n",0.01)
            writeway(f"{Yellow}Temperature {Red}: {Cyan1}{temp_c}°C\n",0.01)
            writeway(f"{Yellow}Humidity {Red}: {Cyan1}{humidity}%\n",0.01)
            writeway(f"{Yellow}Wind Speed {Red}: {Cyan1}{wind_kph} kph\n",0.01)
            
            # Prompt user to continue or exit
            choice = input("\nDo you want to check weather for another city? (yes/no): ")
            if choice.lower() == "no":
                return True  # Stop the application
            else:
                return False  # Continue the application
        else:
            print("City not found!")
            return False  # Continue the application if city not found

if __name__ == "__main__":
    logo.print_logo()
    print(f"{Cyan1}Welcome to the Weather App CLI!\n")
    
    # Run the application until user chooses to exit
    while True:
        city = input(f"{Yellow}Enter the city name {Red}: {White}")
        logo.print_logo()
        weather_data = mainfunction.get_weather(city)
        stop_application = mainfunction.display_weather(weather_data)
        if stop_application:
            break
