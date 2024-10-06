#here are the imports from "biblioteks" I suppose
import json
from difflib import get_close_matches
#for the GUI APP 
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

#here we must LOADDDDD our knowledge base thanks to json (or better said FROM the json file)
def load_knowledge_base(file_path: str) -> dict: #knowledge 
#dict = dictionary
    with open(file_path, 'r') as file:  #file = opened file
        data: dict = json.load(file)
    return data

#now that we loaded it, KEEP IN MIND that's a chatbot so it is supposed to remember things
#so let's now SAVEEEEE the knowledge base in order to have th previous responses in memory
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


#neverthless, what would be the best fits? the best matches of answers?
def find_best_matches(user_question : str, questions: list[str]) -> str | None:
        #"None" because a situation can happen that the data that's being searched doesn't exist/doesn't have sense
        #so we should return None ;)
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    #n=1 means that we want only one best match, we could have put n=2 or n=3 but here it is only a little insignficant project that teaches us some skills, not the invention of a whole competitive chatbot
    #so n=1 will be sufficient for our purpose and to be most perfectly precise for our little project
    #the cutoff correspond to the accuracy of the match (the lower the value, the more less precise the match is)
    #as an example, cutoff=0.6 means that the match must be at least 60% similar to the user_question
    #so taking cutoff=0.0 is similar to 0%, SOOOOO what's the point of using it here? hhahaahaa
    return matches[0] if matches else None


#BUUUUUUUUUUUUUUUT the most exciting part is receiving answers isn't it???????? :))))))
#so let's codeeeeeeeeeeeeeee it hihihi

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
#"q" is like a variable that represents each question in the knowledge_base["questions"] list
#so basically, we're looking for an answer in the knowledge_base that matches the user's question and return its CORRRECT answer (or at leat a logical one) !!!
    return None

#we are progressssssssing on our really non-extraordinary chatbot (EVEN THO FOR ME IT IS LIKE OMG????????? SPLENDID????? PROGRAMMING A KIND OF CONVERSTIONAL MACHINE TO TALK WITH AND TEACH IT???? isn't that amazing????)
def chat_bot():

    bot_name = input("What would you like to name me? :)            ")
    print(f"{bot_name}: Wow! {bot_name}! I love my name! So, I'm your new virtual friend. How can I assist you today? ^_^") 

    knowledge_base: dict = load_knowledge_base("knowledge_base.json")

    #creating an infinite loop to keep the chatbot running ;)
    while True:
        user_input: str = input("You:") #so we can chat with our A M A Z I N GGGGG invention

        if user_input.lower() == 'quit':
            #f"{bot_name}" is an f-string on python, which replaces {bot_name} with the actual value of the variable bot_name!!!!! 
            #so without the f, it treats {bot_name} as a literal string, which is why you could see {bot_name} instead of the bot's actual name given by the user :)
            print(f"{bot_name} : OH! Well, it was a HUGE pleasure talking and learning with you! I enjoyed it SOOO much! Have a really great day and don't hesitate to talk to me again soon if you have questions or else!!! :)")
        #petite piqûre de rappel car jai trop fait l'anglophone hahaha : "=" assigns a value et "==" compares values for equality
        #voilà revenons à nos moutons beeeh beeeeh meuuuuuuh meuuuuuuuuuuuuuuuh kh kh kh on se fend la poire je vais cabler il est 2h du mat et je fais ça moi? décidément HA HA HA HA HA HA allez on continue on lache rien AH LE GATEAU IL ETAIT SECCCCC???????? signorinna poltronè sofà authentica qualità et voilà ha ha ha bref 
            break
        #that means the chatbot is going to stop if the user types "quit" :)
        #si normal otra vez pero es que vamos mi espalda està ya muertisimaaaaaa ayudaaaaaaaaaa

def chatbot_response(user_input):
        best_match: str | None = find_best_matches(user_input, [q["question"] for q in knowledge_base["questions"]])
    #we want to find the best match in our knowledge base based on the user's question like the "user input"
    #remember : "q" of QUESTION 

    #bloody hell, what if the user's question is not in our knowledge base? SO IT DOESNT FIND A BEST MATCH?????
    #in programming we must always think about all the negative thinks that could happen to avoid these kind of situations having no issues
    #like a forensics game in cybersecurity (actually idk if that"s a good example, but that"s how I visualize it ^^ )

        if best_match:
            #answer: str = get_answer_for_question(best_match, knowledge_base)
            #print(f"{bot_name}: {answer}") #here it is exciting cuz we are able now to choose an example of answer that the chatbot (WHICH IS NOT HUMAN) can answer to the user based on the user's question
                return get_answer_for_question(best_match, knowledge_base)
        else:
            #print(f"{bot_name}: I am so sorry my dear, I didn't understand your question. Could you please try again and teach me the right answer? ;)")
            #FEEEEEEEEEEEEEEEEL FREEEEEEEEEEEEEEE to customize the answer as you wish
            #new_answer: str = input('Type the answer or "skip" to skip :') #that's your impact, the 'You'
            new_answer = simpledialog.askstring("TEACH ME ╰(*°▽°*)╯", "I am so sorry my dear, I didn't understand your question. Could you tell what should I answer? ;)")
#so everything you type here will be the new answer for the best match question in our knowledge base (and then the ANSWER REGISTRATED BY OUUUR (probably YOUR) chatbot!!!!!!!!!!!! HAHAHA AMAZING NO???)
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                #append modifies the original list in place and does not return a new list, it adds the item as the last element of the list, if you append another list, it will be added as a single element (nested list).
                #that means if the user types something other than "skip", it will be added to our knowledge base as a NEEEEEW question and a NEEEEEEEW answer
                save_knowledge_base("knowledge_base.json", knowledge_base)
                #soooooooo the chatbooot will register your answer and say that : (feel free to customize it once againnnnn :D)
                return (f"{bot_name}: Oh WOW! Thank you so much! I learned something new today! :)") #remember : the 'Bot' is a programmed character of our chatbot, NOOOOOOOOT A HUMAN!!! IT DOESNT HAVE FEELINGS OR MINDS LIKE US!!!!!


if __name__ == '__main__':
    #we are going to run our chatbot only if this script is the main script (not imported)
    chat_bot()

# GUI Application
def send_message():
    user_input = input_box.get("1.0", "end-1c").strip()
    input_box.delete("1.0", "end")

    if user_input.lower() == 'quit':
        root.quit()

    if user_input:
        chat_window.insert(tk.END, f"You: {user_input}\n")
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, f"{bot_name}: {response}\n")
        chat_window.see(tk.END)

#construction of the GUU
root = tk.Tk()
root.title("Chatbot") #free to change Chatbot to any other name

#chat display window
chat_window = tk.Text(root, bd=1, bg="white", width=50, height=8) #measures
chat_window.pack(padx=10, pady=10) #dimensions

#input box
input_box = tk.Text(root, bd=1, bg="white", width=29, height=2) #same as before but now w/the input box even tho in the final one I changed it if I am not mistaken
input_box.pack(padx=10, pady=10)

#send button
send_button = tk.Button(root, text="Send", width=12, command=send_message)
send_button.pack() #smth simple and basic nothing really joyful

#askiiiing for the bot's name
bot_name = simpledialog.askstring("Bot Name", "What would you like to name me?")

#loading knowledge base within JSON
knowledge_base = load_knowledge_base("knowledge_base.json")

root.mainloop() #execution i suppose 

#I reworked the end of the coding

#lets do the..... ROULEMENT DE TAMBOUR
#GUI APPLICATION :D

#def show_notice():
    #messagebox.showinfo ("LUNA'S CREATION - LDCHATBOT", 
                        
                        #"Welcome my dear! (●'◡'●)\n\n"
                        
                        #"I will be pleased to be your new conversational friend!\n\n"

                        #"So, these are the instructions so you can understand better how I work:\n\n"
                        #"- You are able to give me a name.\n"
                        #"- Type your question in the input field.\n"
                        #"- Click 'Send' to receive a response from the bot.\n"
                        #"- If you see that I can't answer properly, you can provide me new knowledge by typing them in the input field and clicking 'Send'.\n"
                        #"- That way, I will be able to learn and improve my responses with an amazing person like you! :)\n"
                        #"- The more questions and answers are added, the more the conversation will grow and become COOOL! \n"
                        #"- We can talk about anything you want, just ask! :D \n"
                        #"- You can ask me about anything from history, book recommendations, your life, technology, fun facts or ANYTHING else you're interested in! \n"
                        #"- When you feel satisfied with the conversation, type 'quit' to exit the application. \n\n"

                        #"SO, are you ready to chat with me? (❁´◡`❁)")

#def send_message():
    #user_input = input_box.get("1.0", "end-1c").strip()
    #input_box.delete("1.0", "end")

    #if user_input.lower() == 'quit':
        #root.quit()

    #if user_input:
        #chat_window.insert(tk.END, f"You: {user_input}\n")
        #response = chatbot_response(user_input)
        #chat_window.insert(tk.END, f"{bot_name}: {response}\n")
        #chat_window.see(tk.END)

        # Main function to run the chatbot app
#if __name__ == '__main__':
    # Initialize the GUI window
    #root = tk.Tk()
    #root.title("Chatbot")

    # Chat display window (read-only)
    #chat_window = tk.Text(root, bd=1, bg="white", width=50, height=8)
    #chat_window.pack(padx=10, pady=10)

    # User input box
    #input_box = tk.Text(root, bd=1, bg="white", width=29, height=2)
    #input_box.pack(padx=10, pady=10)

    # Send button to submit user input
    #send_button = tk.Button(root, text="Send", width=12, command=send_message)
    #send_button.pack()

#you can customize the chatbot by adding more questions and answers in the "knowledge_base.json" file that you must create now if it is still not done deaaar
#NOW, enjoooooooooooooooooooooooooooooooooooooooooooy :))))
