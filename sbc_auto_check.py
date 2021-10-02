#Check local policy with API
#Python 3
#OS Oracle 8.4
#Version 1.3
#Date 09/2021
#Created by Emmanuel SUEUR

import requests
import re
import xml.etree.ElementTree as ET
import phonenumbers
import time


logprocessing = open("auto_check_policy.log", "w")

sbc1ip = '192.168.56.10' # Adresse IP sbc
url_tok = 'https://192.168.56.10/rest/v1.1/auth/token' # Url pour acquisiont token

#Création du headers
headers = {
    'Accept': 'application/xml',
}

response_tok = requests.post(url_tok, headers=headers, verify=False, auth=('admin', 'Ytreytre'))


PATTERN_TOK = re.search('<accessToken>(.+?)</accessToken>', response_tok.text).group(1)

if not (PATTERN_TOK):

    # Check acquision token

    print("error get token API check AUTH")
    logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + "error get token API check AUTH" + ":" +"\n")

else:
    print("Token acquisition OK")
    logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + "Token acquisition OK" + ":" + "\n")

# Header to get configuration
headers = {
    "Accept":"application/xml",
    "Authorization":"Bearer " + PATTERN_TOK,
}

url_poli = "https://" + sbc1ip + "/rest/v1.1/configuration/configElements?elementType=local-policy"
resp = requests.get(url_poli, headers=headers, verify=False)
xmltxt = resp.content

# List implementation

verif_number = []
valid_number = []
unvalid_number = []

#Parse xml
root = ET.fromstring(xmltxt)

for element in root.find('data'):


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

            # white space correction
            attrib_from_address = re.findall(r"^\w+", attribute.find('value').text)

            for blocage in attrib_from_address:
                isblocage = blocage == "blocage"



    if isblocage:

        # Implementation list verif number valid/unvalid

        for numbers in verif_number:

            valid = phonenumbers.is_valid_number(phonenumbers.parse(numbers))

            if valid == True:
                valid_number.append(numbers)

                #print(valid_number)
            else:
                unvalid_number.append(numbers)
                #print(unvalid_number)


#Création des fichiers de log
verifFile = open("ValidNumber"+"_"+time.strftime("%Y%m%d-%H""h""%M""m""%S")+".txt", "w+")
verifFile.write("NDI:DATE\n")
unvalidFile = open("UnvalidNumber"+"_"+time.strftime("%Y%m%d-%H""h""%M""m""%S")+".txt", "w+")
unvalidFile.write("NDI:DATE\n")

if not (valid_number):

    # Vérification list pour création fichier
    print("error empty valid number")
    logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + ":" + "error empty valid number"+ "\n")

else:
    print("RAS valid number")
    logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + ":" + "RAS valid number" + "\n")


for number in valid_number:

    # Creat txt to log valid

    verifFile.write(number +":"+ time.strftime("%Y%m%d-%H""h""%M")+"\n")

logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + ":" + "Check valid" + "\n")


for number in unvalid_number:

    # Creat txt to log unvalid number

    unvalidFile.write(number + ":"+ time.strftime("%Y%m%d-%H""h""%M")+"\n")

logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + ":" + "Check unvalid" + "\n")

#End
print("fin de traitement")
logprocessing.write(time.strftime("%Y%m%d-%H""h""%M""m""%S") + ":" + "fin de traitement" + "\n")