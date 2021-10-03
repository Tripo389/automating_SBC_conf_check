
# SBC/ECB oracle autocheck param config local-policy

Palier à l'abascence de featur client via API 
Le projet à pour objectif d'automatiser la validité des numéros renseigner en black list via la local-policy. 



### Tech 

**Client:** python3 

**Server:** oracle ESBC or ECB release 8.4 or higher

  
### Documentation

[Documentation API rest oracle](https://docs.oracle.com/en/industries/communications/session-border-controller/8.4.0/rest/index.html)
[HLD automating_SBC_conf_check](https://github.com/Tripo389/automating_SBC_conf_check/blob/c6e861cb283ffedcb05f18d9a681570236357fb5/HLD%20automating_SBC_conf_check.docx)

  
### Environment py3

lyb:   
   -__requests__              *pour les requets via API*  
   -__re__                    *pour traitement string via regex*  
   -__xml.etree.ElementTree__ *pour parse xml*   
   -__phonenumbers__          *pour check NDI*  

  
  
