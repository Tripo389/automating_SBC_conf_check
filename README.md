
# SBC/ECB oracle autocheck param config local-policy

Palier à l'abascence de featur client via API 
Le projet à pour objectif d'automatiser la validité des numéros renseigner en black list via la local-policy.  
Le script dans sa versiont actuel ne permet qu'une verifiation et un log des entrées valides et des entrées non valides.  
L'interêt final sera de pouvoir palier aux erreurs humaines lors de l'implémentation de nouvelles rêgles de blocage.



### Tech 

**Client:** python3 

**Server:** oracle ESBC or ECB release 8.4 or higher

  
### Documentation

[Documentation API rest oracle](https://docs.oracle.com/en/industries/communications/session-border-controller/8.4.0/rest/index.html)  
[HLD automating_SBC_conf_check](https://github.com/Tripo389/automating_SBC_conf_check/blob/c6e861cb283ffedcb05f18d9a681570236357fb5/HLD%20automating_SBC_conf_check.docx)  
[User guide automating_SBC_conf_check](https://github.com/Tripo389/automating_SBC_conf_check/blob/d4a9af6f1553cffb248b870ca78504c098abdad8/User%20guide%20automating_SBC_conf_check.docx)  

  
### Environment py3

lyb:   
   -__requests__              *pour les requets via API*  
   -__re__                    *pour traitement string via regex*  
   -__xml.etree.ElementTree__ *pour parse xml*   
   -__phonenumbers__          *pour check NDI*  

  
  
