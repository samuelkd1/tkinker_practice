from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("weather app")
root.geometry("400x80")

# create Zipcode Lookup Function
def ziplookup():
	#zipcode.get()
	#zipcodeLabel = Label(root, text = zipcode.get())
	#zipcodeLabel.grid(row = 1, column = 0, columnspan = 2)

	# now to bring in the api

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=E00BA9FB-AC4A-4AEE-A02B-D57C97C832ED")

	try:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode.get() + "&distance=25&API_KEY=E00BA9FB-AC4A-4AEE-A02B-D57C97C832ED")
		api = json.loads(api_request.content)
		city = api[0]["ReportingArea"]
		quality = api[0]["AQI"]
		category = api[0]["Category"]["Name"]

		if category == "Good":
			weather_colour = "#0C0"

		elif category == "Moderate":
			weather_colour = "#FFFF00 "

		elif category == "Unhealthy":
			weather_colour = "FF0000"

		elif category == "Very Unhealthy":
			weather_colour = "#990066 "

		elif category == "Hazardous":
			weather_colour = "#660000 "

		else:
			weather_colour = "ff9900 "

		root.configure(background = weather_colour)

		# since we only want the first bit we will only call this item 
		myLabel = Label(root, text = f"{city} Air quality:{quality} {category}", font = ("Arial", 20), background = weather_colour)
		myLabel.grid(row = 1, column = 0, columnspan = 2)

	except Exception as e:
		api = "Error..."


zipcode = Entry(root)
zipcode.grid(row = 0, column = 0, stick = W+E+N+S)

zip_btn = Button(root, text = "Lookup Zipcode", command = ziplookup)
zip_btn.grid(row = 0, column = 1, stick = W+E+N+S)

root.mainloop()