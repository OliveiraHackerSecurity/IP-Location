 #!usr/bin/python3 
 ​import​ ​requests 
 ​from​ ​time​ ​import​ ​sleep 
 ​import​ ​os 
 ​#Iniciando vamos lá!! 
 ​#me segue no github https://github.com/OliveiraHackerSecurity 
 ​#cores da depressão 
 ​vd​=​'​\033​[32m' 
 ​am​=​'​\033​[33m' 
 ​vm​=​'​\033​[31m' 
 ​az​=​'​\033​[36m' 
 ​ng​=​'​\033​[1m' 
 ​f​=​'​\033​[m' 
 ​lz​=​'​\033​[34m'​    
 ​#api ip 
 ​def​ ​ip​():   
 ​        ​ip1​=​input​(​f'​{​vm​}​--> ​{​f​}​{​az​}​(fonte IPgeolocation)​{​f​}​ ​\n​{​vm​}​--> ​{​f​}​{​az​}​( ip )​{​f​}​ ​{​am​}​-->​{​f​}​ '​) 
 ​        ​url1​ ​=​ ​"https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}"​.​format​(​ip1​) 
 ​        ​res​ ​=​ ​requests​.​get​(​url1​) 
 ​        ​req​=​res​.​json​() 
 ​        ​br​=​"​\n​{}[@] ip localizado com sucesso ​\n​[@] dados abaixo{}{} ​\n​->[ip]:{}​\n​->[código continental]:{}​\n​->[nome do continente]:{}​\n​->[código do seu país citado 2]:{}​\n​->[código do país 3]:{}​\n​->[nome do país]:{}​\n​->[capital do país]:{}​\n​->[prov do estado]:{}​\n​->[distrito]:{}​\n​->[cidade]:{}​\n​->[CEP]:{}​\n​->[latitude]:{}​\n​->[longitude]:{}​\n​->[is_eu]:{}​\n​->[código da chamada]:{}​\n​->[país tld]:{}​\n​->[languages]:{}​\n​->[bandeira representada país]:{}​\n​->[ geoname_id ]:{}​\n​->[ isp ]:{}​\n​->[continente]:{}​\n​->[organização]:{}​\n​->[moeda]:{}​\n​->[fuso horário]:{}​\n​\033​[m"​.​format​(​ng​,​f​,​vd​,​req​[​'ip'​],​req​[​'continent_code'​],​req​[​'continent_name'​],​req​[​'country_code2'​],​req​[​'country_code3'​],​req​[​'country_name'​],​req​[​'country_capital'​],​req​[​'state_prov'​],​req​[​'district'​],​req​[​'city'​],​req​[​'zipcode'​],​req​[​'latitude'​],​req​[​'longitude'​],​req​[​'is_eu'​],​req​[​'calling_code'​],​req​[​'country_tld'​],​req​[​'languages'​],​req​[​'country_flag'​],​req​[​'geoname_id'​],​req​[​'isp'​],​req​[​'connection_type'​],​req​[​'organization'​],​req​[​'currency'​],​req​[​'time_zone'​]) 
 ​        ​print​(​br​) 
 ​        ​exit​() 
  
 ​{​f​}​{​vd​}​by @OliveiraHackerSecurity{​f​} 
 ​ ​{​az​}​{​f​}​                                     
 ​{​vm​}​  ​{​vd​} 
 
 ​{​f​}​    
 ​  """​) 
 ​os​.​system​(​'clear'​); 
 ​def​ ​menu​(): 
 ​    ​print​(​f""" 
 ​{​az​}​             
 
 ​                              @OliveiraHackerSecurity 
  
 ​{​f​}​{​am​}​ --> ​{​f​}​{​vm​}​escolha uma oopção {​f​} 
 ​  
 ​                             
 ​{​az​}​(​{​f​}​{​lz​}​01​{​f​}​{​az​}​)​{​f​}​ ​{​vd​}​localizador de IP​{​f​} 
   
  
 ​{​az​}​(​{​f​}​{​lz​}​03​{​f​}​{​az​}​)​{​f​}​{​vm​}​ sair do script{​f​} 
 ​    """​) 
 ​try​: 
 ​    ​menu​() 
 ​    ​inpu​=​str​(​input​(​f'​{​am​}​+-+->​{​f​}​ '​)) 
 ​except​ ​KeyboardInterrupt​: 
 ​    ​exit​() 
 ​except​: 
 ​    ​print​(​f'​{​vm​}​* [!!!] Digite o valor correto ​{​f​}​'​) 
 ​try​:     
 ​    ​if​ ​inpu​==​'1'​ ​or​ ​inpu​==​'01'​:    
 ​        ​os​.​system​(​'clear'​);​ban​();​ip​() 
 ​    ​elif​ ​inpu​==​'2'​ ​or​ ​inpu​==​'02'​: 
 ​        ​os​.​system​(​'clear'​);​ban​();​yt​() 
 ​    ​elif​ ​inpu​==​'3'​ ​or​ ​inpu​==​'03'​: 
 ​        ​os​.​system​(​'clear'​) 
 ​        ​print​(​f""" ​{​vm​} 
 ​           a mimir 
 ​
 ​{​f​} 
 ​"""​) 
 ​        ​exit​() 
 ​    ​else​: 
 ​        ​print​(​f'​{​vm​}​- [!?!] digite uma opção valida [!?!] ​{​f​}​'​);​exit​()                                                                                           
 ​except​: 
 ​    ​exit​()
