# coding=utf-8
import vk_api
vkontakte = vk_api.VkApi(token='0db8b23cc3faf1f60b3aac6ea1a748430863739270b64384256e77c479922e5e718bce010691dbfefa524')
vkontakte._auth_token()
values = {'out': 0, 'count': 100, 'time_offset': 60}

def write_msg(user_id, s):
    vkontakte.method('messages.send', {'user_id': user_id, 'message': s})


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


while True:
    response = vkontakte.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        text = response['items'][0]['body']
        if is_ascii(text):
            write_msg(item['user_id'], 'Ваш текст не является кириллицей')
        elif response['items'][0]['body'] == 'ь':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        elif response['items'][0]['body'] == 'Ь':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        elif response['items'][0]['body'] == 'Ъ':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        elif response['items'][0]['body'] == 'ъ':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        else:
            final = text.replace("я","ıa").replace("Я","Ia").replace("ю","ıý").replace("Ю","Iý").replace("ц","ts").replace("а", "a").replace("ә", "á").replace("б", "b").replace("д", "d").replace("е",
                                                                                                                                                                                                    "e").replace(
            "ф", "f").replace("г", "g").replace("ғ", "ǵ").replace("х", "h").replace("һ", "h").replace("і",
                                                                                                       "і").replace(
            "и", "ı").replace("й", "ı").replace("ж", "j").replace("к", "k").replace("л", "l").replace("м",
                                                                                                        "m").replace(
            "н", "n").replace("ң", "ń").replace("о", "o").replace("ө", "ó").replace("п", "p").replace("қ",
                                                                                                        "q").replace(
            "р", "r").replace("с", "s").replace("ш", "sh").replace("щ", "sh").replace("ч", "ch").replace("т",
                                                                                                         "t").replace(
            "ұ", "u").replace("ү", "ú").replace("в", "v").replace("ы", "y").replace("у", "ý").replace("з",
                                                                                                        "z").replace(
            "ь", "").replace("ъ", "").replace("Ъ", "").replace("Ь", "").replace("А", "A").replace("Ә", "Á").replace("Б", "B").replace("Д",
                                                                                                                                       "D").replace(
            "Е", "E").replace("Ф", "F").replace("Г", "G").replace("Ғ", "Ǵ").replace("Х", "H").replace("І",
                                                                                                       "I").replace(
            "Й", "I").replace("И", "I").replace("Ж", "J").replace("К", "K").replace("Л", "L").replace("М",
                                                                                                        "M").replace(
            "Н", "N").replace("Ң", "Ń").replace("О", "O").replace("Ө", "Ó").replace("П", "P").replace("Қ",
                                                                                                        "Q").replace(
            "Р", "R").replace("С", "S").replace("Ш", "Sh").replace("Щ", "Sh").replace("Ч", "Ch").replace("Т",
                                                                                                         "T").replace(
            "Ұ", "U").replace("Ү", "Ú").replace("В", "V").replace("Ы", "Y").replace("У", "Ý").replace("З", "Z").replace("ё", "е").replace("Ё", "E").replace("э","e").replace("Э","E")
            write_msg(item['user_id'], final)


