#!/usr/bin/python3

import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()

qkm = int(form.getvalue("qkm"))
side = float(form.getvalue("side_radio"))
curr = form.getvalue("curr_radio")


def berechne():
   
    if curr == "Euro":
        price = 0.00625 * qkm * side 
    if curr == "Dollar":
        price = 0.00625 * qkm * side / 0.93
    if curr == "Rubel":
        price = 0.00625 * qkm * side / 0.014
    if curr == "Bitcoin":
        price = 0.00625 * qkm * side / 26830.70
    if curr == "Döner":
        price = 0.00625 * qkm * side / 5

    return price
print("Content-type:text/html\r\n\r\n")
print('''
    <!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mondgrundstückskalkulator</title>
    <link rel="stylesheet" href="../style.css">
    <script src="script.cgi" defer></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rubik+Moonrocks&display=swap" rel="stylesheet">
</head>

<body>
        <h1>Mondgrundstückskalkulator</h1> 
        <img src="../Bilder/moontransp.png" alt="Mond">
    
    <div>    
        <div class="general">
            <p>Sie wollten schon immer Teilbesitzer des Mondes sein? Mit Hilfe dieses wunderschönen Tools können Sie den
                Wert einer von Ihnen ausgewählten Fläche des Mondes ermitteln. Hierbei können Sie nicht nur die Größe
                der Fläche
                frei wählen, sondern auch entscheiden, ob diese der Erde und somit Ihnen zugewandt ist! Des Weiteren
                können
                Sie sich den Wert in einer von Ihnen gewünschten Währung ausgeben lassen.</p>
        </div>
''')

print('''
    <div>
        <h4><label>Der Preis Ihres gewünschten Grundstückes: {price} {curr} </label><h/4>
    </div>

'''.format(price = berechne(), curr = curr)) 
    
print('''
    </div>
</body>

</html>
''')