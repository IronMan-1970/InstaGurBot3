import openai
import windscribe

from photo import download_photo
from instagrapi import Client
def cli():
    cl = Client()
    cl.login("nikaaksenina", "N52483156")
    print("Виберіть завдання:"
          "\n1 запостити іпсо"
          "\n2 закоментити іпсо"
          "\n3 залайкати іпсо")
    menuChooser = input()

    if menuChooser == '1':  # if key 'q' is pressed
        photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRipjtAVbwcoE8WC8332VHt2IjP7GPHB0A3jQ&usqp=CAU"
        save_path = "photos/photo.jpg"
        download_photo(photo_url, save_path)
        print(cl.account_info().dict())
        media = cl.photo_upload(
            "photos/photo.jpg",
            caption="Прем`єра 2023 року! Веселі пригоди! Венздей Адамс та Хаґі Ваґі у <<Грі в Кальмара>>! Найкрутіші герої, яких обожнюють діти. Танці, інтерактивний екшн! Світлове шоу та багато мультимедійних ефектів! Ви поринете у світ <<Гри в Кальмара>> Ближче побачите улюблених Хаґі Ваґі, Кісі Місі, Ванк Панк, Скарі Ларі! Познайомитесь з жахливо прикольною Венздей Адамс! Та нарешті преможите злодія!")


    elif menuChooser == '2':
        media_id = cl.media_id(cl.media_pk_from_url(
            'https://www.instagram.com/p/CtyeYlHMIBa/?utm_source=ig_web_button_share_sheet&igshid=MzRlODBiNWFlZA=='))
        comment = cl.media_comment(media_id, "Запад нас слєваєт")
        comment.dict()
        comment = cl.media_comment(media_id, "Нам пзд як полякам в 39", replied_to_comment_id=comment.pk)
        print(comment.pk)
        comment.dict()


    else:
        media_id = cl.media_id(cl.media_pk_from_url(
            'https://www.instagram.com/p/CtyeYlHMIBa/?utm_source=ig_web_button_share_sheet&igshid=MzRlODBiNWFlZA=='))
        like = cl.media_like(media_id)


def read_accounts():
    strings = []

    readAccounts = open("users.txt", "r")
    for account in readAccounts:
        strings.append(account)

    accounts = []
    for i in range(len(strings)):
        split = strings[i].split("/")
        b = [split[0], split[1]]
        accounts.append(b)

    return accounts
def work_with_chat_GPT_coments(subjectEntry):
    openai.api_key = "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"
    messages = []
    message = subjectEntry
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply
def work_with_chat_GPT(subjectEntry):
    openai.api_key = "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"
    messages = []
    message = subjectEntry.get()
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply
def find_element_index_by_meaning(array, meaning):
    for row_index, row in enumerate(array):
        # Check if the element exists in the current row
        if meaning in row:
            # Found the element in this row
           return row_index


    # If the element is not found in any row
    else:
        print("Element", meaning, "not found in any row")
