import requests
import re
import xml.etree.ElementTree as ET
import phonenumbers
from phonenumbers import carrier, timezone, geocoder

sbc1ip = '192.168.56.10'
url_tok = 'https://192.168.56.10/rest/v1.1/auth/token'
headers = {
    'Accept': 'application/xml',
}

response_tok = requests.post(url_tok, headers=headers, verify=False, auth=('admin', 'Ytreytre'))
#print(response_tok.text)

PATTERN_TOK = re.search('<accessToken>(.+?)</accessToken>', response_tok.text).group(1)
#tok_auth = re.search(PATTERN_TOK, response.text)

#print(PATTERN_TOK)

headers = { "Accept":"application/xml", "Authorization":"Bearer " + PATTERN_TOK}
url_poli = "https://" + sbc1ip + "/rest/v1.1/configuration/configElements?elementType=local-policy"
resp = requests.get(url_poli, headers=headers, verify=False)
xmltxt = resp.content

root = ET.fromstring(xmltxt) # on u

verif_number = []
valid_number = []
unvalid_number = []

for element in root.find('data'):

    # Boul pour filtrage

    isblocage = False

    # Iterate over attribute

    for attribute in element.iter('attribute'):

        # Get attribute name

        name = attribute.find('name').text

        # Retrieve from-adress values

        if name == "from-address":

            for child in attribute.iter('value'):

                verif_number.append(child.text)

        # Check the description

        if name == "description":
            attrib_from_address = re.findall(r"^\w+", attribute.find('value').text)
            for blocage in attrib_from_address:
                isblocage = blocage == "blocage"

    if isblocage:
        print(verif_number)
        for numbers in verif_number:
            valid = phonenumbers.is_valid_number(phonenumbers.parse(numbers))
            print(valid)
            if valid == True:
                valid_number.append(numbers)
                print(valid_number)
            else:
                unvalid_number.append(numbers)
                print(unvalid_number)
