import tkinter as tk
import tkinter.font as tkFont
import time

import openai
from instagrapi import Client

from photo import download_photo, delete_photo
from shell import read_accounts, work_with_chat_GPT, find_element_index_by_meaning, work_with_chat_GPT_coments
import random


class App:

    def __init__(self, root):
        # setting title
        root.title("Інста ГУР бот")
        # setting window size
        width = 606
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.userAddLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        self.userAddLabel["font"] = ft
        self.userAddLabel["fg"] = "#01aaed"
        self.userAddLabel["justify"] = "center"
        self.userAddLabel["text"] = "Додавання користувачів"
        self.userAddLabel.place(x=0,y=0,width=244,height=46)

        self.userLoginEntry=tk.Entry(root)
        self.userLoginEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.userLoginEntry["font"] = ft
        self.userLoginEntry["fg"] = "#333333"
        self.userLoginEntry["justify"] = "center"
        self.userLoginEntry["text"] = "login"
        self.userLoginEntry.place(x=90,y=40,width=153,height=30)


        self.userLoginLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.userLoginLabel["font"] = ft
        self.userLoginLabel["fg"] = "#333333"
        self.userLoginLabel["justify"] = "center"
        self.userLoginLabel["text"] = "Логін"
        self.userLoginLabel.place(x=10,y=40,width=70,height=25)

        self.userPasswordLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.userPasswordLabel["font"] = ft
        self.userPasswordLabel["fg"] = "#333333"
        self.userPasswordLabel["justify"] = "center"
        self.userPasswordLabel["text"] = "Пароль"
        self.userPasswordLabel.place(x=20,y=90,width=70,height=25)

        self.userPasswordEntry=tk.Entry(root)
        self.userPasswordEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.userPasswordEntry["font"] = ft
        self.userPasswordEntry["fg"] = "#333333"
        self.userPasswordEntry["justify"] = "center"
        self.userPasswordEntry["text"] = "password"
        self.userPasswordEntry.place(x=90,y=90,width=152,height=30)

        self.userAddButton = tk.Button(root)
        self.userAddButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.userAddButton["font"] = ft
        self.userAddButton["fg"] = "#000000"
        self.userAddButton["justify"] = "center"
        self.userAddButton["text"] = "Додати"
        self.userAddButton.place(x=150, y=140, width=94, height=28)
        self.userAddButton["command"] = lambda: self.userAddButton_command()


        self.addBotCountLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.addBotCountLabel["font"] = ft
        self.addBotCountLabel["fg"] = "#333333"
        self.addBotCountLabel["justify"] = "center"
        self.addBotCountLabel["text"] = "Введіть к-сть ботів"
        self.addBotCountLabel.place(x=260,y=70,width=152,height=30)

        self.addBotCountEntry=tk.Entry(root)
        self.addBotCountEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.addBotCountEntry["font"] = ft
        self.addBotCountEntry["fg"] = "#333333"
        self.addBotCountEntry["justify"] = "center"
        self.addBotCountEntry.place(x=270,y=100,width=307,height=31)



        self.postLinkLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.postLinkLabel["font"] = ft
        self.postLinkLabel["fg"] = "#333333"
        self.postLinkLabel["justify"] = "center"
        self.postLinkLabel["text"] = "Введіть посилання на пост"
        self.postLinkLabel.place(x=270,y=130,width=208,height=30)

        self.postLinkEntry=tk.Entry(root)
        self.postLinkEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.postLinkEntry["font"] = ft
        self.postLinkEntry["fg"] = "#333333"
        self.postLinkEntry["justify"] = "center"
        self.postLinkEntry.place(x=270,y=160,width=308,height=32)



        self.subjectLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.subjectLabel["font"] = ft
        self.subjectLabel["fg"] = "#333333"
        self.subjectLabel["justify"] = "center"
        self.subjectLabel["text"] = "Тематика"
        self.subjectLabel.place(x=270,y=10,width=70,height=25)

        self.subjectEntry=tk.Entry(root)
        self.subjectEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.subjectEntry["font"] = ft
        self.subjectEntry["fg"] = "#333333"
        self.subjectEntry["justify"] = "center"
        self.subjectEntry.place(x=270,y=40,width=308,height=30)

        self.usernameAccountEntry=tk.Entry(root)
        self.usernameAccountEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.usernameAccountEntry["font"] = ft
        self.usernameAccountEntry["fg"] = "#333333"
        self.usernameAccountEntry["justify"] = "center"
        self.usernameAccountEntry.place(x=20,y=360,width=141,height=32)


        self.createButton=tk.Button(root)
        self.createButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.createButton["font"] = ft
        self.createButton["fg"] = "#000000"
        self.createButton["justify"] = "center"
        self.createButton["text"] = "Створити"
        self.createButton.place(x=90,y=560,width=70,height=25)
        self.createButton["command"] = self.createButton_command

        self.createPostLabel=tk.Label(root)
        self.createPostLabel["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=18)
        self.createPostLabel["font"] = ft
        self.createPostLabel["fg"] = "#01aaed"
        self.createPostLabel["justify"] = "center"
        self.createPostLabel["text"] = "Створити пост"
        self.createPostLabel.place(x=0,y=270,width=172,height=30)

        self.imageLinkLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.imageLinkLabel["font"] = ft
        self.imageLinkLabel["fg"] = "#333333"
        self.imageLinkLabel["justify"] = "center"
        self.imageLinkLabel["text"] = "Введіть посилання на картинку"
        self.imageLinkLabel.place(x=0,y=390,width=249,height=51)

        self.imageLinkEntry=tk.Entry(root)
        self.imageLinkEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.imageLinkEntry["font"] = ft
        self.imageLinkEntry["fg"] = "#333333"
        self.imageLinkEntry["justify"] = "center"
        self.imageLinkEntry.place(x=20,y=440,width=205,height=30)

        self.subjectPostLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.subjectPostLabel["font"] = ft
        self.subjectPostLabel["fg"] = "#333333"
        self.subjectPostLabel["justify"] = "center"
        self.subjectPostLabel["text"] = "Введіть тематику для тексту"
        self.subjectPostLabel.place(x=0,y=470,width=220,height=33)

        self.subjectPostEntry=tk.Entry(root)
        self.subjectPostEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.subjectPostEntry["font"] = ft
        self.subjectPostEntry["fg"] = "#333333"
        self.subjectPostEntry["justify"] = "center"
        self.subjectPostEntry.place(x=20,y=510,width=204,height=30)

        self.coment_check_entery_Label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        self.coment_check_entery_Label["font"] = ft
        self.coment_check_entery_Label["fg"] = "#333333"
        self.coment_check_entery_Label["justify"] = "center"
        self.coment_check_entery_Label["text"] = "Відповідь чата GPT"
        self.coment_check_entery_Label.place(x=270, y=200, width=308, height=62)

        self.coment_check_entery = tk.Text()
        self.coment_check_entery.pack()
        self.coment_check_entery.grid(column=1, row=20)
        self.coment_check_entery["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.coment_check_entery["font"] = ft
        self.coment_check_entery.place(x=270, y=250, width=308, height=62)


        self.regenerate = tk.Button(root)
        self.regenerate["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.regenerate["font"] = ft
        self.regenerate["fg"] = "#000000"
        self.regenerate["justify"] = "center"
        self.regenerate["text"] = "Згенерувати"
        self.regenerate.place(x=270, y=330, width=100, height=25)
        self.regenerate["command"] = self.regenerate_command  # commentPostButton_command_with_reply

        self.post_without_replays = tk.Button(root)
        self.post_without_replays["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.post_without_replays["font"] = ft
        self.post_without_replays["fg"] = "#000000"
        self.post_without_replays["justify"] = "center"
        self.post_without_replays["text"] = "запостити без відповідей"
        self.post_without_replays.place(x=375, y=330, width=100, height=25)
        self.post_without_replays["command"] = self.post_without_replays_command  # commentPostButton_command_with_reply

        self.post_with_replays = tk.Button(root)
        self.post_with_replays["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.post_with_replays["font"] = ft
        self.post_with_replays["fg"] = "#000000"
        self.post_with_replays["justify"] = "center"
        self.post_with_replays["text"] = "запостити з відповідями"
        self.post_with_replays.place(x=480, y=330, width=100, height=25)
        self.post_with_replays["command"] = self.post_with_replays_command  # commentPostButton_command_with_reply



        self.key_for_GPT_API_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.key_for_GPT_API_Label["font"] = ft
        self.key_for_GPT_API_Label["fg"] = "#333333"
        self.key_for_GPT_API_Label["justify"] = "center"
        self.key_for_GPT_API_Label["text"] = "Ключ для чату GPT"
        self.key_for_GPT_API_Label.place(x=270,y=370,width=308,height=25)


        self.key_for_GPT_API=tk.Entry(root)
        self.key_for_GPT_API["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.key_for_GPT_API["font"] = ft
        self.key_for_GPT_API["fg"] = "#333333"
        self.key_for_GPT_API["justify"] = "center"
        self.key_for_GPT_API.place(x=270,y=400,width=308,height=32)

    def userAddButton_command(self):
        file = open("users.txt", "a")
        file.write(self.userLoginEntry.get() + "/" + self.userPasswordEntry.get()+"\n")
        file.close()
    def createButton_command(self):
        strings = read_accounts()
        answer = work_with_chat_GPT(self.subjectPostEntry,self.key_for_GPT_API)
        photo_url = self.imageLinkEntry.get()+""
        save_path = "photos/photo.jpg"
        download_photo(photo_url, save_path)
        cl = Client()
        cl.login(strings[find_element_index_by_meaning(strings,self.usernameAccountEntry.get()+"")][0], strings[find_element_index_by_meaning(strings,self.usernameAccountEntry.get()+"")][1])
        print(cl.account_info().dict())
        media = cl.photo_upload(
            "photos/photo.jpg",
            caption=answer)

        delete_photo("photos/photo.jpg")

    def regenerate_command(self):
        self.coment_check_entery.insert(tk.END, "")
        answer = work_with_chat_GPT(self.subjectEntry,self.key_for_GPT_API)
        self.coment_check_entery.insert(tk.END, answer)
    def post_without_replays_command(self):
        answer = self.coment_check_entery.get("1.0", "end-1c")
        strings = read_accounts()
        print(len(strings))
        if int(self.addBotCountEntry.get()) <= len(strings):

            cl = Client()
            cl.login(strings[int(self.addBotCountEntry.get())][0], strings[int(self.addBotCountEntry.get())][1])
            media_id = cl.media_id(cl.media_pk_from_url(
                self.postLinkEntry.get()))
            comment = cl.media_comment(media_id, answer)
            comment.dict()

            for i in range(int(self.addBotCountEntry.get()) - 1, 0, -1):
                print(i)
                cl1 = Client()
                cl1.login(strings[i][0], strings[i][1])
                random_number1 = random.randint(1, 2)
                if random_number1 == 1:
                    comment1 = cl1.media_comment(media_id, work_with_chat_GPT_coments(
                        "напиши аргументованый очень краткий комент подержки в ответ" + answer))
                else:
                    comment1 = cl1.media_comment(media_id, work_with_chat_GPT_coments(
                        "напиши краткий грубый  комент в ответ очень краткий опровергает позию " + answer))
                print(comment.pk)
                comment.dict()
                delay = random.randint(1, 10)
                time.sleep(delay)
        else:
            print("похибка")

    def post_with_replays_command(self) -> object:
        answer = self.coment_check_entery.get("1.0", "end-1c")
        strings = read_accounts()
        print(len(strings))
        if int(self.addBotCountEntry.get()) <= len(strings):
            cl = Client()
            cl.login(strings[int(self.addBotCountEntry.get())][0], strings[int(self.addBotCountEntry.get())][1])
            media_id = cl.media_id(cl.media_pk_from_url(
                self.postLinkEntry.get()))
            comment = cl.media_comment(media_id, answer)
            comment.dict()

            for i in range(int(self.addBotCountEntry.get()) - 1, 0, -1):
                print(i)
                cl1 = Client()
                cl1.login(strings[i][0], strings[i][1])
                random_number1 = random.randint(1, 2)
                if random_number1 == 1:
                    comment1 = cl1.media_comment(media_id, work_with_chat_GPT_coments(
                        "напиши аргументованый очень краткий комент подержки в ответ" + answer),
                                                replied_to_comment_id=comment.pk)
                else:
                    comment1 = cl1.media_comment(media_id, work_with_chat_GPT_coments(
                        "напиши краткий грубый  комент в ответ очень краткий опровергает позию " + answer),
                                                replied_to_comment_id=comment.pk)
                print(comment.pk)
                comment.dict()
                delay = random.randint(1, 10)
                time.sleep(delay)

        else:
            print("похибка")