import csv

#Dictionnaire consommation totale par pays entre 2008 et 2021
f = open("consommation-mondiale-de-gaz-naturel.csv","r", encoding='utf-8')
reader = csv.DictReader(f, delimiter=";")
dico_pays_conso={}

for row in reader :
    if row["pays"] not in dico_pays_conso:
        dico_pays_conso[row["pays"]]=0
    dico_pays_conso[row["pays"]]+=round(float(row["consommation_gm3_an"]))
f.close()

dico_pays_conso = sorted(dico_pays_conso.items(), key=lambda x: x[1])

#Dictionnaire qui servira au calcul
f = open("consommation-mondiale-de-gaz-naturel.csv","r", encoding='utf-8')
reader = csv.DictReader(f, delimiter=";")
dico_pays_conso_pourcentage={}

for row in reader :
    if row["pays"] not in dico_pays_conso_pourcentage:
        dico_pays_conso_pourcentage[row["pays"]]=0
    dico_pays_conso_pourcentage[row["pays"]]+=round(float(row["consommation_gm3_an"]))
f.close()

dico_pays_conso_pourcentage = sorted(dico_pays_conso_pourcentage.items(), key=lambda x: x[1])

#Dictionnaire de la consommation total(ligne "Monde"/"World") par année croissante
f = open("consommation-mondiale-de-gaz-naturel.csv","r", encoding='utf-8')
reader = csv.DictReader(f, delimiter=";")

dico_annee_conso={}

for row in reader :
    if row["pays"] == "Monde":
        if row["annee"] not in dico_annee_conso :
            dico_annee_conso[row["annee"]]=0
        dico_annee_conso[row["annee"]]+=round(float(row["consommation_gm3_an"]))

dico_annee_conso = sorted(dico_annee_conso.items())
f.close()

#Calcul de la part de la consommation des continents en % entre 2008 et 2021 inclut
f = open("consommation-mondiale-de-gaz-naturel.csv","r", encoding='utf-8')
reader = csv.DictReader(f, delimiter=";")
Dico_pays_conso={}

for k,v in dico_pays_conso:
    Dico_pays_conso[k]=v


Dico_pays_conso_pourcentage={}

for k,v in dico_pays_conso_pourcentage:
    Dico_pays_conso_pourcentage[k]=v

pourcentage={}

for k,v in Dico_pays_conso_pourcentage.items():
    pourcentage[k]=round(((v*100)/48716),2)

#Début du calcul de la croissance de la consommation de 2008 à 2021
Dico_annee_conso={}

for k,v in dico_annee_conso:
    Dico_annee_conso[k]=v

min=0
max=0
taux=0

for k,v in Dico_annee_conso.items():
    if k == "2008":
        min=int(v)
    if k == "2021":
        max=int(v)
taux=round(((max-min)/min)*100,2)

#Début de la page HTML
html= """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>CHAOUCH Zakaria | Traiter des données</title>
</head>
<body>"""

#Mise en place du 1er tableau
html +="""
    <section>
        <div class = debut>
            <h1>Traiter des données</h1>
            <p>En informatique, le terme traitement de données ou traitement électronique des données renvoie à une série de processus qui permettent d'extraire de l'information ou de produire du savoir à partir de données brutes.
            Ces processus, une fois programmés, sont le plus souvent automatisés à l'aide d'ordinateurs.
        </div>
    </section>
    <section>
        <div class = partie_1>
            <h1>Réalisation d'un pourcentage</h1>
            <p>Ce tableau ci-dessous présente la consommation totale en gm3 de gaz naturel consommé par les continents entre 2008 et 2021.</p>
            <p>Comme nous pouvons le voir, le continent ou pays qui consomme le moins sont ceux faisant partie de l'Europe des Vingt-Sept. \n
            Cette consommation s'explique du au fait que ce comité existe depuis le 31 janvier 2020, suite au Brexit. </p>
            <p>Le continent qui pollue le plus est celui de l'Amérique du Nord avec une consommation de 12 788 gm3 entre 2008 et 2021.<p>
            <p>A l'aide de ce tableau, nous pouvons donc calculer la part qu'à chaque continent
            dans la consommation de gaz naturel entre 2008 et 2021 comme montrer dans le deuxième tableau.</p>

        </div>
        <div class = tab1>
        <table class=tableau1 border=1>
            <tr>
                <th>Continents</th>
                <th>Consommation total de chaque continents (en gm3) </th>
            </tr>"""
    

for k,v in dico_pays_conso:
    html += f"""<tr>
            <td>{k}</td>
            <td>{v}</td>
            </tr>"""

html +="""</table>
        </div>
    </section>"""
#Fin du 1er tableau
#Mise en place du 2ème tableau
html +="""<div class = tab2>
    <table class=tableau2 border=1>
        <tr>
            <th>Continents</th>
            <th>Consommations de chaque continents entre 2008 et 2021 (en %)</th>
        </tr>"""
for k,v in pourcentage.items():
    html += f"""<tr>
        <td>{k}</td>
        <td>{v}</td>
    </tr>"""

html +="""</table>
    </div>"""
#Fin du 2ème tableau

#3ème tableau
html +="""
    <section>
        <div class = partie_2>
            <h1>Réalisation d'un taux de croissance</h1>
            <p>Ce tableau ci-dessous présente la consommation mondiale en gm3 par année entre 2008 et 2021.</p>
            <p>Comme en témoigne le tableau, nous pouvons voir qu'il y a une augmentation de la consommation mondiale. Nous pouvons le voir rien qu'avec
            la première et dernière valeur de ce tableau, en 2008 la consommation était de 2 999gm3 tandis qu'en 2021, il y a une augmentation jusqu'a 4 037gm3.</p>
            <p>J'ai donc calculé le taux de croissance. Ce taux est une augmentation d'environ 35%. Ce qui veut dire que depuis 2008, la consommation mondial de gaz naturel
            à augmenté de +35%, comme en témoigne le dernier tableau :</p>
        <div class = tab3>
            <table class=tableau3 border=1>
            <tr>
                <th>Années</th>
                <th>Consommation mondial (en gm3)</th>
            </tr>"""
for k,v in Dico_annee_conso.items():
    html += f"""<tr>
        <td>{k}</td>
        <td>{v}</td>
    </tr>"""

html +="""</table>
        </div>"""
#Fin du 3ème tableau

#4ème tableau
html +="""<div class = tab4>
    <table class=tableau3 border=1>
        <tr>
            <th>Années</th>
            <th>Croissance de la consommation mondial (en %)</th>
        </tr>"""
for k,v in Dico_annee_conso.items():
    html +=f"""<tr>
        <td>2008 - 2021</td>
        <td>{taux}</td>
    </tr>"""
    break

html +="""</table>
    </div></body> 
</html>"""
#Fin du 4ème tableau et de la partie HTML

css=""" 
body{
    height: 100vh;
    font-family: "Jost", sans-serif;
    background-color: rgba(76, 72, 72, 0.557);
}
.debut h1{
    font-size: 32px;
    text-align: center;
}
p{
    color: whitesmoke;
}
.debut p{
    font-size: 16px;
    text-align: justify;
    margin-left: 20px;
    margin-right: 20px;
}
.partie_1 h1{
    font-size: 32px;
    text-align: center;
}

.partie_1 p{
    font-size: 16px;
    text-align: justify;
    margin-left: 20px;
    margin-right: 20px;
}

.partie_2 h1{
    font-size: 32px;
    text-align: center;
}

.partie_2 p{
    font-size: 16px;
    text-align: justify;
    margin-left: 20px;
    margin-right: 20px;
}

.tab p{
    font-size: 16px;
    text-align: justify;
    margin-left: 20px;
    margin-right: 20px;
}

table {
    border-collapse: collapse;
    width: 50%;
    margin: 0 auto;
}

th, td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
    padding: 15px 20px;
}

td{
    background-color: blanchedalmond;
    padding: 15px 20px;
}
tr:hover td {
    background-color: #f5f5f5;
}

td.selected {
    background-color: #3f51b5;
    color: white;
}

.tab1{
    margin-top: 20px;
}

.tab2{
    margin-top: 20px;
}

.tab3{
    margin-top: 20px;
}

.tab4{
    margin-top: 20px;
}
"""

f = open("donnee.html",'w', encoding="utf-8")
f.write(html)
f.close()

f=open("style.css","w",encoding="utf-8")
f.write(css)
f.close()