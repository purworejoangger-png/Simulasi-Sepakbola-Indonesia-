import os, random
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

TRAITS_POOL = {
    "GK": ["Refleks Kilat", "Komandan Kotak Penalti", "Spesialis Penalti", "Distribusi Bola"],
    "DF": ["Tembok Kokoh", "Raja Tekel", "Duel Udara", "Kapten Vokal", "Bek Modern"],
    "MF": ["Playmaker Jenius", "Mesin Lari", "Umpan Terobosan", "Pekerja Keras", "Tembakan Jarak Jauh"],
    "FW": ["Penyelesai Klinis", "Dribel Cepat", "Predator Kotak Penalti", "Target Man", "Temperamental"]
}

def mk_sq(pfx, ovr, stars):
    tpl = [("GK",1),("DF",1),("DF",1),("DF",1),("DF",1),("MF",1),("MF",1),("MF",1),("FW",1),("FW",1),("FW",1),("GK",0),("DF",0),("MF",0),("FW",0),("FW",0)]
    res = []
    for i, (pos, st) in enumerate(tpl):
        if i < len(stars):
            n, p, o, a, nat, tr = stars[i]
        else:
            n, p, o, a, nat = f"{pfx} Player {i+1}", pos, max(68, min(86, ovr + random.randint(-3, 2))), random.randint(20, 31), "IDN"
            tr = random.choice(TRAITS_POOL[pos])
        res.append({
            "id": f"{pfx.lower()}_{i+1}", "name": n, "pos": p, "ovr": o, "age": a, "nat": nat,
            "trait": tr, "morale": random.randint(78, 92), "goals": 0, "assists": 0,
            "val": max(1500000000, (o-60)*650000000), "wage": max(35000000, int((o-62)*8500000)),
            "contract": random.randint(2, 4), "stamina": 100, "is_starter": bool(st), "suspended": 0, "injury": None
        })
    return res

LIGA1 = [
    {"id":"persib","name":"PERSIB BANDUNG","short":"PSB","league":"LIGA1","color":"#003399","accent":"#ffffff","kit":"stripes","stars":4,"rating":83,"stadium":"Gelora Bandung Lautan Api","squad":mk_sq("PSB",83,[
        ("Kevin Ray Mendoza","GK",82,30,"PHI","Refleks Kilat"),("Nick Kuipers","DF",83,32,"NED","Tembok Kokoh"),("Gustavo Franca","DF",82,28,"BRA","Duel Udara"),("Edo Febriansah","DF",80,27,"IDN","Bek Modern"),("Henhen Herdiana","DF",79,29,"IDN","Raja Tekel"),
        ("Marc Klok","MF",83,31,"IDN","Kapten Vokal"),("Tyronne del Pino","MF",84,33,"ESP","Playmaker Jenius"),("Mateo Kocijan","MF",80,29,"CRO","Pekerja Keras"),
        ("Ciro Alves","FW",85,35,"BRA","Dribel Cepat"),("David da Silva","FW",86,35,"BRA","Penyelesai Klinis"),("Beckham Putra","FW",80,23,"IDN","Mesin Lari"),
        ("Teja Paku Alam","GK",79,30,"IDN","Spesialis Penalti"),("Rachmat Irianto","DF",80,25,"IDN","Pekerja Keras"),("Adam Alis","MF",80,31,"IDN","Tembakan Jarak Jauh"),("Dimas Drajad","FW",80,27,"IDN","Target Man")
    ])},
    {"id":"persija","name":"PERSIJA JAKARTA","short":"PSJ","league":"LIGA1","color":"#dc2626","accent":"#facc15","kit":"solid","stars":2,"rating":82,"stadium":"Jakarta International Stadium","squad":mk_sq("PSJ",82,[
        ("Andritany Ardhiyasa","GK",80,33,"IDN","Komandan Kotak Penalti"),("Rizky Ridho","DF",84,23,"IDN","Kapten Vokal"),("Ondrej Kudela","DF",82,37,"CZE","Tembok Kokoh"),("Muhammad Ferarri","DF",80,21,"IDN","Duel Udara"),("Firza Andika","DF",79,25,"IDN","Raja Tekel"),
        ("Maciej Gajos","MF",82,33,"POL","Tembakan Jarak Jauh"),("Ramon Bueno","MF",81,29,"ESP","Umpan Terobosan"),("Hanif Sjahbandi","MF",79,27,"IDN","Pekerja Keras"),
        ("Ryo Matsumura","FW",83,30,"JPN","Dribel Cepat"),("Gustavo Almeida","FW",84,28,"BRA","Predator Kotak Penalti"),("Witan Sulaeman","FW",81,23,"IDN","Mesin Lari"),
        ("Carlos Eduardo","GK",79,32,"BRA","Refleks Kilat"),("Hansamu Yama","DF",78,29,"IDN","Duel Udara"),("Marko Simic","FW",80,36,"CRO","Target Man")
    ])},
    {"id":"persebaya","name":"PERSEBAYA SURABAYA","short":"PBY","league":"LIGA1","color":"#047857","accent":"#facc15","kit":"stripes","stars":2,"rating":82,"stadium":"Gelora Bung Tomo","squad":mk_sq("PBY",82,[
        ("Ernando Ari","GK",83,22,"IDN","Spesialis Penalti"),("Slavko Damjanovic","DF",81,32,"MNE","Tembok Kokoh"),("Kadek Raditya","DF",79,25,"IDN","Raja Tekel"),("Ardi Idrus","DF",79,31,"IDN","Pekerja Keras"),("Catur Pamungkas","DF",78,25,"IDN","Bek Modern"),
        ("Francisco Rivera","MF",84,30,"MEX","Playmaker Jenius"),("Mohammed Rashid","MF",82,29,"PLE","Tembakan Jarak Jauh"),("Gilson Costa","MF",80,28,"POR","Mesin Lari"),
        ("Bruno Moreira","FW",84,25,"BRA","Dribel Cepat"),("Flavio Silva","FW",83,28,"POR","Penyelesai Klinis"),("Malik Risaldi","FW",81,28,"IDN","Mesin Lari"),
        ("Toni Firmansyah","MF",78,19,"IDN","Umpan Terobosan")
    ])},
    {"id":"arema","name":"AREMA FC","short":"ARE","league":"LIGA1","color":"#1e3a8a","accent":"#ef4444","kit":"half","stars":1,"rating":80,"stadium":"Stadion Kanjuruhan","squad":mk_sq("ARE",80,[
        ("Lucas Frigeri","GK",81,35,"BRA","Refleks Kilat"),("Thales Lira","DF",80,31,"BRA","Duel Udara"),("Choi Bo-kyung","DF",79,36,"KOR","Tembok Kokoh"),("Johan Alfarizi","DF",79,34,"IDN","Kapten Vokal"),("Achmad Maulana","DF",78,21,"IDN","Mesin Lari"),
        ("Wiliam Marcilio","MF",82,28,"BRA","Playmaker Jenius"),("Pablo Oliveira","MF",80,29,"BRA","Raja Tekel"),("Arkhan Fikri","MF",80,20,"IDN","Umpan Terobosan"),
        ("Dalberto Luan","FW",82,30,"BRA","Predator Kotak Penalti"),("Charles Lokolingoy","FW",81,27,"AUS","Dribel Cepat"),("Dedik Setiawan","FW",78,30,"IDN","Pekerja Keras")
    ])},
    {"id":"bali","name":"BALI UNITED","short":"BAL","league":"LIGA1","color":"#b91c1c","accent":"#111827","kit":"sash","stars":2,"rating":81,"stadium":"Stadion Kapten I Wayan Dipta","squad":mk_sq("BAL",81,[
        ("Adilson Maringa","GK",82,34,"BRA","Refleks Kilat"),("Elias Dolah","DF",81,31,"THA","Duel Udara"),("Brandon Wilson","DF",79,27,"AUS","Raja Tekel"),("Ricky Fajrin","DF",80,29,"IDN","Kapten Vokal"),("Andhika Wijaya","DF",78,28,"IDN","Pekerja Keras"),
        ("Mitsuru Maruoka","MF",81,28,"JPN","Playmaker Jenius"),("Kenzo Nambu","MF",81,32,"JPN","Tembakan Jarak Jauh"),("Made Tito","MF",79,21,"IDN","Mesin Lari"),
        ("Privat Mbarga","FW",83,32,"CAM","Dribel Cepat"),("Everton Nascimento","FW",82,31,"BRA","Target Man"),("Irfan Jaya","FW",80,28,"IDN","Penyelesai Klinis")
    ])},
    {"id":"borneo","name":"BORNEO FC","short":"BOR","league":"LIGA1","color":"#ea580c","accent":"#111827","kit":"solid","stars":1,"rating":82,"stadium":"Stadion Segiri","squad":mk_sq("BOR",82,[
        ("Nadeo Argawinata","GK",82,27,"IDN","Spesialis Penalti"),("Christophe Nduwarugira","DF",81,30,"BDI","Tembok Kokoh"),("Gabriel Furtado","DF",81,25,"BRA","Duel Udara"),("Leo Guntara","DF",79,30,"IDN","Raja Tekel"),("Fajar Fathur Rahman","DF",80,22,"IDN","Bek Modern"),
        ("Kei Hirose","MF",82,29,"JPN","Mesin Lari"),("Berguinho","MF",83,27,"BRA","Playmaker Jenius"),("Rivaldo Pakpahan","MF",79,21,"IDN","Pekerja Keras"),
        ("Stefano Lilipaly","FW",83,34,"IDN","Kapten Vokal"),("Leo Gaucho","FW",83,23,"BRA","Penyelesai Klinis"),("Mariano Peralta","FW",82,26,"ARG","Dribel Cepat")
    ])},
    {"id":"psm","name":"PSM MAKASSAR","short":"PSM","league":"LIGA1","color":"#7f1d1d","accent":"#facc15","kit":"solid","stars":2,"rating":81,"stadium":"Gelora B.J. Habibie","squad":mk_sq("PSM",81,[
        ("Hilmansyah","GK",79,27,"IDN","Refleks Kilat"),("Yuran Fernandes","DF",84,30,"CPV","Kapten Vokal"),("Aloisio Neto","DF",81,27,"BRA","Tembok Kokoh"),("Syahrul Lasinari","DF",78,25,"IDN","Raja Tekel"),("Victor Luiz","DF",80,27,"BRA","Bek Modern"),
        ("Latyr Fall","MF",80,30,"SEN","Mesin Lari"),("Akbar Tanjung","MF",79,31,"IDN","Pekerja Keras"),("Ananda Raehan","MF",79,21,"IDN","Umpan Terobosan"),
        ("Nermin Haljeta","FW",82,27,"SVN","Target Man"),("Tito Okello","FW",80,28,"SSD","Duel Udara"),("Dzaky Asraf","FW",79,21,"IDN","Dribel Cepat")
    ])},
    {"id":"dewa","name":"DEWA UNITED","short":"DEW","league":"LIGA1","color":"#111827","accent":"#eab308","kit":"sash","stars":0,"rating":83,"stadium":"Indomilk Arena","squad":mk_sq("DEW",83,[
        ("Sonny Stevens","GK",82,32,"NED","Distribusi Bola"),("Angelo Meneses","DF",81,31,"POR","Tembok Kokoh"),("Risto Mitrevski","DF",81,33,"MKD","Kapten Vokal"),("Alta Ballah","DF",79,24,"IDN","Bek Modern"),("Reva Adi Utama","DF",79,28,"IDN","Raja Tekel"),
        ("Alexis Messidoro","MF",84,27,"ARG","Playmaker Jenius"),("Hugo Gomes Jaja","MF",83,29,"BRA","Tembakan Jarak Jauh"),("Ricky Kambuaya","MF",81,28,"IDN","Dribel Cepat"),
        ("Egy Maulana Vikri","FW",83,24,"IDN","Dribel Cepat"),("Alex Martins","FW",84,31,"BRA","Penyelesai Klinis"),("Taisei Marukawa","FW",83,27,"JPN","Mesin Lari")
    ])},
    {"id":"madura","name":"MADURA UNITED","short":"MAD","league":"LIGA1","color":"#dc2626","accent":"#ffffff","kit":"hoops","stars":0,"rating":79,"stadium":"Gelora Bangkalan","squad":mk_sq("MAD",79,[("Wagner dos Santos","GK",79,34,"BRA","Refleks Kilat"),("Pedro Monteiro","DF",80,30,"POR","Tembok Kokoh"),("Jordy Wehrmann","MF",82,25,"NED","Playmaker Jenius"),("Lulinha","FW",82,34,"BRA","Dribel Cepat")])},
    {"id":"malut","name":"MALUT UNITED","short":"MAL","league":"LIGA1","color":"#991b1b","accent":"#facc15","kit":"solid","stars":0,"rating":80,"stadium":"Gelora Kie Raha","squad":mk_sq("MAL",80,[("Wahyu Prasetyo","DF",80,26,"IDN","Tembok Kokoh"),("Yance Sayuri","DF",81,27,"IDN","Mesin Lari"),("Yakob Sayuri","FW",83,27,"IDN","Dribel Cepat")])},
    {"id":"psis","name":"PSIS SEMARANG","short":"SMG","league":"LIGA1","color":"#1d4ed8","accent":"#facc15","kit":"solid","stars":1,"rating":79,"stadium":"Stadion Jatidiri","squad":mk_sq("SMG",79,[("Adi Satryo","GK",80,23,"IDN","Refleks Kilat"),("Alfeandra Dewangga","DF",81,23,"IDN","Bek Modern"),("Septian David","MF",80,28,"IDN","Playmaker Jenius"),("Gali Freitas","FW",82,20,"TLS","Dribel Cepat")])},
    {"id":"persis","name":"PERSIS SOLO","short":"SOL","league":"LIGA1","color":"#b91c1c","accent":"#facc15","kit":"solid","stars":1,"rating":79,"stadium":"Stadion Manahan","squad":mk_sq("SOL",79,[("Muhammad Riyandi","GK",80,24,"IDN","Refleks Kilat"),("Sho Yamamoto","MF",81,28,"JPN","Mesin Lari"),("Moussa Sidibe","FW",82,30,"MLI","Dribel Cepat"),("Ramadhan Sananta","FW",82,22,"IDN","Penyelesai Klinis")])},
    {"id":"pss","name":"PSS SLEMAN","short":"PSS","league":"LIGA1","color":"#15803d","accent":"#ffffff","kit":"stripes","stars":0,"rating":78,"stadium":"Stadion Maguwoharjo","squad":mk_sq("PSS",78,[("Cleberson","DF",81,32,"BRA","Tembok Kokoh"),("Gustavo Tocantins","FW",81,28,"BRA","Penyelesai Klinis"),("Hokky Caraka","FW",80,20,"IDN","Target Man")])},
    {"id":"persita","name":"PERSITA TANGERANG","short":"PTA","league":"LIGA1","color":"#6b21a8","accent":"#ffffff","kit":"solid","stars":0,"rating":78,"stadium":"Indomilk Arena","squad":mk_sq("PTA",78,[("Igor Rodrigues","GK",80,29,"POR","Refleks Kilat"),("Javlon Guseynov","DF",80,33,"UZB","Tembok Kokoh"),("Marios Ogkmpoe","FW",80,30,"GRE","Target Man")])},
    {"id":"persik","name":"PERSIK KEDIRI","short":"PSK","league":"LIGA1","color":"#581c87","accent":"#facc15","kit":"solid","stars":2,"rating":79,"stadium":"Stadion Brawijaya","squad":mk_sq("PSK",79,[("Ze Valente","MF",83,30,"POR","Playmaker Jenius"),("Ezra Walian","FW",80,27,"IDN","Penyelesai Klinis"),("Ramiro Fergonzi","FW",81,35,"ARG","Target Man")])},
    {"id":"barito","name":"BARITO PUTERA","short":"BAR","league":"LIGA1","color":"#eab308","accent":"#111827","kit":"stripes","stars":0,"rating":78,"stadium":"Stadion Demang Lehman","squad":mk_sq("BAR",78,[("Bagas Kaffa","DF",79,22,"IDN","Bek Modern"),("Levy Madinda","MF",81,32,"GAB","Playmaker Jenius"),("Murilo Mendes","FW",81,29,"BRA","Dribel Cepat")])},
    {"id":"psbs","name":"PSBS BIAK","short":"BIA","league":"LIGA1","color":"#0284c7","accent":"#ffffff","kit":"half","stars":0,"rating":78,"stadium":"Stadion Cendrawasih","squad":mk_sq("BIA",78,[("Julian Velazquez","DF",80,34,"ARG","Tembok Kokoh"),("Alexsandro","FW",81,27,"BRA","Penyelesai Klinis")])},
    {"id":"semen","name":"SEMEN PADANG","short":"SPD","league":"LIGA1","color":"#991b1b","accent":"#facc15","kit":"hoops","stars":0,"rating":77,"stadium":"Stadion Haji Agus Salim","squad":mk_sq("SPD",77,[("Bruno Dybal","MF",80,30,"BRA","Playmaker Jenius"),("Kenneth Ngwoke","FW",80,31,"NGA","Target Man")])}
]

LIGA2 = [
    {"id":"psim","name":"PSIM YOGYAKARTA","short":"YOG","league":"LIGA2","color":"#1e40af","accent":"#ffffff","kit":"solid","stars":1,"rating":76,"stadium":"Mandala Krida","squad":mk_sq("YOG",76,[("Rafinha","FW",80,32,"BRA","Penyelesai Klinis")])},
    {"id":"bhayangkara","name":"BHAYANGKARA FC","short":"BFC","league":"LIGA2","color":"#eab308","accent":"#111827","kit":"solid","stars":1,"rating":78,"stadium":"Tri Sanja","squad":mk_sq("BFC",78,[("Matias Mier","MF",81,34,"URU","Tembakan Jarak Jauh"),("Ilija Spasojevic","FW",80,37,"IDN","Target Man")])},
    {"id":"persiraja","name":"PERSIRAJA ACEH","short":"PRJ","league":"LIGA2","color":"#ea580c","accent":"#111827","kit":"stripes","stars":0,"rating":76,"stadium":"Harapan Bangsa","squad":mk_sq("PRJ",76,[("Andik Vermansah","FW",78,33,"IDN","Dribel Cepat")])},
    {"id":"psms","name":"PSMS MEDAN","short":"MDN","league":"LIGA2","color":"#15803d","accent":"#ffffff","kit":"solid","stars":2,"rating":75,"stadium":"Teladan","squad":mk_sq("MDN",75,[("Fabio Gama","MF",78,32,"BRA","Playmaker Jenius")])},
    {"id":"sriwijaya","name":"SRIWIJAYA FC","short":"SFC","league":"LIGA2","color":"#eab308","accent":"#b91c1c","kit":"sash","stars":2,"rating":75,"stadium":"Jakabaring","squad":mk_sq("SFC",75,[("Chencho Gyeltshen","FW",79,28,"BHU","Dribel Cepat")])},
    {"id":"persela","name":"PERSELA LAMONGAN","short":"PSL","league":"LIGA2","color":"#0284c7","accent":"#facc15","kit":"solid","stars":0,"rating":76,"stadium":"Surajaya","squad":mk_sq("PSL",76,[("Ezechiel Ndouassel","FW",80,36,"CHA","Target Man")])},
    {"id":"gresik","name":"GRESIK UNITED","short":"GRS","league":"LIGA2","color":"#eab308","accent":"#15803d","kit":"half","stars":0,"rating":74,"stadium":"Joko Samudro","squad":mk_sq("GRS",74,[("Renan Silva","MF",79,35,"BRA","Playmaker Jenius")])},
    {"id":"deltras","name":"DELTRAS FC","short":"DEL","league":"LIGA2","color":"#b91c1c","accent":"#111827","kit":"solid","stars":0,"rating":75,"stadium":"Gelora Delta","squad":mk_sq("DEL",75,[("Emerson Carioca","FW",78,29,"BRA","Penyelesai Klinis")])},
    {"id":"persipura","name":"PERSIPURA JAYAPURA","short":"PPR","league":"LIGA2","color":"#dc2626","accent":"#111827","kit":"stripes","stars":4,"rating":75,"stadium":"Mandala","squad":mk_sq("PPR",75,[("Boaz Solossa","FW",78,38,"IDN","Kapten Vokal")])},
    {"id":"psps","name":"PSPS PEKANBARU","short":"PKU","league":"LIGA2","color":"#1d4ed8","accent":"#ffffff","kit":"solid","stars":0,"rating":75,"stadium":"Kaharuddin Nasution","squad":mk_sq("PKU",75,[("Omid Popalzay","MF",79,28,"AFG","Playmaker Jenius")])},
    {"id":"bekasi","name":"FC BEKASI CITY","short":"BKS","league":"LIGA2","color":"#111827","accent":"#ef4444","kit":"solid","stars":0,"rating":75,"stadium":"Patriot Candrabhaga","squad":mk_sq("BKS",75,[("Cahya Supriadi","GK",78,21,"IDN","Refleks Kilat")])},
    {"id":"persijap","name":"PERSIJAP JEPARA","short":"JEP","league":"LIGA2","color":"#b91c1c","accent":"#facc15","kit":"solid","stars":0,"rating":74,"stadium":"Gelora Bumi Kartini","squad":mk_sq("JEP",74,[("Rosalvo Junior","FW",78,33,"BRA","Target Man")])}
]

ACL_TWO = [
    {"id":"gamba","name":"Gamba Osaka (JPN)","short":"GAM","color":"#1d4ed8","accent":"#111827","rating":85},
    {"id":"pohang","name":"Pohang Steelers (KOR)","short":"POH","color":"#b91c1c","accent":"#111827","rating":85},
    {"id":"port_fc","name":"Port FC (THA)","short":"PRT","color":"#ea580c","accent":"#1e3a8a","rating":82},
    {"id":"lion_city","name":"Lion City Sailors (SGP)","short":"LCS","color":"#1d4ed8","accent":"#ffffff","rating":81},
    {"id":"selangor","name":"Selangor FC (MAS)","short":"SEL","color":"#dc2626","accent":"#facc15","rating":81},
    {"id":"nam_dinh","name":"Nam Dinh FC (VIE)","short":"NAM","color":"#eab308","accent":"#1d4ed8","rating":80},
    {"id":"kaya_fc","name":"Kaya FC Iloilo (PHI)","short":"KAY","color":"#eab308","accent":"#111827","rating":78},
    {"id":"eastern","name":"Eastern SC (HKG)","short":"EST","color":"#1e40af","accent":"#ffffff","rating":78}
]

ACL_ELITE = [
    {"id":"al_hilal","name":"Al-Hilal SFC (KSA)","short":"HIL","color":"#1d4ed8","accent":"#ffffff","rating":93},
    {"id":"al_ittihad","name":"Al-Ittihad (KSA)","short":"ITT","color":"#eab308","accent":"#111827","rating":91},
    {"id":"al_nassr","name":"Al-Nassr FC (KSA)","short":"NAS","color":"#facc15","accent":"#1d4ed8","rating":91},
    {"id":"vissel","name":"Vissel Kobe (JPN)","short":"VIS","color":"#881337","accent":"#ffffff","rating":88},
    {"id":"ulsan","name":"Ulsan HD FC (KOR)","short":"ULS","color":"#1e40af","accent":"#facc15","rating":87},
    {"id":"jdt","name":"Johor Darul Ta'zim (MAS)","short":"JDT","color":"#1e3a8a","accent":"#dc2626","rating":85},
    {"id":"buriram","name":"Buriram United (THA)","short":"BUR","color":"#1e3a8a","accent":"#ffffff","rating":84},
    {"id":"shanghai","name":"Shanghai Port (CHN)","short":"SHP","color":"#dc2626","accent":"#facc15","rating":86}
]

PRESEASON_TOURS = [
    {"id":"tour_idn","name":"🇮🇩 Nusantara Cup (Bali)", "opps":[("Bali All-Stars",76),("Timnas U-23",79),("JDT Malaysia",83)], "reward":2500000000, "morale_boost":6},
    {"id":"tour_asia","name":"🌏 East Asia Challenge (Tokyo)", "opps":[("FC Tokyo",82),("Ulsan HD",85),("Vissel Kobe",87)], "reward":5500000000, "morale_boost":9},
    {"id":"tour_euro","name":"🇪🇺 European Summer Tour (Belanda)", "opps":[("FC Utrecht",84),("FC Twente",86),("Ajax Amsterdam",89)], "reward":10000000000, "morale_boost":12}
]

MARKET = [
    {"id":"tm_1","name":"Jay Idzes","pos":"DF","ovr":85,"age":24,"nat":"IDN","cat":"TIMNAS","trait":"Kapten Vokal","club":"Venezia FC","val":18000000000,"wage":180000000},
    {"id":"tm_2","name":"Mees Hilgers","pos":"DF","ovr":86,"age":23,"nat":"IDN","cat":"TIMNAS","trait":"Tembok Kokoh","club":"FC Twente","val":24000000000,"wage":220000000},
    {"id":"tm_3","name":"Kevin Diks","pos":"DF","ovr":85,"age":28,"nat":"IDN","cat":"TIMNAS","trait":"Spesialis Penalti","club":"FC Copenhagen","val":20000000000,"wage":200000000},
    {"id":"tm_4","name":"Calvin Verdonk","pos":"DF","ovr":84,"age":27,"nat":"IDN","cat":"TIMNAS","trait":"Mesin Lari","club":"NEC Nijmegen","val":15000000000,"wage":150000000},
    {"id":"tm_5","name":"Thom Haye","pos":"MF","ovr":84,"age":29,"nat":"IDN","cat":"TIMNAS","trait":"Playmaker Jenius","club":"Almere City","val":14000000000,"wage":145000000},
    {"id":"tm_6","name":"Maarten Paes","pos":"GK","ovr":85,"age":26,"nat":"IDN","cat":"TIMNAS","trait":"Refleks Kilat","club":"FC Dallas","val":16000000000,"wage":160000000},
    {"id":"tm_7","name":"Marselino Ferdinan","pos":"MF","ovr":82,"age":20,"nat":"IDN","cat":"TIMNAS","trait":"Dribel Cepat","club":"Oxford Utd","val":12000000000,"wage":115000000},
    {"id":"tm_8","name":"Ole Romeny","pos":"FW","ovr":84,"age":24,"nat":"IDN","cat":"TIMNAS","trait":"Penyelesai Klinis","club":"Oxford Utd","val":17000000000,"wage":170000000},
    {"id":"tm_9","name":"Ragnar Oratmangoen","pos":"FW","ovr":83,"age":26,"nat":"IDN","cat":"TIMNAS","trait":"Pekerja Keras","club":"FCV Dender","val":13000000000,"wage":130000000},
    {"id":"tm_10","name":"Eliano Reijnders","pos":"MF","ovr":82,"age":24,"nat":"IDN","cat":"TIMNAS","trait":"Bek Modern","club":"PEC Zwolle","val":11500000000,"wage":115000000},
    {"id":"tm_11","name":"Justin Hubner","pos":"DF","ovr":82,"age":21,"nat":"IDN","cat":"TIMNAS","trait":"Temperamental","club":"Wolves U21","val":11000000000,"wage":110000000},
    {"id":"tm_12","name":"Sandy Walsh","pos":"DF","ovr":83,"age":29,"nat":"IDN","cat":"TIMNAS","trait":"Raja Tekel","club":"KV Mechelen","val":12500000000,"wage":125000000},
    {"id":"tm_13","name":"Ivar Jenner","pos":"MF","ovr":82,"age":20,"nat":"IDN","cat":"TIMNAS","trait":"Umpan Terobosan","club":"FC Utrecht","val":11000000000,"wage":110000000},
    {"id":"tm_14","name":"Emil Audero","pos":"GK","ovr":85,"age":27,"nat":"IDN","cat":"TIMNAS","trait":"Komandan Kotak Penalti","club":"Como 1907","val":19000000000,"wage":185000000},
    {"id":"tm_21","name":"Son Heung-min","pos":"FW","ovr":91,"age":32,"nat":"KOR","cat":"ASIA","trait":"Penyelesai Klinis","club":"Tottenham","val":42000000000,"wage":380000000},
    {"id":"tm_22","name":"Kaoru Mitoma","pos":"FW","ovr":88,"age":27,"nat":"JPN","cat":"ASIA","trait":"Dribel Cepat","club":"Brighton","val":36000000000,"wage":310000000},
    {"id":"tm_23","name":"Takefusa Kubo","pos":"MF","ovr":88,"age":23,"nat":"JPN","cat":"ASIA","trait":"Playmaker Jenius","club":"Real Sociedad","val":38000000000,"wage":320000000},
    {"id":"tm_24","name":"Kim Min-jae","pos":"DF","ovr":89,"age":28,"nat":"KOR","cat":"ASIA","trait":"Tembok Kokoh","club":"Bayern Munich","val":40000000000,"wage":350000000},
    {"id":"tm_30","name":"Cristiano Ronaldo","pos":"FW","ovr":93,"age":39,"nat":"POR","cat":"WORLD","trait":"Predator Kotak Penalti","club":"Al-Nassr","val":60000000000,"wage":650000000},
    {"id":"tm_31","name":"Lionel Messi","pos":"FW","ovr":93,"age":37,"nat":"ARG","cat":"WORLD","trait":"Playmaker Jenius","club":"Inter Miami","val":60000000000,"wage":650000000},
    {"id":"tm_32","name":"Kylian Mbappe","pos":"FW","ovr":95,"age":26,"nat":"FRA","cat":"WORLD","trait":"Dribel Cepat","club":"Real Madrid","val":95000000000,"wage":850000000},
    {"id":"tm_33","name":"Erling Haaland","pos":"FW","ovr":95,"age":24,"nat":"NOR","cat":"WORLD","trait":"Penyelesai Klinis","club":"Man City","val":95000000000,"wage":850000000},
    {"id":"tm_35","name":"Jude Bellingham","pos":"MF","ovr":94,"age":21,"nat":"ENG","cat":"WORLD","trait":"Kapten Vokal","club":"Real Madrid","val":90000000000,"wage":800000000}
]

SPONSORS = [
    {"id":"sp_bri","name":"BRI","full":"Bank BRI","per_match":850000000,"win_bonus":350000000},
    {"id":"sp_indofood","name":"INDOFOOD","full":"Indofood","per_match":1050000000,"win_bonus":450000000},
    {"id":"sp_freeport","name":"FREEPORT","full":"PT Freeport Indonesia","per_match":1400000000,"win_bonus":600000000},
    {"id":"sp_mandiri","name":"MANDIRI","full":"Bank Mandiri","per_match":950000000,"win_bonus":400000000},
    {"id":"sp_pegadaian","name":"PEGADAIAN","full":"Pegadaian","per_match":650000000,"win_bonus":300000000},
    {"id":"sp_emirates","name":"EMIRATES","full":"Fly Emirates","per_match":1800000000,"win_bonus":800000000}
]

APPARELS = [
    {"id":"ap_erspo","name":"Erspo","origin":"Indonesia 🇮🇩","per_match":380000000,"merch_bonus":220000000},
    {"id":"ap_mills","name":"Mills","origin":"Indonesia 🇮🇩","per_match":350000000,"merch_bonus":200000000},
    {"id":"ap_specs","name":"Specs","origin":"Indonesia 🇮🇩","per_match":340000000,"merch_bonus":190000000},
    {"id":"ap_ortus","name":"Ortuseight","origin":"Indonesia 🇮🇩","per_match":340000000,"merch_bonus":195000000},
    {"id":"ap_riors","name":"Riors","origin":"Indonesia 🇮🇩","per_match":300000000,"merch_bonus":170000000},
    {"id":"ap_adidas","name":"Adidas","origin":"Jerman 🇩🇪","per_match":750000000,"merch_bonus":420000000},
    {"id":"ap_nike","name":"Nike","origin":"AS 🇺🇸","per_match":780000000,"merch_bonus":450000000}
]

COACHES = [
    {"id":"co_local","name":"Coach Lokal Lisensi A","ovr_bonus":0,"cost":0,"salary":120000000},
    {"id":"co_indra","name":"Indra Sjafri","ovr_bonus":2,"cost":3000000000,"salary":220000000},
    {"id":"co_bojan","name":"Bojan Hodak","ovr_bonus":3,"cost":5000000000,"salary":320000000},
    {"id":"co_sty","name":"Shin Tae-yong","ovr_bonus":5,"cost":10000000000,"salary":500000000},
    {"id":"co_kluivert","name":"Patrick Kluivert","ovr_bonus":5,"cost":11000000000,"salary":550000000},
    {"id":"co_guardiola","name":"Pep Guardiola","ovr_bonus":8,"cost":28000000000,"salary":1100000000}
]

MEDICAL = [
    {"id":"med_basic","name":"Fisioterapis Standar","recovery_bonus":5,"injury_shield":10,"cost":0,"salary":65000000},
    {"id":"med_pro","name":"Sport Science Nasional","recovery_bonus":12,"injury_shield":35,"cost":3500000000,"salary":150000000},
    {"id":"med_europe","name":"Klinik Medis Eropa","recovery_bonus":22,"injury_shield":65,"cost":9000000000,"salary":300000000}
]

SCOUTS = [
    {"id":"sc_local","name":"Pemandu Bakat Regional","youth_boost":0,"cost":0,"salary":60000000},
    {"id":"sc_national","name":"Jaringan Nusantara","youth_boost":3,"cost":3000000000,"salary":140000000},
    {"id":"sc_global","name":"Direktur Scouting Global","youth_boost":6,"cost":8500000000,"salary":280000000}
]

INJURIES = [("Cedera Hamstring", 1), ("Keseleo Engkel", 1), ("Robekan Otot Paha", 2), ("Cedera Lutut MCL", 3)]

def sim_engine(home, away, is_home_game=True, tactic="balanced", mentality="normal", coach_bonus=0, injury_shield=10, ko=False):
    sq = home.get("squad", [])
    fit = [p for p in sq if p.get("is_starter") and not p.get("injury")] or [p for p in sq if not p.get("injury")]

    # Pengaruh Moral & Trait Pemain
    avg_morale = sum(p.get("morale", 80) for p in fit) / max(1, len(fit))
    morale_mod = 2 if avg_morale >= 85 else (-2 if avg_morale < 65 else 0)
    trait_bonus = sum(1 for p in fit if p.get("trait") in ("Kapten Vokal", "Playmaker Jenius", "Penyelesai Klinis", "Tembok Kokoh")) * 0.4

    u_rat = home.get("rating", 78) + coach_bonus + morale_mod + trait_bonus + (2 if is_home_game else -1) + (2 if tactic == "attack" else 0)
    o_rat = away.get("rating", 78) + (1 if tactic == "attack" else (-1 if tactic == "defend" else 0))
    diff = u_rat - o_rat

    ug = min(6, max(0, int(random.gauss(max(0.35, 1.35 + diff * 0.11), 0.95))))
    og = min(5, max(0, int(random.gauss(max(0.25, 1.15 - diff * 0.09), 0.9))))
    pu, po = None, None
    if ko and ug == og:
        pu, po = random.randint(3, 5), random.randint(2, 5)
        if pu == po:
            if random.random() < 0.55: pu += 1
            else: po += 1

    # Bobot pencetak gol & assist berdasarkan trait
    scorers_pool, assisters_pool = [], []
    for p in fit:
        w_s = 5 if p["pos"] == "FW" else (3 if p["pos"] == "MF" else 1)
        if p.get("trait") in ("Penyelesai Klinis", "Predator Kotak Penalti"): w_s += 4
        scorers_pool.extend([p] * w_s)

        w_a = 5 if p["pos"] == "MF" else (3 if p["pos"] == "FW" else 2)
        if p.get("trait") in ("Playmaker Jenius", "Umpan Terobosan"): w_a += 4
        assisters_pool.extend([p] * w_a)

    evs = [{"min": 1, "type": "info", "text": f"Kick-off! {home['name']} vs {away['name']}."}]
    goal_records = []
    for _ in range(ug):
        sc = random.choice(scorers_pool) if scorers_pool else None
        as_candidates = [x for x in assisters_pool if not sc or x["id"] != sc["id"]]
        ast = random.choice(as_candidates) if (as_candidates and random.random() < 0.78) else None
        m_min = random.randint(4, 90)
        sc_name = sc["name"] if sc else "Striker"
        ast_txt = f" (Assist: {ast['name']})" if ast else ""
        evs.append({"min": m_min, "type": "goal", "text": f"⚽ {m_min}' GOL! {sc_name}{ast_txt}!"})
        goal_records.append({"scorer_id": sc["id"] if sc else None, "scorer_name": sc_name, "assist_id": ast["id"] if ast else None, "assist_name": ast["name"] if ast else None})

    for _ in range(og):
        m_min = random.randint(5, 90)
        evs.append({"min": m_min, "type": "goal_away", "text": f"⚽ {m_min}' Gol untuk {away['name']}."})
    inj_p = None
    inj_prob = (0.20 if mentality == "hard" else 0.09) * (1.0 - injury_shield / 100.0)
    if fit and random.random() < inj_prob:
        v = random.choice(fit)
        it, iw = random.choice(INJURIES)
        inj_p = {"id": v["id"], "name": v["name"], "type": it, "weeks": iw}
        evs.append({"min": random.randint(25, 85), "type": "injury", "text": f"🚑 CEDERA! {v['name']} ({it}, {iw} pekan)."})

    red_p = None
    temp_players = [p for p in fit if p.get("trait") == "Temperamental"]
    if fit and random.random() < (0.18 if mentality == "hard" else (0.12 if temp_players else 0.04)):
        rp = random.choice(temp_players) if (temp_players and random.random() < 0.6) else random.choice(fit)
        red_p = {"id": rp["id"], "name": rp["name"]}
        evs.append({"min": random.randint(35, 89), "type": "red", "text": f"🟥 KARTU MERAH! {rp['name']} diusir wasit!"})

    sanc = None
    if random.random() < (0.22 if mentality == "hard" else 0.07):
        sanc = {"title": "Denda Komdis PSSI", "fine": 120000000, "fans_loss": 2, "desc": "⚖️ Komdis PSSI menjatuhkan denda Rp 120 Jt akibat flare suporter."}
        evs.append({"min": 90, "type": "sanction", "text": sanc["desc"]})

    evs.sort(key=lambda x: x["min"])

    # Statistik Permainan Lengkap
    poss_u = max(34, min(72, int(50 + diff * 2.2 + (6 if tactic == "possession" else (-5 if tactic == "defend" else 0)) + random.randint(-4, 4))))
    shots_u = max(ug + 2, int(8 + diff * 0.7 + random.randint(1, 6)))
    shots_o = max(og + 1, int(7 - diff * 0.5 + random.randint(1, 5)))
    sot_u = max(ug, min(shots_u, int(shots_u * random.uniform(0.38, 0.62))))
    sot_o = max(og, min(shots_o, int(shots_o * random.uniform(0.35, 0.58))))

    return {
        "user_goals": ug, "opp_goals": og, "pen_user": pu, "pen_opp": po, "events": evs,
        "goal_records": goal_records, "pssi_sanction": sanc, "red_card_player": red_p, "injured_player": inj_p,
        "attendance": random.randint(16000, 42000) if is_home_game else 0,
        "match_stats": {
            "poss_user": poss_u, "poss_opp": 100 - poss_u,
            "shots_user": shots_u, "shots_opp": shots_o,
            "sot_user": sot_u, "sot_opp": sot_o,
            "pass_acc_user": min(94, max(72, int(78 + (poss_u - 50) * 0.4 + random.randint(-2, 3)))),
            "pass_acc_opp": min(91, max(68, int(76 - (poss_u - 50) * 0.3 + random.randint(-2, 3)))),
            "fouls_user": random.randint(11, 19) if mentality == "hard" else random.randint(6, 13),
            "fouls_opp": random.randint(7, 15),
            "motm": goal_records[0]["scorer_name"] if goal_records else (fit[0]["name"] if fit else "Kapten"),
            "motm_rating": round(min(9.9, 7.6 + ug * 0.4 + random.uniform(0.1, 0.4)), 1)
        }
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/init_data")
def init_data():
    return jsonify({"liga1": LIGA1, "liga2": LIGA2, "acl_two": ACL_TWO, "acl_elite": ACL_ELITE, "preseason": PRESEASON_TOURS, "market": MARKET, "sponsors": SPONSORS, "apparels": APPARELS, "coaches": COACHES, "medical": MEDICAL, "scouts": SCOUTS})

@app.route("/api/simulate_match", methods=["POST"])
def simulate_match():
    d = request.get_json(force=True)
    res = sim_engine(d["user_club"], d["opp_club"], d.get("is_home", True), d.get("tactic","balanced"), d.get("mentality","normal"), d.get("coach_bonus",0), d.get("injury_shield",10), False)
    others = [c for c in d.get("league_clubs", []) if c["id"] not in (d["user_club"]["id"], d["opp_club"]["id"])]
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
            is_u1 = t1["id"] == uid
            r = sim_engine(t1 if is_u1 else t2, t2 if is_u1 else t1, True, d.get("tactic","balanced"), d.get("mentality","normal"), d.get("coach_bonus",0), d.get("injury_shield",10), True)
            s1, s2 = (r["user_goals"], r["opp_goals"]) if is_u1 else (r["opp_goals"], r["user_goals"])
            p1, p2 = (r["pen_user"], r["pen_opp"]) if is_u1 else (r["pen_opp"], r["pen_user"])
            u_evs = r["events"]
        else:
            s1, s2, p1, p2 = max(0, int(random.gauss(1.3, 0.9))), max(0, int(random.gauss(1.2, 0.9))), None, None
            if s1 == s2: p1, p2 = 5, 4
        win = t1 if (s1 > s2 or (s1 == s2 and (p1 or 0) > (p2 or 0))) else t2
        upd.append({"team1": t1, "team2": t2, "score1": s1, "score2": s2, "pen1": p1, "pen2": p2, "winner": win})
    return jsonify({"matches": upd, "user_events": u_evs})
