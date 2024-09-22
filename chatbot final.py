import json
from difflib import get_close_matches
import tkinter as tk
from tkinter import simpledialog, messagebox

#HERE : loads!!! knowledge base from JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

#it is going to save!!!! knowledge base back to JSON file!!! (so the memory is updated anddd pulls off)
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

#fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiind the best match for the user question
def find_best_matches(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

#get the answer for a given question ;)
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"].lower() == question.lower():
            return q["answer"]
    return None

#well the brain, ykik : the main chatbot functionality
def chatbot_response(user_input: str) -> str:
    best_match = find_best_matches(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_match:
        return get_answer_for_question(best_match, knowledge_base)
    else:
        #MARIPOSAAAA is going to ask the user to provide a new answer if none is found!
        new_answer = simpledialog.askstring("TEACH ME ╰(*°▽°*)╯", "I didn't understand your question. Could you tell me what I should answer?")
        if new_answer and new_answer.lower() != 'skip':
            knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
            save_knowledge_base("knowledge_base.json", knowledge_base)
            return "Oh WOW! Thank you so much! I learned something new today!"
        return "I'm sorry, I couldn't understand that. Please try again."

#thats going to let you send a message in the GUI ;)
def send_message():
    user_input = input_box.get("1.0", "end-1c").strip()  #here you GETTTT the user's input
    input_box.delete("1.0", "end")  #youuuu clear the input box

    #if user_input.lower() == 'quit':  #je saissss paaaas si cest bien mais bon ca marchait pas
        #root.quit()

    if user_input.lower() == 'quit':  #that's when the user wantssss to quit #sad
        chat_window.insert(tk.END, f"You: {user_input}\n")  #it displays its input
        response = "OH! Well, it was a HUGE pleasure talking and learning with you! I enjoyed it SOOO much! Have a really great day and don't hesitate to talk to me again soon if you have questions or else!!! :)"
        chat_window.insert(tk.END, f"{bot_name}: {response}\n")  #that is going to display the chatbot's response
        chat_window.see(tk.END) 
        root.after(2000, root.destroy)  #it closes the window after 3 seconds, soooo 2000 = 2 seconds (you can change the time if you want)


    if user_input:
        chat_window.insert(tk.END, f"You: {user_input}\n")  # Display user input
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, f"{bot_name}: {response}\n")  # Display chatbot response
        chat_window.see(tk.END)  # Scroll chat window to the end

        #AN ANIMATIONNNNNNNNN cuz why not??? lets use tkinter as a whole program
        animation_label = tk.Label(root, text="Sending...", font=("Helvetica", 12), fg="#333")
        animation_label.place(x=150, y=550)  #aaadjust the position as needed!!

        i = 0
        def animate():
            nonlocal i
            animation_label.config(text="Sending... (≧∀≦)ゞ" + "." * (i % 3 + 1))
            i += 1
            if i < 10:  #adjust the animation duration as needed
                root.after(100, animate)
            else:
                animation_label.destroy()

        animate()

#lets make the GUI steup aesthteic :)))) GUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


#root = tk.Tk()  
#root.title("Chatbot")  this 2 lines if you want smth ugly and simple
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x600")
root.configure(background="#ffe6f7")

#WINDOW THAT WILL DISPLAY THE CHAT
chat_window = tk.Text(root, width=40, height=20, font=("Helvetica", 12), wrap=tk.WORD, bg="#ffe6f7", fg="#333") 
#blablablablabalaba (root, bd=1, bg="white", width=50, height=8) (if smth simple)
#chat_window.pack(padx=10, pady=10) smth simple
chat_window.pack(pady=20)

#input frame :))))
# Input frame
input_frame = tk.Frame(root, bg="#ffe6f7")
input_frame.pack(pady=10)

#input box (A BORING ONEEEE VS A CUUUUUUUTE ONE)
#input_box = tk.Text(root, bd=1, bg="white", width=29, height=2)
#input_box.pack(padx=10, pady=10)
input_box = tk.Text(input_frame, width=30, height=5, font=("Helvetica", 12), wrap=tk.WORD, bg="#ffe6f7", fg="#333")
input_box.pack(side=tk.LEFT, padx=10)

#THEEEEEEEEEEE send button (same battle as before goes here hahaha)
#send_button = tk.Button(root, text="Send", width=12, command=send_message)
#send_button.pack()
send_button = tk.Button(input_frame, text="Send", font=("Helvetica", 12), bg="#ffc5c5", fg="#333", command=send_message)
send_button.pack(side=tk.LEFT, padx=10)

# Show notice
def show_notice():

    #DOESNT WORK BUT I FELT BAD DELETING IT SO IT IS NOW A COMMMENT HAHAHAH
    #notice_window = tk.Toplevel(root)
    #notice_window.configure(background="#ffe6f7")

    #image = tk.PhotoImage(file="cute.image.png")
    #image_label = tk.Label(notice_window, image=image, bg="#ffe6f7")
    #image_label.pack(pady=10)

    #notice_text = tk.Text(notice_window, width=40, height=10, font=("Helvetica", 12), wrap=tk.WORD, bg="#ffe6f7", fg="#333")
    #notice_text.pack(pady=10)

    #notice_text.insert(tk.END, "Welcome my dear! (●'◡'●)\n\n")
    #notice_text.insert(tk.END, "I will be pleased to be your new conversational friend!\n\n")
    #notice_text.insert(tk.END, "So, these are the instructions so you can understand better how I work:\n\n")
    #notice_text.insert(tk.END, "- You are able to give me a name.\n")
    #notice_text.insert(tk.END, "- Type your question in the input field.\n")
    #notice_text.insert(tk.END, "- Click 'Send' to receive a response from the bot.\n")
    #notice_text.insert(tk.END, "- If you see that I can't answer properly, you can provide me new knowledge by typing them in the input field and clicking 'Send'.\n")
    #notice_text.insert(tk.END, "- That way, I will be able to learn and improve my responses with an amazing person like you! :)\n")
    #notice_text.insert(tk.END, "- The more questions and answers are added, the more the conversation will grow and become COOOL! \n")
    #notice_text.insert(tk.END, "- We can talk about anything you want, just ask! :D \n")
    #notice_text.insert(tk.END, "- You can ask me about anything from history, book recommendations, your life, technology, fun facts or ANYTHING else you're interested in! \n")
    #notice_text.insert(tk.END, "- When you feel satisfied with the conversation, type 'quit' to exit the application. \n\n")
    #notice_text.insert(tk.END, "SO, are you ready to chat with me? (❁´◡`❁)")

    #notice_window.wait_window(notice_window)

    messagebox.showinfo ("LUNA'S CREATION - MARIPOSA",
                        "Welcome my dear! (●'◡'●)\n\n"
                        "I will be pleased to be your new conversational friend!\n\n"
                        "So, these are the instructions so you can understand better how I work:\n\n"
                        "- You are able to give me a name.\n"
                        "- Type your question in the input field.\n"
                        "- Click 'Send' to receive a response from the bot.\n"
                        "- If you see that I can't answer properly, you can provide me new knowledge by typing them in the input field and clicking 'Send'.\n"
                        "- That way, I will be able to learn and improve my responses with an amazing person like you! :)\n"
                        "- The more questions and answers are added, the more the conversation will grow and become COOOL! \n"
                        "- We can talk about anything you want, just ask! :D \n"
                        "- You can ask me about anything from history, book recommendations, your life, technology, fun facts or ANYTHING else you're interested in! \n"
                        "- When you feel satisfied with the conversation, type 'quit' to exit the application. \n\n"
                        "SO, are you ready to chat with me? (❁´◡`❁)")

#here you show the noticeeeeee window
show_notice()

#heeerreeeeeee a window will appear
bot_name = simpledialog.askstring("Bot Name", "What would you like to name me? ^.^")

#the BRAINNN lit. of the chatbot MARIPOSA
knowledge_base = load_knowledge_base("knowledge_base.json")

#GUI will live a sensationallllll LOOOP
root.mainloop()

#THATS IT :D
#YAAAAY!!! YOU'VE MADE A (cute) CHATBOT!!!