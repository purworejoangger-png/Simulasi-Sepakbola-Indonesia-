import os, random
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

def mk_sq(pfx, ovr, stars):
    tpl = [("GK",1),("DF",1),("DF",1),("DF",1),("DF",1),("MF",1),("MF",1),("MF",1),("FW",1),("FW",1),("FW",1),("GK",0),("DF",0),("MF",0),("FW",0),("FW",0)]
    res = []
    for i, (pos, st) in enumerate(tpl):
        if i < len(stars):
            n, p, o, a, nat = stars[i]
        else:
            n, p, o, a, nat = f"{pfx} Player {i+1}", pos, max(68, min(86, ovr + random.randint(-3, 2))), random.randint(20, 31), "IDN"
        res.append({"id": f"{pfx.lower()}_{i+1}", "name": n, "pos": p, "ovr": o, "age": a, "nat": nat, "val": max(1500000000, (o-60)*650000000), "wage": max(35000000, int((o-62)*8500000)), "contract": random.randint(2, 4), "stamina": 100, "is_starter": bool(st), "suspended": 0, "injury": None})
    return res

LIGA1 = [
    {"id":"persib","name":"Persib Bandung","short":"PSB","league":"LIGA1","color":"#003399","accent":"#ffffff","stars":4,"rating":83,"stadium":"Gelora Bandung Lautan Api","squad":mk_sq("PSB",83,[("Kevin Ray Mendoza","GK",82,30,"PHI"),("Nick Kuipers","DF",83,32,"NED"),("Gustavo Franca","DF",82,28,"BRA"),("Edo Febriansah","DF",80,27,"IDN"),("Henhen Herdiana","DF",79,29,"IDN"),("Marc Klok","MF",83,31,"IDN"),("Tyronne del Pino","MF",84,33,"ESP"),("Mateo Kocijan","MF",80,29,"CRO"),("Ciro Alves","FW",85,35,"BRA"),("David da Silva","FW",86,35,"BRA"),("Beckham Putra","FW",80,23,"IDN"),("Teja Paku Alam","GK",79,30,"IDN"),("Rachmat Irianto","DF",80,25,"IDN"),("Adam Alis","MF",80,31,"IDN"),("Dimas Drajad","FW",80,27,"IDN")])},
    {"id":"persija","name":"Persija Jakarta","short":"PSJ","league":"LIGA1","color":"#dc2626","accent":"#facc15","stars":2,"rating":82,"stadium":"Jakarta International Stadium","squad":mk_sq("PSJ",82,[("Andritany Ardhiyasa","GK",80,33,"IDN"),("Rizky Ridho","DF",84,23,"IDN"),("Ondrej Kudela","DF",82,37,"CZE"),("Muhammad Ferarri","DF",80,21,"IDN"),("Firza Andika","DF",79,25,"IDN"),("Maciej Gajos","MF",82,33,"POL"),("Ramon Bueno","MF",81,29,"ESP"),("Hanif Sjahbandi","MF",79,27,"IDN"),("Ryo Matsumura","FW",83,30,"JPN"),("Gustavo Almeida","FW",84,28,"BRA"),("Witan Sulaeman","FW",81,23,"IDN"),("Carlos Eduardo","GK",79,32,"BRA"),("Hansamu Yama","DF",78,29,"IDN"),("Marko Simic","FW",80,36,"CRO")])},
    {"id":"persebaya","name":"Persebaya Surabaya","short":"PBY","league":"LIGA1","color":"#047857","accent":"#facc15","stars":2,"rating":82,"stadium":"Gelora Bung Tomo","squad":mk_sq("PBY",82,[("Ernando Ari","GK",83,22,"IDN"),("Slavko Damjanovic","DF",81,32,"MNE"),("Kadek Raditya","DF",79,25,"IDN"),("Ardi Idrus","DF",79,31,"IDN"),("Catur Pamungkas","DF",78,25,"IDN"),("Francisco Rivera","MF",84,30,"MEX"),("Mohammed Rashid","MF",82,29,"PLE"),("Gilson Costa","MF",80,28,"POR"),("Bruno Moreira","FW",84,25,"BRA"),("Flavio Silva","FW",83,28,"POR"),("Malik Risaldi","FW",81,28,"IDN"),("Toni Firmansyah","MF",78,19,"IDN")])},
    {"id":"arema","name":"Arema FC","short":"ARE","league":"LIGA1","color":"#1e3a8a","accent":"#ef4444","stars":1,"rating":80,"stadium":"Stadion Kanjuruhan","squad":mk_sq("ARE",80,[("Lucas Frigeri","GK",81,35,"BRA"),("Thales Lira","DF",80,31,"BRA"),("Choi Bo-kyung","DF",79,36,"KOR"),("Johan Alfarizi","DF",79,34,"IDN"),("Achmad Maulana","DF",78,21,"IDN"),("Wiliam Marcilio","MF",82,28,"BRA"),("Pablo Oliveira","MF",80,29,"BRA"),("Arkhan Fikri","MF",80,20,"IDN"),("Dalberto Luan","FW",82,30,"BRA"),("Charles Lokolingoy","FW",81,27,"AUS"),("Dedik Setiawan","FW",78,30,"IDN")])},
    {"id":"bali","name":"Bali United","short":"BAL","league":"LIGA1","color":"#b91c1c","accent":"#111827","stars":2,"rating":81,"stadium":"Stadion Kapten I Wayan Dipta","squad":mk_sq("BAL",81,[("Adilson Maringa","GK",82,34,"BRA"),("Elias Dolah","DF",81,31,"THA"),("Brandon Wilson","DF",79,27,"AUS"),("Ricky Fajrin","DF",80,29,"IDN"),("Andhika Wijaya","DF",78,28,"IDN"),("Mitsuru Maruoka","MF",81,28,"JPN"),("Kenzo Nambu","MF",81,32,"JPN"),("Made Tito","MF",79,21,"IDN"),("Privat Mbarga","FW",83,32,"CAM"),("Everton Nascimento","FW",82,31,"BRA"),("Irfan Jaya","FW",80,28,"IDN")])},
    {"id":"borneo","name":"Borneo FC Samarinda","short":"BOR","league":"LIGA1","color":"#ea580c","accent":"#111827","stars":1,"rating":82,"stadium":"Stadion Segiri","squad":mk_sq("BOR",82,[("Nadeo Argawinata","GK",82,27,"IDN"),("Christophe Nduwarugira","DF",81,30,"BDI"),("Gabriel Furtado","DF",81,25,"BRA"),("Leo Guntara","DF",79,30,"IDN"),("Fajar Fathur Rahman","DF",80,22,"IDN"),("Kei Hirose","MF",82,29,"JPN"),("Berguinho","MF",83,27,"BRA"),("Rivaldo Pakpahan","MF",79,21,"IDN"),("Stefano Lilipaly","FW",83,34,"IDN"),("Leo Gaucho","FW",83,23,"BRA"),("Mariano Peralta","FW",82,26,"ARG")])},
    {"id":"psm","name":"PSM Makassar","short":"PSM","league":"LIGA1","color":"#7f1d1d","accent":"#facc15","stars":2,"rating":81,"stadium":"Gelora B.J. Habibie","squad":mk_sq("PSM",81,[("Hilmansyah","GK",79,27,"IDN"),("Yuran Fernandes","DF",84,30,"CPV"),("Aloisio Neto","DF",81,27,"BRA"),("Syahrul Lasinari","DF",78,25,"IDN"),("Victor Luiz","DF",80,27,"BRA"),("Latyr Fall","MF",80,30,"SEN"),("Akbar Tanjung","MF",79,31,"IDN"),("Ananda Raehan","MF",79,21,"IDN"),("Nermin Haljeta","FW",82,27,"SVN"),("Tito Okello","FW",80,28,"SSD"),("Dzaky Asraf","FW",79,21,"IDN")])},
    {"id":"dewa","name":"Dewa United","short":"DEW","league":"LIGA1","color":"#111827","accent":"#eab308","stars":0,"rating":83,"stadium":"Indomilk Arena","squad":mk_sq("DEW",83,[("Sonny Stevens","GK",82,32,"NED"),("Angelo Meneses","DF",81,31,"POR"),("Risto Mitrevski","DF",81,33,"MKD"),("Alta Ballah","DF",79,24,"IDN"),("Reva Adi Utama","DF",79,28,"IDN"),("Alexis Messidoro","MF",84,27,"ARG"),("Hugo Gomes Jaja","MF",83,29,"BRA"),("Ricky Kambuaya","MF",81,28,"IDN"),("Egy Maulana Vikri","FW",83,24,"IDN"),("Alex Martins","FW",84,31,"BRA"),("Taisei Marukawa","FW",83,27,"JPN")])},
    {"id":"madura","name":"Madura United","short":"MAD","league":"LIGA1","color":"#dc2626","accent":"#ffffff","stars":0,"rating":79,"stadium":"Gelora Bangkalan","squad":mk_sq("MAD",79,[("Wagner dos Santos","GK",79,34,"BRA"),("Pedro Monteiro","DF",80,30,"POR"),("Koko Ari","DF",78,24,"IDN"),("Jordy Wehrmann","MF",82,25,"NED"),("Iran Junior","MF",80,29,"BRA"),("Lulinha","FW",82,34,"BRA"),("Maxuel Cassio","FW",80,24,"BRA")])},
    {"id":"malut","name":"Malut United","short":"MAL","league":"LIGA1","color":"#991b1b","accent":"#facc15","stars":0,"rating":80,"stadium":"Gelora Kie Raha","squad":mk_sq("MAL",80,[("Cassio Scheid","DF",80,30,"BRA"),("Wahyu Prasetyo","DF",80,26,"IDN"),("Yance Sayuri","DF",81,27,"IDN"),("Adriano Castanheira","MF",80,31,"POR"),("Yakob Sayuri","FW",83,27,"IDN"),("Diego Martinez","FW",81,29,"PAR")])},
    {"id":"psis","name":"PSIS Semarang","short":"SMG","league":"LIGA1","color":"#1d4ed8","accent":"#facc15","stars":1,"rating":79,"stadium":"Stadion Jatidiri","squad":mk_sq("SMG",79,[("Adi Satryo","GK",80,23,"IDN"),("Alfeandra Dewangga","DF",81,23,"IDN"),("Boubakary Diarra","MF",81,31,"FRA"),("Septian David","MF",80,28,"IDN"),("Gali Freitas","FW",82,20,"TLS")])},
    {"id":"persis","name":"Persis Solo","short":"SOL","league":"LIGA1","color":"#b91c1c","accent":"#facc15","stars":1,"rating":79,"stadium":"Stadion Manahan","squad":mk_sq("SOL",79,[("Muhammad Riyandi","GK",80,24,"IDN"),("Eduardo Kunde","DF",80,27,"BRA"),("Sho Yamamoto","MF",81,28,"JPN"),("Moussa Sidibe","FW",82,30,"MLI"),("Ramadhan Sananta","FW",82,22,"IDN")])},
    {"id":"pss","name":"PSS Sleman","short":"PSS","league":"LIGA1","color":"#15803d","accent":"#ffffff","stars":0,"rating":78,"stadium":"Stadion Maguwoharjo","squad":mk_sq("PSS",78,[("Alan Bernardon","GK",80,30,"BRA"),("Cleberson","DF",81,32,"BRA"),("Betinho","MF",80,32,"BRA"),("Gustavo Tocantins","FW",81,28,"BRA"),("Hokky Caraka","FW",80,20,"IDN")])},
    {"id":"persita","name":"Persita Tangerang","short":"PTA","league":"LIGA1","color":"#6b21a8","accent":"#ffffff","stars":0,"rating":78,"stadium":"Indomilk Arena","squad":mk_sq("PTA",78,[("Igor Rodrigues","GK",80,29,"POR"),("Javlon Guseynov","DF",80,33,"UZB"),("Bae Sin-yeong","MF",80,32,"KOR"),("Marios Ogkmpoe","FW",80,30,"GRE")])},
    {"id":"persik","name":"Persik Kediri","short":"PSK","league":"LIGA1","color":"#581c87","accent":"#facc15","stars":2,"rating":79,"stadium":"Stadion Brawijaya","squad":mk_sq("PSK",79,[("Kiko Carneiro","DF",80,31,"POR"),("Ze Valente","MF",83,30,"POR"),("Rohit Chand","MF",80,32,"NEP"),("Ezra Walian","FW",80,27,"IDN"),("Ramiro Fergonzi","FW",81,35,"ARG")])},
    {"id":"barito","name":"Barito Putera","short":"BAR","league":"LIGA1","color":"#eab308","accent":"#111827","stars":0,"rating":78,"stadium":"Stadion Demang Lehman","squad":mk_sq("BAR",78,[("Lucao","DF",80,29,"BRA"),("Bagas Kaffa","DF",79,22,"IDN"),("Levy Madinda","MF",81,32,"GAB"),("Murilo Mendes","FW",81,29,"BRA")])},
    {"id":"psbs","name":"PSBS Biak","short":"BIA","league":"LIGA1","color":"#0284c7","accent":"#ffffff","stars":0,"rating":78,"stadium":"Stadion Cendrawasih","squad":mk_sq("BIA",78,[("Julian Velazquez","DF",80,34,"ARG"),("Takuya Matsunaga","MF",80,34,"JPN"),("Alexsandro","FW",81,27,"BRA"),("Jeam Kelly Sroyer","FW",79,22,"IDN")])},
    {"id":"semen","name":"Semen Padang FC","short":"SPD","league":"LIGA1","color":"#991b1b","accent":"#facc15","stars":0,"rating":77,"stadium":"Stadion Haji Agus Salim","squad":mk_sq("SPD",77,[("Tin Martic","DF",79,28,"CRO"),("Bruno Dybal","MF",80,30,"BRA"),("Kenneth Ngwoke","FW",80,31,"NGA")])}
]

LIGA2 = [
    {"id":"psim","name":"PSIM Yogyakarta","short":"YOG","league":"LIGA2","color":"#1e40af","accent":"#ffffff","stars":1,"rating":76,"stadium":"Mandala Krida","squad":mk_sq("YOG",76,[("Rafinha","FW",80,32,"BRA"),("Pedrinho","MF",79,29,"BRA")])},
    {"id":"bhayangkara","name":"Bhayangkara FC","short":"BFC","league":"LIGA2","color":"#eab308","accent":"#111827","stars":1,"rating":78,"stadium":"Tri Sanja","squad":mk_sq("BFC",78,[("Matias Mier","MF",81,34,"URU"),("Ilija Spasojevic","FW",80,37,"IDN")])},
    {"id":"persiraja","name":"Persiraja Banda Aceh","short":"PRJ","league":"LIGA2","color":"#ea580c","accent":"#111827","stars":0,"rating":76,"stadium":"Harapan Bangsa","squad":mk_sq("PRJ",76,[("Andik Vermansah","FW",78,33,"IDN"),("Corfe Deri","FW",79,26,"ENG")])},
    {"id":"psms","name":"PSMS Medan","short":"MDN","league":"LIGA2","color":"#15803d","accent":"#ffffff","stars":2,"rating":75,"stadium":"Teladan","squad":mk_sq("MDN",75,[("Fabio Gama","MF",78,32,"BRA")])},
    {"id":"sriwijaya","name":"Sriwijaya FC","short":"SFC","league":"LIGA2","color":"#eab308","accent":"#b91c1c","stars":2,"rating":75,"stadium":"Jakabaring","squad":mk_sq("SFC",75,[("Chencho Gyeltshen","FW",79,28,"BHU")])},
    {"id":"persela","name":"Persela Lamongan","short":"PSL","league":"LIGA2","color":"#0284c7","accent":"#facc15","stars":0,"rating":76,"stadium":"Surajaya","squad":mk_sq("PSL",76,[("Ezechiel Ndouassel","FW",80,36,"CHA"),("Esteban Vizcarra","MF",79,38,"IDN")])},
    {"id":"gresik","name":"Gresik United","short":"GRS","league":"LIGA2","color":"#eab308","accent":"#15803d","stars":0,"rating":74,"stadium":"Joko Samudro","squad":mk_sq("GRS",74,[("Renan Silva","MF",79,35,"BRA")])},
    {"id":"deltras","name":"Deltras Sidoarjo","short":"DEL","league":"LIGA2","color":"#b91c1c","accent":"#111827","stars":0,"rating":75,"stadium":"Gelora Delta","squad":mk_sq("DEL",75,[("Emerson Carioca","FW",78,29,"BRA")])},
    {"id":"persipura","name":"Persipura Jayapura","short":"PPR","league":"LIGA2","color":"#dc2626","accent":"#111827","stars":4,"rating":75,"stadium":"Mandala","squad":mk_sq("PPR",75,[("Boaz Solossa","FW",78,38,"IDN")])},
    {"id":"psps","name":"PSPS Pekanbaru","short":"PKU","league":"LIGA2","color":"#1d4ed8","accent":"#ffffff","stars":0,"rating":75,"stadium":"Kaharuddin Nasution","squad":mk_sq("PKU",75,[("Omid Popalzay","MF",79,28,"AFG")])},
    {"id":"bekasi","name":"FC Bekasi City","short":"BKS","league":"LIGA2","color":"#111827","accent":"#ef4444","stars":0,"rating":75,"stadium":"Patriot Candrabhaga","squad":mk_sq("BKS",75,[("Cahya Supriadi","GK",78,21,"IDN")])},
    {"id":"persijap","name":"Persijap Jepara","short":"JEP","league":"LIGA2","color":"#b91c1c","accent":"#facc15","stars":0,"rating":74,"stadium":"Gelora Bumi Kartini","squad":mk_sq("JEP",74,[("Rosalvo Junior","FW",78,33,"BRA")])}
]

ACL_TWO = [
    {"id":"gamba","name":"Gamba Osaka (JPN)","short":"GAM","color":"#1d4ed8","accent":"#111827","stars":2,"rating":85},
    {"id":"pohang","name":"Pohang Steelers (KOR)","short":"POH","color":"#b91c1c","accent":"#111827","stars":3,"rating":85},
    {"id":"port_fc","name":"Port FC (THA)","short":"PRT","color":"#ea580c","accent":"#1e3a8a","stars":0,"rating":82},
    {"id":"lion_city","name":"Lion City Sailors (SGP)","short":"LCS","color":"#1d4ed8","accent":"#ffffff","stars":1,"rating":81},
    {"id":"selangor","name":"Selangor FC (MAS)","short":"SEL","color":"#dc2626","accent":"#facc15","stars":2,"rating":81},
    {"id":"nam_dinh","name":"Nam Dinh FC (VIE)","short":"NAM","color":"#eab308","accent":"#1d4ed8","stars":1,"rating":80},
    {"id":"kaya_fc","name":"Kaya FC Iloilo (PHI)","short":"KAY","color":"#eab308","accent":"#111827","stars":0,"rating":78},
    {"id":"eastern","name":"Eastern SC (HKG)","short":"EST","color":"#1e40af","accent":"#ffffff","stars":0,"rating":78}
]

ACL_ELITE = [
    {"id":"al_hilal","name":"Al-Hilal SFC (KSA)","short":"HIL","color":"#1d4ed8","accent":"#ffffff","stars":4,"rating":93},
    {"id":"al_ittihad","name":"Al-Ittihad (KSA)","short":"ITT","color":"#eab308","accent":"#111827","stars":2,"rating":91},
    {"id":"al_nassr","name":"Al-Nassr FC (KSA)","short":"NAS","color":"#facc15","accent":"#1d4ed8","stars":0,"rating":91},
    {"id":"vissel","name":"Vissel Kobe (JPN)","short":"VIS","color":"#881337","accent":"#ffffff","stars":1,"rating":88},
    {"id":"ulsan","name":"Ulsan HD FC (KOR)","short":"ULS","color":"#1e40af","accent":"#facc15","stars":2,"rating":87},
    {"id":"jdt","name":"Johor Darul Ta'zim (MAS)","short":"JDT","color":"#1e3a8a","accent":"#dc2626","stars":1,"rating":85},
    {"id":"buriram","name":"Buriram United (THA)","short":"BUR","color":"#1e3a8a","accent":"#ffffff","stars":1,"rating":84},
    {"id":"shanghai","name":"Shanghai Port (CHN)","short":"SHP","color":"#dc2626","accent":"#facc15","stars":1,"rating":86}
]

MARKET = [
    {"id":"tm_1","name":"Jay Idzes","pos":"DF","ovr":85,"age":24,"nat":"IDN","cat":"TIMNAS","club":"Venezia FC","val":18000000000,"wage":180000000},
    {"id":"tm_2","name":"Mees Hilgers","pos":"DF","ovr":86,"age":23,"nat":"IDN","cat":"TIMNAS","club":"FC Twente","val":24000000000,"wage":220000000},
    {"id":"tm_3","name":"Kevin Diks","pos":"DF","ovr":85,"age":28,"nat":"IDN","cat":"TIMNAS","club":"FC Copenhagen","val":20000000000,"wage":200000000},
    {"id":"tm_4","name":"Calvin Verdonk","pos":"DF","ovr":84,"age":27,"nat":"IDN","cat":"TIMNAS","club":"NEC Nijmegen","val":15000000000,"wage":150000000},
    {"id":"tm_5","name":"Thom Haye","pos":"MF","ovr":84,"age":29,"nat":"IDN","cat":"TIMNAS","club":"Almere City","val":14000000000,"wage":145000000},
    {"id":"tm_6","name":"Maarten Paes","pos":"GK","ovr":85,"age":26,"nat":"IDN","cat":"TIMNAS","club":"FC Dallas","val":16000000000,"wage":160000000},
    {"id":"tm_7","name":"Marselino Ferdinan","pos":"MF","ovr":82,"age":20,"nat":"IDN","cat":"TIMNAS","club":"Oxford Utd","val":12000000000,"wage":115000000},
    {"id":"tm_8","name":"Ole Romeny","pos":"FW","ovr":84,"age":24,"nat":"IDN","cat":"TIMNAS","club":"Oxford Utd","val":17000000000,"wage":170000000},
    {"id":"tm_9","name":"Ragnar Oratmangoen","pos":"FW","ovr":83,"age":26,"nat":"IDN","cat":"TIMNAS","club":"FCV Dender","val":13000000000,"wage":130000000},
    {"id":"tm_10","name":"Eliano Reijnders","pos":"MF","ovr":82,"age":24,"nat":"IDN","cat":"TIMNAS","club":"PEC Zwolle","val":11500000000,"wage":115000000},
    {"id":"tm_11","name":"Justin Hubner","pos":"DF","ovr":82,"age":21,"nat":"IDN","cat":"TIMNAS","club":"Wolves U21","val":11000000000,"wage":110000000},
    {"id":"tm_12","name":"Sandy Walsh","pos":"DF","ovr":83,"age":29,"nat":"IDN","cat":"TIMNAS","club":"KV Mechelen","val":12500000000,"wage":125000000},
    {"id":"tm_13","name":"Ivar Jenner","pos":"MF","ovr":82,"age":20,"nat":"IDN","cat":"TIMNAS","club":"FC Utrecht","val":11000000000,"wage":110000000},
    {"id":"tm_14","name":"Nathan Tjoe-A-On","pos":"DF","ovr":81,"age":23,"nat":"IDN","cat":"TIMNAS","club":"Swansea City","val":10000000000,"wage":100000000},
    {"id":"tm_15","name":"Rafael Struick","pos":"FW","ovr":81,"age":21,"nat":"IDN","cat":"TIMNAS","club":"Brisbane Roar","val":9500000000,"wage":95000000},
    {"id":"tm_16","name":"Pratama Arhan","pos":"DF","ovr":80,"age":23,"nat":"IDN","cat":"TIMNAS","club":"Bangkok Utd","val":8500000000,"wage":85000000},
    {"id":"tm_17","name":"Asnawi Mangkualam","pos":"DF","ovr":81,"age":25,"nat":"IDN","cat":"TIMNAS","club":"Port FC","val":9000000000,"wage":90000000},
    {"id":"tm_18","name":"Emil Audero","pos":"GK","ovr":85,"age":27,"nat":"IDN","cat":"TIMNAS","club":"Como 1907","val":19000000000,"wage":185000000},
    {"id":"tm_19","name":"Joey Pelupessy","pos":"MF","ovr":82,"age":31,"nat":"IDN","cat":"TIMNAS","club":"Lommel SK","val":10000000000,"wage":105000000},
    {"id":"tm_20","name":"Dean James","pos":"DF","ovr":82,"age":24,"nat":"IDN","cat":"TIMNAS","club":"Go Ahead Eagles","val":12000000000,"wage":120000000},
    {"id":"tm_21","name":"Son Heung-min","pos":"FW","ovr":91,"age":32,"nat":"KOR","cat":"ASIA","club":"Tottenham","val":42000000000,"wage":380000000},
    {"id":"tm_22","name":"Kaoru Mitoma","pos":"FW","ovr":88,"age":27,"nat":"JPN","cat":"ASIA","club":"Brighton","val":36000000000,"wage":310000000},
    {"id":"tm_23","name":"Takefusa Kubo","pos":"MF","ovr":88,"age":23,"nat":"JPN","cat":"ASIA","club":"Real Sociedad","val":38000000000,"wage":320000000},
    {"id":"tm_24","name":"Kim Min-jae","pos":"DF","ovr":89,"age":28,"nat":"KOR","cat":"ASIA","club":"Bayern Munich","val":40000000000,"wage":350000000},
    {"id":"tm_25","name":"Wataru Endo","pos":"MF","ovr":86,"age":31,"nat":"JPN","cat":"ASIA","club":"Liverpool","val":26000000000,"wage":250000000},
    {"id":"tm_26","name":"Lee Kang-in","pos":"MF","ovr":87,"age":23,"nat":"KOR","cat":"ASIA","club":"PSG","val":34000000000,"wage":290000000},
    {"id":"tm_27","name":"Salem Al-Dawsari","pos":"FW","ovr":85,"age":33,"nat":"KSA","cat":"ASIA","club":"Al-Hilal","val":21000000000,"wage":220000000},
    {"id":"tm_28","name":"Arif Aiman","pos":"FW","ovr":82,"age":22,"nat":"MAS","cat":"ASIA","club":"JDT","val":11000000000,"wage":110000000},
    {"id":"tm_29","name":"Zion Suzuki","pos":"GK","ovr":84,"age":22,"nat":"JPN","cat":"ASIA","club":"Parma","val":18000000000,"wage":165000000},
    {"id":"tm_30","name":"Cristiano Ronaldo","pos":"FW","ovr":93,"age":39,"nat":"POR","cat":"WORLD","club":"Al-Nassr","val":60000000000,"wage":650000000},
    {"id":"tm_31","name":"Lionel Messi","pos":"FW","ovr":93,"age":37,"nat":"ARG","cat":"WORLD","club":"Inter Miami","val":60000000000,"wage":650000000},
    {"id":"tm_32","name":"Kylian Mbappe","pos":"FW","ovr":95,"age":26,"nat":"FRA","cat":"WORLD","club":"Real Madrid","val":95000000000,"wage":850000000},
    {"id":"tm_33","name":"Erling Haaland","pos":"FW","ovr":95,"age":24,"nat":"NOR","cat":"WORLD","club":"Man City","val":95000000000,"wage":850000000},
    {"id":"tm_34","name":"Vinicius Junior","pos":"FW","ovr":95,"age":24,"nat":"BRA","cat":"WORLD","club":"Real Madrid","val":92000000000,"wage":820000000},
    {"id":"tm_35","name":"Jude Bellingham","pos":"MF","ovr":94,"age":21,"nat":"ENG","cat":"WORLD","club":"Real Madrid","val":90000000000,"wage":800000000},
    {"id":"tm_36","name":"Lamine Yamal","pos":"FW","ovr":92,"age":17,"nat":"ESP","cat":"WORLD","club":"Barcelona","val":85000000000,"wage":680000000},
    {"id":"tm_37","name":"Kevin De Bruyne","pos":"MF","ovr":92,"age":33,"nat":"BEL","cat":"WORLD","club":"Man City","val":52000000000,"wage":550000000 
    {"id":"tm_38","name":"Rodri","pos":"MF","ovr":94,"age":28,"nat":"ESP","cat":"WORLD","club":"Man City","val":80000000000,"wage":720000000},
    {"id":"tm_39","name":"Mohamed Salah","pos":"FW","ovr":92,"age":32,"nat":"EGY","cat":"WORLD","club":"Liverpool","val":55000000000,"wage":580000000},
    {"id":"tm_40","name":"Harry Kane","pos":"FW","ovr":93,"age":31,"nat":"ENG","cat":"WORLD","club":"Bayern Munich","val":68000000000,"wage":640000000},
    {"id":"tm_41","name":"Neymar Jr","pos":"FW","ovr":90,"age":32,"nat":"BRA","cat":"WORLD","club":"Al-Hilal","val":48000000000,"wage":520000000},
    {"id":"tm_42","name":"Karim Benzema","pos":"FW","ovr":90,"age":36,"nat":"FRA","cat":"WORLD","club":"Al-Ittihad","val":42000000000,"wage":480000000},
    {"id":"tm_43","name":"Virgil van Dijk","pos":"DF","ovr":92,"age":33,"nat":"NED","cat":"WORLD","club":"Liverpool","val":50000000000,"wage":520000000},
    {"id":"tm_44","name":"William Saliba","pos":"DF","ovr":91,"age":23,"nat":"FRA","cat":"WORLD","club":"Arsenal","val":65000000000,"wage":560000000},
    {"id":"tm_45","name":"Alisson Becker","pos":"GK","ovr":92,"age":32,"nat":"BRA","cat":"WORLD","club":"Liverpool","val":54000000000,"wage":500000000},
    {"id":"tm_46","name":"Thibaut Courtois","pos":"GK","ovr":92,"age":32,"nat":"BEL","cat":"WORLD","club":"Real Madrid","val":54000000000,"wage":500000000}
]

SPONSORS = [
    {"id":"sp_bri","name":"Bank BRI","sector":"Perbankan BUMN","per_match":1200000000,"win_bonus":600000000},
    {"id":"sp_indofood","name":"Indofood","sector":"FMCG Nasional","per_match":1500000000,"win_bonus":700000000},
    {"id":"sp_freeport","name":"PT Freeport Indonesia","sector":"Pertambangan","per_match":2000000000,"win_bonus":900000000},
    {"id":"sp_mandiri","name":"Bank Mandiri","sector":"Perbankan Nasional","per_match":1400000000,"win_bonus":650000000},
    {"id":"sp_pegadaian","name":"Pegadaian","sector":"Keuangan BUMN","per_match":900000000,"win_bonus":450000000},
    {"id":"sp_astra","name":"Astra International","sector":"Industri","per_match":1650000000,"win_bonus":750000000},
    {"id":"sp_pertamina","name":"Pertamina","sector":"Energi BUMN","per_match":1900000000,"win_bonus":850000000},
    {"id":"sp_emirates","name":"Fly Emirates","sector":"Maskapai Global","per_match":2800000000,"win_bonus":1200000000}
]

APPARELS = [
    {"id":"ap_erspo","name":"Erspo","origin":"Indonesia 🇮🇩","per_match":550000000,"merch_bonus":350000000},
    {"id":"ap_mills","name":"Mills Sport","origin":"Indonesia 🇮🇩","per_match":500000000,"merch_bonus":320000000},
    {"id":"ap_specs","name":"Specs Indonesia","origin":"Indonesia 🇮🇩","per_match":480000000,"merch_bonus":300000000},
    {"id":"ap_ortus","name":"Ortuseight","origin":"Indonesia 🇮🇩","per_match":480000000,"merch_bonus":310000000},
    {"id":"ap_riors","name":"Riors","origin":"Indonesia 🇮🇩","per_match":420000000,"merch_bonus":260000000},
    {"id":"ap_djsport","name":"DJ Sport","origin":"Indonesia 🇮🇩","per_match":380000000,"merch_bonus":230000000},
    {"id":"ap_adhoc","name":"Adhoc Apparel","origin":"Indonesia 🇮🇩","per_match":370000000,"merch_bonus":220000000},
    {"id":"ap_calci","name":"Calci Indonesia","origin":"Indonesia 🇮🇩","per_match":360000000,"merch_bonus":210000000},
    {"id":"ap_910","name":"910 Nineten","origin":"Indonesia 🇮🇩","per_match":400000000,"merch_bonus":250000000},
    {"id":"ap_juara","name":"Juara Apparel","origin":"Indonesia 🇮🇩","per_match":350000000,"merch_bonus":200000000},
    {"id":"ap_tiento","name":"Tiento Indonesia","origin":"Indonesia 🇮🇩","per_match":340000000,"merch_bonus":195000000},
    {"id":"ap_etams","name":"Etams Indonesia","origin":"Indonesia 🇮🇩","per_match":390000000,"merch_bonus":240000000},
    {"id":"ap_warrix","name":"Warrix","origin":"Thailand 🇹🇭","per_match":520000000,"merch_bonus":300000000},
    {"id":"ap_kelme","name":"Kelme","origin":"Spanyol 🇪🇸","per_match":600000000,"merch_bonus":350000000},
    {"id":"ap_puma","name":"Puma","origin":"Jerman 🇩🇪","per_match":900000000,"merch_bonus":500000000},
    {"id":"ap_adidas","name":"Adidas","origin":"Jerman 🇩🇪","per_match":1100000000,"merch_bonus":650000000},
    {"id":"ap_nike","name":"Nike","origin":"AS 🇺🇸","per_match":1150000000,"merch_bonus":680000000}
]

COACHES = [
    {"id":"co_local","name":"Coach Lokal Lisensi A PSSI","nat":"IDN","style":"Seimbang","ovr_bonus":0,"cost":0,"salary":150000000},
    {"id":"co_indra","name":"Indra Sjafri","nat":"IDN","style":"Tiki-Taka & Muda","ovr_bonus":2,"cost":3000000000,"salary":250000000},
    {"id":"co_bojan","name":"Bojan Hodak","nat":"CRO","style":"Counter Attack","ovr_bonus":3,"cost":5000000000,"salary":350000000},
    {"id":"co_munster","name":"Paul Munster","nat":"NIR","style":"High Pressing","ovr_bonus":3,"cost":5000000000,"salary":350000000},
    {"id":"co_sty","name":"Shin Tae-yong","nat":"KOR","style":"Stamina & Transisi","ovr_bonus":5,"cost":10000000000,"salary":550000000},
    {"id":"co_kluivert","name":"Patrick Kluivert","nat":"NED","style":"Total Football","ovr_bonus":5,"cost":11000000000,"salary":600000000},
    {"id":"co_mourinho","name":"Jose Mourinho","nat":"POR","style":"Parkir Bus Juara","ovr_bonus":7,"cost":22000000000,"salary":950000000},
    {"id":"co_guardiola","name":"Pep Guardiola","nat":"ESP","style":"Dominasi Bola","ovr_bonus":8,"cost":28000000000,"salary":1200000000}
]

MEDICAL = [
    {"id":"med_basic","name":"Fisioterapis Standar Klub","recovery_bonus":5,"injury_shield":10,"cost":0,"salary":80000000},
    {"id":"med_pro","name":"Sport Science Nasional","recovery_bonus":12,"injury_shield":35,"cost":3500000000,"salary":180000000},
    {"id":"med_europe","name":"Klinik Medis Eropa","recovery_bonus":22,"injury_shield":65,"cost":9000000000,"salary":350000000}
]

SCOUTS = [
    {"id":"sc_local","name":"Pemandu Bakat Regional","youth_boost":0,"cost":0,"salary":75000000},
    {"id":"sc_national","name":"Jaringan Scouting Nusantara","youth_boost":3,"cost":3000000000,"salary":160000000},
    {"id":"sc_global","name":"Direktur Scouting Global","youth_boost":6,"cost":8500000000,"salary":320000000}
]

WEATHERS = [
    {"id":"cerah","name":"Cerah Berawan","icon":"☀️","stamina_mod":0,"goal_mod":0.1},
    {"id":"panas","name":"Panas Terik Tropis","icon":"🔥","stamina_mod":5,"goal_mod":0.0},
    {"id":"hujan","name":"Hujan Deras","icon":"🌧️","stamina_mod":4,"goal_mod":0.25},
    {"id":"sejuk","name":"Malam Sejuk","icon":"🌙","stamina_mod":-2,"goal_mod":0.15}
]

TIMES = ["15:30 WIB (Sore)", "19:00 WIB (Malam Prime Time)", "20:30 WIB (Malam)"]
INJURIES = [("Cedera Hamstring", 1, "Ringan"), ("Keseleo Engkel", 1, "Ringan"), ("Robekan Otot Paha", 2, "Sedang"), ("Cedera Lutut MCL", 3, "Berat")]

def sim_engine(home, away, tactic="balanced", mentality="normal", coach_bonus=0, injury_shield=10, ko=False):
    w = random.choice(WEATHERS)
    t_str = random.choice(TIMES)
    h_rat = home.get("rating", 78) + coach_bonus + 2 + (2 if tactic == "attack" else (1 if tactic == "defend" else 0))
    a_rat = away.get("rating", 78) + (1 if tactic == "attack" else (-1 if tactic == "defend" else 0))
    diff = h_rat - a_rat

    hg = min(6, max(0, int(random.gauss(max(0.35, 1.35 + diff * 0.11 + w["goal_mod"]), 0.95))))
    ag = min(5, max(0, int(random.gauss(max(0.25, 1.15 - diff * 0.09 + w["goal_mod"] * 0.5), 0.9))))
    ph, pa = None, None
    if ko and hg == ag:
        ph, pa = random.randint(3, 5), random.randint(2, 5)
        if ph == pa:
            if random.random() < 0.52 + diff * 0.02: ph += 1
            else: pa += 1

    sq = home.get("squad", [])
    fit = [p for p in sq if p.get("is_starter") and not p.get("injury")] or [p for p in sq if not p.get("injury")]
    bench = [p for p in sq if not p.get("is_starter") and not p.get("injury")]
    scorers = [p["name"] for p in fit if p["pos"] in ("FW", "MF")] or [p["name"] for p in fit]

    evs = [{"min": 1, "type": "info", "text": f"Kick-off {t_str}! Cuaca {w['icon']} {w['name']}."}]
    for _ in range(hg):
        evs.append({"min": random.randint(4, 90), "type": "goal", "text": f"⚽ GOL! {random.choice(scorers) if scorers else 'Striker'} membobol gawang {away['name']}!"})
    for _ in range(ag):
        evs.append({"min": random.randint(5, 90), "type": "goal_away", "text": f"⚽ Gol balasan dari {away['name']}."})
    if len(fit) >= 2 and bench:
        so, si = random.choice(fit[1:]), random.choice(bench)
        evs.append({"min": random.randint(60, 82), "type": "sub", "text": f"🔄 Substitusi: {si['name']} menggantikan {so['name']}."})

    inj_p = None
    inj_prob = (0.24 if mentality == "hard" else (0.14 if mentality == "normal" else 0.08)) * (1.0 - injury_shield / 100.0)
    if fit and random.random() < inj_prob:
        v = random.choice(fit)
        it, iw, isev = random.choice(INJURIES)
        inj_p = {"id": v["id"], "name": v["name"], "type": it, "weeks": iw, "severity": isev}
        evs.append({"min": random.randint(25, 85), "type": "injury", "text": f"🚑 CEDERA! {v['name']} mengalami {it} (Absen {iw} pekan)."})

    red_p = None
    if fit and random.random() < (0.75 if mentality == "hard" else 0.4):
        evs.append({"min": random.randint(15, 88), "type": "yellow", "text": f"🟨 Kartu Kuning untuk {random.choice(fit)['name']}."})
    if fit and random.random() < (0.22 if mentality == "hard" else 0.06):
        rp = random.choice(fit)
        red_p = {"id": rp["id"], "name": rp["name"]}
        evs.append({"min": random.randint(35, 89), "type": "red", "text": f"🟥 KARTU MERAH! {rp['name']} diusir wasit & skorsing 1 laga!"})

    sanc = None
    if random.random() < (0.28 if mentality == "hard" else 0.1):
        st, sf, sfl, sd = random.choice([
            ("Penyalaan Flare Suporter", 150000000, 3, "⚖️ Komdis PSSI menjatuhkan denda Rp 150 Jt akibat flare."),
            ("Pelemparan Botol", 100000000, 2, "⚖️ Komdis PSSI menjatuhkan denda Rp 100 Jt akibat pelemparan botol."),
            ("Protes Keras Ofisial", 75000000, 1, "⚖️ Komdis PSSI menjatuhkan denda Rp 75 Jt atas protes bangku cadangan.")
        ])
        sanc = {"title": st, "fine": sf, "fans_loss": sfl, "desc": sd}
        evs.append({"min": 90, "type": "sanction", "text": sd})

    if ph is not None:
        evs.append({"min": 90, "type": "goal", "text": f"🎯 Adu Penalti: {home['name']} ({ph}) vs ({pa}) {away['name']}!"})
    evs.sort(key=lambda x: x["min"])

    poss = max(35, min(68, 50 + diff * 2 + (4 if tactic == "possession" else 0)))
    return {
        "home_goals": hg, "away_goals": ag, "pen_home": ph, "pen_away": pa, "weather": w, "match_time": t_str,
        "events": evs, "pssi_sanction": sanc, "red_card_player": red_p, "injured_player": inj_p,
        "attendance": random.randint(14000, 42000),
        "stats": {"possession_home": poss, "possession_away": 100 - poss, "shots_home": max(hg+2, int(poss/4.5)+2), "shots_away": max(ag+1, int((100-poss)/4.8)+1), "motm": random.choice(fit)["name"] if fit else "Kapten", "motm_rating": round(min(9.8, 7.6 + hg*0.35 + random.uniform(0.1, 0.5)), 1)}
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/init_data")
def init_data():
    return jsonify({"liga1": LIGA1, "liga2": LIGA2, "acl_two": ACL_TWO, "acl_elite": ACL_ELITE, "market": MARKET, "sponsors": SPONSORS, "apparels": APPARELS, "coaches": COACHES, "medical": MEDICAL, "scouts": SCOUTS, "weathers": WEATHERS, "times": TIMES})

@app.route("/api/simulate_match", methods=["POST"])
def simulate_match():
    d = request.get_json(force=True)
    res = sim_engine(d["home"], d["away"], d.get("tactic","balanced"), d.get("mentality","normal"), d.get("coach_bonus",0), d.get("injury_shield",10), False)
    others = [c for c in d.get("league_clubs", []) if c["id"] not in (d["home"]["id"], d["away"]["id"])]
    random.shuffle(others)
    res["other_results"] = [{"home_id": others[i]["id"], "away_id": others[i+1]["id"], "home_goals": max(0, int(random.gauss(1.3, 0.9))), "away_goals": max(0, int(random.gauss(1.2, 0.9)))} for i in range(0, len(others)-1, 2)]
    return jsonify(res)

@app.route("/api/simulate_knockout", methods=["POST"])
def simulate_knockout():
    d = request.get_json(force=True)
    uid = d.get("user_club_id")
    upd, u_evs = [], []
    for m in d.get("matches", []):
        t1, t2 = m["team1"], m["team2"]
        if t1["id"] == uid or t2["id"] == uid:
            is_h = t1["id"] == uid
            r = sim_engine(t1 if is_h else t2, t2 if is_h else t1, d.get("tactic","balanced"), d.get("mentality","normal"), d.get("coach_bonus",0), d.get("injury_shield",10), True)
            s1, s2 = (r["home_goals"], r["away_goals"]) if is_h else (r["away_goals"], r["home_goals"])
            p1, p2 = (r["pen_home"], r["pen_away"]) if is_h else (r["pen_away"], r["pen_home"])
            u_evs = r["events"]
        else:
            s1, s2, p1, p2 = max(0, int(random.gauss(1.3, 0.9))), max(0, int(random.gauss(1.2, 0.9))), None, None
            if s1 == s2: p1, p2 = 5, 4
        win = t1 if (s1 > s2 or (s1 == s2 and (p1 or 0) > (p2 or 0))) else t2
        upd.append({"team1": t1, "team2": t2, "score1": s1, "score2": s2, "pen1": p1, "pen2": p2, "winner": win})
    return jsonify({"matches": upd, "user_events": u_evs})
