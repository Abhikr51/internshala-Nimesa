import requests
import re
def print_menu():
   print("-------- Get Weather Details ---------")
   print("| 1. Get Temperature                 |")
   print("| 2. Get Wind Speed                  |")
   print("| 3. Get Pressure                    |")
   print("| 0. Exit                            |")
   print("--------------------------------------")

def get_date_time_input():
    try:
        #Taking User input
        date = input("Enter date (YYYY-MM-DD) [range - > 2019-03-27 - 2019-03-31]: ").strip()
        time = input("Enter time (HH)[range -> 01-24]: ").strip()
        dt_txt = date + " " + time +":00:00"
        regex = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
        if re.match(regex , dt_txt):
            return dt_txt
        else:
            raise Exception("Invalid date or time sequence")
    except:
        print("Invalid date or time sequence")
        return False
def get_date_num_from_date_txt(date_txt):
    date_text_parts = date_txt.split(" ")
    date_num = "".join(date_text_parts[0].split("-")) + date_text_parts[1].split(":")[0]
    return int(date_num)
def fetchApi(url):
    #Api Calling
    print("Fetching Data from weather API ....")
    response = requests.get(url)
    data = response.json()
    indexed_arr = []
    for item in data["list"]:
        val = get_date_num_from_date_txt(item["dt_txt"])
        indexed_arr.append(val)
    print("Now program is ready")
    return (data, indexed_arr)

def binary_search_to_find_info(indexed_arr , date_text):
    val = get_date_num_from_date_txt(date_text)
    low = 0
    high = len(indexed_arr) - 1
    mid = 0
    while low <= high:

        mid = (high + low) // 2

        if indexed_arr[mid] < val:
            low = mid + 1
        elif indexed_arr[mid] > val:
            high = mid - 1
        else:
            return mid
    return -1





try:
    url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
    (data , indexes) = fetchApi(url)
    
    
    while(True):
        print_menu()
        choice = input("Choose a option : ")
        if choice == "1":
           #Get temperature
           date_time_text = get_date_time_input()
           if(date_time_text):
                index = binary_search_to_find_info(indexes,date_time_text)
                if index != -1:   
                    print(f"Temperature : {data['list'][index]['main']['temp']}")
                else:
                    print("Not Found")
        elif choice == "2":
           #Get wind speed
           date_time_text = get_date_time_input()
           if(date_time_text):
                index = binary_search_to_find_info(indexes,date_time_text)
                if index != -1:   
                    print(f"Wind Speed : {data['list'][index]['wind']['speed']}")
                else:
                    print("Not Found")
        elif choice == "3":
           #Get pressure
           date_time_text = get_date_time_input()
           if(date_time_text):
                index = binary_search_to_find_info(indexes,date_time_text)
                if index != -1:   
                    print(f"Pressure : {data['list'][index]['main']['pressure']}")
                else:
                    print("Not Found")
        elif choice == "0":
           break
        else:
           print("Invalid Output Please try Again")

except Exception as e:
  print(str(e))
    





