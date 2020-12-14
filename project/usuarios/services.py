import googlemaps 
KEY='' 
gmaps=googlemaps.Client(key=KEY)

def get_coordinates(address,city):
    geocode_result=gmaps.geocode(str(address)+''+city)
    if len(geocode_result) > 0:
        result = list(geocode_result[0]['geometry']['location'].values())
        result.append(geocode_result[0])
        return result
    else:
        return 0