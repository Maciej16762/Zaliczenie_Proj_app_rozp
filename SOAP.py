from zeep import Client

def get_countries():
    wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    client = Client(wsdl)
    result = client.service.ListOfCountryNamesByName()
    for country in result:
        print(f"{country.sISOCode} - {country.sName}")

def get_country_flag(country_iso):
    wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    client = Client(wsdl)
    flag_url = client.service.CountryFlag(country_iso)
    print(f"Flaga {country_iso}: {flag_url}")

get_countries()
get_country_flag('PL')  # Przykład dla Polski