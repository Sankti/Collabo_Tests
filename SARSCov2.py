import requests

response = (requests.get("https://corona.lmao.ninja/countries")).json()

def find_country_data(country):
    global response
    for state_dict in response:
        if country == state_dict["country"]:
            my_state_dict = state_dict
            return my_state_dict


def display_count_stats(state_dict):
    print("Country: " + str(state_dict["country"]))
    print("Total cases to date: " + str(state_dict["cases"]))
    print("New cases today: " + str(state_dict["todayCases"]))
    print("Total deaths: " + str(state_dict["deaths"]))
    print("Deaths today only: " + str(state_dict["todayDeaths"]))
    print("Total recovered: " + str(state_dict["recovered"]) + "\n")


def covid_status():
    selection = None
    while selection != "Q":
        try:
            selection = (input("Please specify country: \n\n")).title()
            display_count_stats(find_country_data(selection))
            selection = input("""Press enter to select another country
or press Q to quit the program: \n\n""").upper()
        except:
            print("Sorry, wrong input, try again: \n")

covid_status()










