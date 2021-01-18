from selenium import webdriver
from random import randint
import time;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By







# Openning the Google
driver = webdriver.Chrome("./chromedriver.exe");

# Getting the whatsapp page
driver.get('https://web.whatsapp.com/');




input("Press Enter after scan QR code and enter to the group");






# getting the last message div
last_message = driver.find_elements_by_class_name('_3zb-j')[-1];

# getting the span mensagem
span_message = last_message.find_elements_by_tag_name("span")[0];

# getting the mensagem
message = driver.execute_script("return arguments[0].innerText;", span_message);



# getting message input (to write a message)
message_input = driver.find_element_by_class_name('_1Plpp');





# getting the button to send message
send_message = driver.find_elements_by_class_name('weEq5')[1];



# Ban confirmation will start enabled
ban_confirmation = True;






# Infinite loop to verify the last message all the time
for i in range(9999999999999999999):

    # getting the last message div
    last_message = driver.find_elements_by_class_name('_3zb-j')[-1];

    # getting the span mensagem
    span_message = last_message.find_elements_by_tag_name("span")[0];


    # getting the mensagem
    message = driver.execute_script("return arguments[0].innerText;", span_message);



    # If the message is: help
    if(message.lower() == "/help"):

        # Typing at the message input (need this: 'Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎"' and the next line to brek a row)
        message_input.send_keys("*Comands list:*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");

        # Break row
        message_input.send_keys(Keys.SHIFT, Keys.ENTER);




        message_input.send_keys("1- /Rules", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("2- /Ban @'nome_do_contato/número'", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);


        message_input.send_keys("3- /Ban confirmation   (para desativar ou ativar permissão do líder)", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("Também existe uns comandos secretos...");


        # Sending the message
        send_message.click();
    
    



    elif(message.lower() == "/rules"):
        message_input.send_keys("*REGRAS*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎"); 

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Stickers (figurinhas) só com moderação*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎"); 

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Proibido*⬇️", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎"); 

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Divulgações (somente com autorização dos administradores)*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎"); 
        
        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*BAN IMEDIATO*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Textos muito grandes e sem lógica nenhuma*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");
        
        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Conteúdo relacionado a pornografia, zoofilia e etc...*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");
        
        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Links externos sem permissão*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");
        
        message_input.send_keys(Keys.SHIFT, Keys.ENTER);




        message_input.send_keys("*Reclamações ou dúvidas falar com os administradores*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");
        
        message_input.send_keys(Keys.SHIFT, Keys.ENTER);



        message_input.send_keys("*Seja ativo*");
        



        send_message.click();







    elif(message.lower()[0 : 4] == "/ban" and message.lower() != "/ban confirmation"):



        # Getting just the user name
        message = message.lower().replace('/ban','');

        message = message.replace('@','');

        message = message[1:];


        # Function to remove a person from a whatsapp group
        def RemovePerson(message):
                    
            # Typing this message
            message_input.send_keys("*REMOVING " + message + " FOR EVER*");

            # Sending the message
            send_message.click();



            # Getting the message at lower
            message = message.lower();




            # Finding the group header
            topHeader = driver.find_element_by_class_name('_2y17h');

            # Clicking at group header
            topHeader.click();

        
            # This is the 'directory' to the name of the user in JavaScript
            # document.getElementsByClassName("_2EXPL _3xj48")[0].children[1].children[0].children[0].innerText;

            # time.sleep(1);


            # getting span to see how many memberss the group have
            member_quantid = driver.find_elements_by_class_name("_1sYdX")[2];

            # getting the text
            member_quantid = driver.execute_script("return arguments[0].innerText;", member_quantid)

            # Removing participants from the text
            member_quantid = member_quantid.replace('participants', '');

            # Removing blank characters
            member_quantid = member_quantid.replace(' ', '');


            # If the group have 11 or more than 11 members
            if(int(member_quantid) >= 11):

                # Getting the arrow to see more members
                arrow_div = driver.find_elements_by_class_name("_1jJLh")[2];

                # Clicking it
                arrow_div.click();

                




            # Div that have the members
            principal_div_user = driver.find_elements_by_class_name('_3xj48');





            # Loop to get all the group members
            for i in range( 2, len(principal_div_user)):

                div_user = principal_div_user[i].find_elements_by_class_name('_3j7s9')[0];

                div_user_name_container = div_user.find_elements_by_class_name('_2FBdJ')[0];

                div_user_name = div_user_name_container.find_elements_by_class_name('_25Ooe')[0];

                span_user_name_container = div_user_name.find_elements_by_class_name('_3TEwt')[0];

                
                span_user_name = span_user_name_container.find_elements_by_class_name('_1wjpf')[0];

                
                name = driver.execute_script("return arguments[0].innerText;", span_user_name);

                
                print(name.lower());

                
                print(message)


                
                if(name.lower() == message):
                    print("REMOVING " + message + "----" + name);

                    # getting actions
                    actions = ActionChains(driver);

                    # Going to the member
                    driver.execute_script("arguments[0].scrollIntoView();", span_user_name)

                    # Moving the mouse to the element
                    actions.move_to_element(span_user_name).perform();


                    # Clicking at the arrow to see member options
                    icon_for_open_ban_modal = driver.find_element_by_class_name('ZR5SB');

                    
                    icon_for_open_ban_modal.click();


                    # Getting members options
                    modal_btns = driver.find_elements_by_class_name("Pm0Ov");


                    # Loop to get all the options
                    for i in range(len(modal_btns)):

                        # Getting the button text
                        ban_btn = driver.execute_script("return arguments[0].innerText;", modal_btns[i]);


                        # If is the button that remove the member
                        if(ban_btn == "Remove"):
                        
                            # Clicking it
                            modal_btns[i].click();
                            # actions.move_to_element(modal_btns[i]).perform();

                            # Getting confirm btn
                            remove_btn = driver.find_element_by_class_name("PNlAR");

                            
                            remove_btn.click();

                            # Getting the button to close the header
                            close_ban_btn = driver.find_element_by_class_name("_1aTxu");
                            
                            close_ban_btn.click();
                            




        if(ban_confirmation == True):
    
            confimation = input("Want to remove someone?  Y/N");

            while(confimation.lower() != "y" and confimation.lower() != "n"):
                confimation = input("Error... Want to remove someone?  Y/N");

            
            if(confimation.lower() == "y"):
                RemovePerson(message);
                

            else:
                message_input.send_keys("ERROR... permission denied");

                send_message.click();


        

        else:
            RemovePerson(message);


        


        
        
        



        

    # Se digitar  /ban confirmation  (confirmação de ban pela conta em que está o bot)
    elif(message.lower() == "/ban confirmation"):


        # Pegando a classe para saber se você enviou a mensagem

        parent = last_message.find_element_by_xpath('..')

        parent = parent.find_element_by_xpath('..')

        parent = parent.find_element_by_xpath('..')

        parent = parent.find_element_by_xpath('..')

        parent = parent.find_element_by_xpath('..')

        print(parent.get_attribute("class"));

        if("message-out" in parent.get_attribute("class")):

            if(ban_confirmation == True):
                ban_confirmation = False;

                message_input.send_keys("Ban confirmation disabled!");

                send_message.click();



            else:
                ban_confirmation = True;
        
                message_input.send_keys("Ban confirmation enabled!");

                send_message.click();


        else:
            message_input.send_keys("Error... Just the admin can do this!");

            send_message.click();



    

    


    elif(message[0] == "/"):
    
        message_input.send_keys("*I don't undestand*", Keys.SHIFT + Keys.ENTER, "‎‎‎‎‏‏‎ ‎");

        message_input.send_keys(Keys.SHIFT, Keys.ENTER);


        message_input.send_keys("Type /help to see the comand list...");


        # Enviando a mensagem
        send_message.click();