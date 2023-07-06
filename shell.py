import openai


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
def work_with_chat_GPT_coments(subjectEntry,key_for_GPT_API):
    openai.api_key = key_for_GPT_API.get()
    messages = []
    message = subjectEntry
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply
def work_with_chat_GPT(subjectEntry,key_for_GPT_API):
    openai.api_key = key_for_GPT_API.get()
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
