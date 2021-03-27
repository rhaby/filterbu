print ("[1] filter bu")
print ("[2] export user instagram")
ali = input("enter number tools :")

if ali == '1':
    import requests
    req = requests.Session()
    file = open('user.txt', 'r')
    while True:
            username = file.readline().split('\n')[0]
            print("try username : " + username)
            url = ('https://www.instagram.com/' + username + '?igshid=1lte15hyf3o3k')
            payload = ''
            headers = {
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
            }
            ali = req.get(url, headers=headers, data=payload).text
            if ('"is_business_account":true') in ali:
                print("this business account: " + username)
                with open('business.txt', 'a') as x:
                 x.write(username + '\n')
            elif ("connection.create_connection(") in ali:    
                    print("internet error ")

elif ali == '2':
    import requests
    import time
    import os
    from colorama import Fore , init, Style

    init()
    num=0

    cls=lambda :os.system('cls')
    HEADERS={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Accept': "*/*",'Host': 'www.instagram.com'}
    user_list = open("user.txt", "w")
    keyword=open("CIKU370.txt","r").read().splitlines()
    def grab(sleep):
        global num
        try:
            for word in keyword:
                time.sleep(int(sleep))
                url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="
                response = requests.get(url + word + "&count=1800", headers=HEADERS).json()
                for index in response['users']:
                    username = index['user']['username']
                    num += 1
                    print(username)
                    user_list.write(f"{username}\n")
            user_list.close()
            cls()
            input(f"[!] Total Usernames : {num}")
            exit(0)
        except Exception:
            print('[!] error >>> ')

    slp=input("[+] Sleep >> : ")
    grab(slp)
else:
    print ("no")
