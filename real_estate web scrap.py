import requests
import urllib3
import json
import requests
import pandas as pd
import openpyxl


# The code below requests user input to look into the area of interest of real-estate property
url = "https://realtor.p.rapidapi.com/properties/v2/list-sold"
city = input("Enter city: " )
state = input("Enter state: "  )  
address = input ('Enter address: ' )
try:
    zipcode = int(input('Enter zipcode: ' ))
    radius = int(input('Radius of houses sold: ' ))
    sqft = int(input('Enter square feet of the property: '  ))
    baths = int(input('How many baths you want to look for: ' ))
    beds = int(input('How many beds you want to look for: ' )) 
except ValueError:
    print("Enter only numerical values for zipcode, radius, square feet, baths, or bed fields")

def find_zips(p_code,distance):
    url2 = "https://redline-redline-zipcode.p.rapidapi.com/rest/multi-radius.json/"+str(distance)+"/mile"

    payload2 = "zip_codes="+str(p_code)
    headers2 = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "34215c9ea5msh4ec3d54439862cdp192091jsn6415936ac701",
    'x-rapidapi-host': "redline-redline-zipcode.p.rapidapi.com"
    }

    response2 = requests.request("POST", url2, data=payload2, headers=headers2)
    [zip_stats] = [x['zip_codes'] for x in response2.json()['responses']]
    return zip_stats



def query_data(bath, bedrooms,p_code, sq_feet, c, s, zip_func, distance=1): # this function querys and returns values of real estate properties comparable to the area of interest.

    lm = 200
    
    querystring = {"radius":str(distance), 'baths_min':str(bath), 'beds_min': str(bedrooms),"postal_code":str(p_code),'sqft_min': str(sq_feet-500),"sort":"sold_date",'sqft_max':str(sq_feet+ 500),"city":str(c),"offset":"0","state_code":str(s),"limit":str(lm)}

    headers = {
    'x-rapidapi-host': "realtor.p.rapidapi.com",
    'x-rapidapi-key': "34215c9ea5msh4ec3d54439862cdp192091jsn6415936ac701"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = 0
    data = {}
    prices = []
    address_location = []
    property_type = []
    post_code = []
    city = []
    state = []
    status = []
    size = []

    
    for x in response.json()['properties'][0:50]:
        if x['address']['postal_code'] in zip_func:
            property_type.append(x['prop_type'])
            prices.append(x['price'])
            address_location.append(x['address']['line'])
            post_code.append(x['address']['postal_code'])
            city.append(x['address']['city'])
            state.append(x['address']['state_code'])
            status.append(x['client_display_flags']['presentation_status'])
            size.append(x['building_size']['size'])
            data['Prices']= (prices)
            data['Addresses'] = (address_location)
            data['Type of Property'] = (property_type)
            data['Zipcode'] = (post_code)
            data['City'] = (city)
            data['state'] = (state)
            data['Property Status'] = (status)
            data['Size in sq.ft'] = (size)
    
   
    return data

def compose_dataframe(info): # function stores all of the retrieved data of housing information into an excel spreadsheet
    df = pd.DataFrame(data=info)
    df['Average House Price'] = df['Prices'].mean(axis=0)
    df['Average House Price'] = df['Average House Price'].astype(int).drop_duplicates()
    df.to_excel (r'''C:\\Users\\Jacks\\OneDrive\\Desktop\\Python projects\\Api Excel_output.xlsx''', index = False, header=True)
    return df

if __name__ == "__main__":   
    distance = radius
    bath = baths
    bedrooms = beds
    p_code = zipcode
    sq_feet = sqft
    c = city
    s = state
    zip_data = find_zips(p_code,distance)
    zip_func = zip_data
    info = query_data(bath, bedrooms, p_code, sq_feet, c, s, zip_func, distance=1)

    print(zip_data)
    print(compose_dataframe(info))

        
