dict_city = {"city": "Москва", "temperature": "20"}
print(dict_city["city"])
dict_city["temperature"] = int(dict_city["temperature"]) - 5
dict_city["temperature"] = str(dict_city["temperature"])
print(dict_city)
print(dict_city.get("Country"))
print(dict_city.get("Country","Россия"))
dict_city['date'] = '27.05.2019'
print(dict_city)
print(len(dict_city))
