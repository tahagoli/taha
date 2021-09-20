import json
import requests
import time
import urllib




TOKEN = '1391583443:1NDTayVHoX3s64dSauMsrbsJvoVoueNpiYOtuM5D'
URL = "https://tapi.bale.ai/{}/".format(TOKEN)

print(URL);


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    print(js);
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        print(update)
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]



    if (text =="1"):
     send_message("  خوش آمدید", chat)

    elif (text =="2"):
     send_message("video", chat)

     
    elif (text =="3"):
       send_message("voice", chat)

     
    elif (text =="4"):
      send_message("photo", chat)





     
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
