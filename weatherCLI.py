import requests
import json
import os
from colorama import Fore, Style, Back
from datetime import datetime

key = "a86184fd83be486db83120827240904"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    # Print the logo
    logo = r"""
    
    
__        __         _   _                ____ _     ___ 
\ \      / /__  __ _| |_| |__   ___ _ __ / ___| |   |_ _|
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| |   | |    | | 
  \ V  V /  __/ (_| | |_| | | |  __/ |  | |___| |___ | | 
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|   \____|_____|___|
                                                        
                                                      linux v1.0         
  """
    print(f"{Fore.GREEN}{logo}{Style.RESET_ALL}")
    print(f"{Fore.RED}\n\t\t█▒▓­░⡷⠂ DEVELOPED BY FADED ⠐⢾░▒▓█{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}\n\t\t🏴 彡 https://t.me/cyberhood  彡 🏴 {Style.RESET_ALL}")
    print(f"{Back.RED}\n\t ★ 彡 https://github.com/anonfaded/weatherCLI 彡 ★ {Style.RESET_ALL}\n\n") 

def fetch_weather_data(city):
    # Fetch current weather data
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=yes"
    weather_response = requests.get(weather_url)
    weather_data = json.loads(weather_response.text)

    # Extract temperature, cloud, and visibility data from the current weather data
    temperature = weather_data["current"]["temp_c"]
    cloud = weather_data["current"]["cloud"]
    visibility = weather_data["current"]["vis_km"]
    air_quality = weather_data["current"]["air_quality"]["us-epa-index"]

    # Fetch sunrise and sunset times from the Astronomy API
    astronomy_url = f"http://api.weatherapi.com/v1/astronomy.json?key={key}&q={city}"
    astronomy_response = requests.get(astronomy_url)
    astronomy_data = json.loads(astronomy_response.text)

    # Extract sunrise and sunset times from the Astronomy API response
    sunrise = astronomy_data["astronomy"]["astro"]["sunrise"]
    sunset = astronomy_data["astronomy"]["astro"]["sunset"]

    # Fetch local time zone information
    timezone_url = f"http://api.weatherapi.com/v1/timezone.json?key={key}&q={city}"
    timezone_response = requests.get(timezone_url)
    timezone_data = json.loads(timezone_response.text)

    # Extract time zone id and local time from the Time Zone API response
    timezone_id = timezone_data["location"]["tz_id"]
    local_time = timezone_data["location"]["localtime"]
    
    # Convert local time to AM/PM format
    local_time = datetime.strptime(local_time, '%Y-%m-%d %H:%M')
    local_time = local_time.strftime('%I:%M %p')

    return temperature, cloud, visibility, air_quality, sunrise, sunset, timezone_id, local_time

def print_weather_info(city, temperature, cloud, visibility, air_quality, sunrise, sunset, timezone_id, local_time):
    clear_terminal()
    header()  # Print header
    print(f"{Fore.GREEN}Weather information for {city}:{Style.RESET_ALL}")
    print(f"  - Temperature:   {Fore.YELLOW}{temperature}°C{Style.RESET_ALL}")
    print(f"  - Cloud cover:   {Fore.YELLOW}{cloud}%{Style.RESET_ALL}")
    print(f"  - Visibility:    {Fore.YELLOW}{visibility} km{Style.RESET_ALL}")
    print(f"  - Air Quality:   {Fore.YELLOW}{air_quality}{Style.RESET_ALL}")
    print(f"  - Sunrise:       {Fore.YELLOW}{sunrise}{Style.RESET_ALL}")
    print(f"  - Sunset:        {Fore.YELLOW}{sunset}{Style.RESET_ALL}")
    print(f"  - Timezone ID:   {Fore.YELLOW}{timezone_id}{Style.RESET_ALL}")
    print(f"  - Local Time:    {Fore.YELLOW}{local_time}{Style.RESET_ALL}")

def main():
    while True:
        clear_terminal()
        header()  # Print header
        city = input(f"{Fore.GREEN}Enter the name of city {Fore.LIGHTBLACK_EX}(Enter q to exit)\n{Fore.BLUE}>>> {Style.RESET_ALL}")
        
        if city == '':
            print(f"{Fore.RED}\tPlease enter a city name.{Style.RESET_ALL}")
            input(f"\n{Fore.BLUE}Press Enter to continue...")
            continue
        
        if city == 'q':
            clear_terminal()
            header()
            print(f"{Fore.RED}\n\tQuitting, Goodbye!\n{Style.RESET_ALL}")
            break

        try:
            temperature, cloud, visibility, air_quality, sunrise, sunset, timezone_id, local_time = fetch_weather_data(city)
            print_weather_info(city, temperature, cloud, visibility, air_quality, sunrise, sunset, timezone_id, local_time)
            input("\nPress Enter to continue...")
        except KeyError:
            print(f"{Fore.RED}\n\tCity not found. Please enter a valid city name.\n{Style.RESET_ALL}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
