+++
title = "O2. Game"
weight = 2
+++

Je gaat je eigen breakout game programmeren!
<!--more-->

## Opdrachtbeschrijving
De opdracht in het kort is: Maak in groepjes van twee een breakout spel in python. Je gebruikt de startcode en maakt gebruik van de pygame-library.

### Inschrijven
Je schrijft je in via het onderstaande formulier dat de docent aanlevert (login met je schoolmail voor toegang). 
- [wv4in1 GEE lesdag 23/24](https://link) ___aanvullen___

### Werkwijze
- Je maakt deze opdracht in een team van twee personen. De docent geeft aan hoe de teams gemaakt worden.
- Je krijgt van de docent startcode voor deze opdracht. Je volgt het stappenplan dat je van de docent krijgt.
- ___hoe samenwerken in 1 repl met 2 personen___ Je maakt code in Replit. Je bewaart steeds de laatste versie van je code in Replit, zodat in de historie van Replit te zien is wanneer je welke code hebt aangepast.
- Deze opdracht maak je alsof het een echt project is. Je maakt eerst een planning. Daarna kijk je wekelijks of je nog volgens plan loopt. Als je niet volgens plan loopt, dan stuur je bij. In de les word je hiermee geholpen, maar uiteindelijk moet jij zorgen dat je op tijd klaar bent en een goed resultaat oplevert. 

### Beoordeling
Je krijgt één cijfer per team, maar de docent kan hiervan afwijken als teamleden geen gelijkwaardige bijdrage hebben geleverd. 

Het cijfer dat je voor je PO krijgt wordt vanuit verschillende invalshoeken bepaald: 

**Minimale eisen**

___excel bijvoegen met rubric, in plaats van deze beschrijving___

Voordat je een cijfer krijgt voor je PO, wordt gekeken of je werk voldoet aan de minimale eisen. Werk dat niet voldoet aan de minimale eisen krijgt het cijfer 1,0. De minimale eisen zijn:
- De inhoud is moreel verantwoord: het is niet beledigend, visueel gewelddadig of op andere manieren onfatsoenlijk.
- Natuurlijk mag je overleggen met klasgenoten en mag je op internet kijken hoe je bepaalde dingen kunt maken. Let wel op dat je geen plagiaat pleegt. Je mag maximaal 5 regels code overnemen van andere leerlingen of internet. Dat geldt ook voor code die je zelf vertaalt naar het Nederlands. Overtypen van code uit een Youtube-video of een tutorial van internet volgen en dat resultaat inleveren is niet toegestaan.
- Je gebruikt de startcode die je krijgt.
- Je gebruikt het stappenplan dat bij deze opdracht gegeven is.
- Een download in zip-formaat van je opdracht mag maximaal 50 MB groot zijn.

**Werking en aantrekkelijkheid**
- Spel start op
- Het spel werkt (hoe klein ook)
- Behaalde punten zijn zichtbaar bij game-over
- Het doel en de bediening van het spel is duidelijk
- Aantrekkelijk uiterlijk
- Prettige bediening
- Eenvoudig om mee te beginnen en moeilijker als je verder komt
- Afwisselend

**Techniek**
- De code volgt de lijn van het template
- De code is netjes en duidelijk leesbaar
- De code bevat geen dubbele stukken code
- Je hebt de technieken gebruikt die in de programmeerlessen zijn aangeboden.
- Je hebt dingen toegevoegd waarvan je zelf hebt uitgezocht hoe ze werken

**Inzet, planning en samenwerking**
- Je toont inzet tijdens de lessen
- De planning is vooraf gemaakt, gevolgd en als nodig bijgesteld.
- De taakverdeling is duidelijk en alle teamleden dragen in gelijke mate bij.
- Het werk is verdeeld over de weken waarin aan de opdracht kon worden gewerkt, dit blijkt onder andere uit de commits in Github.

### Inleveren
- De deadline voor inleveren vind je in de lesplanner.
- Je kunt vragen stellen tot de laatste les voor de deadline.
- Je zorgt dat jouw code op dezelfde manier start als de startcode die je aan het begin hebt gekregen (druk op Run in replit). Alle code die jij gemaakt hebt staan in de map mypgame. Dit is tenminste het bestand mygame/main.py. Als je plaatjes gebruikt, dan staan die er ook bij.
- Uit de versie historie in Replit blijkt wanneer je wat gedaan hebt.
- De laatste versie van je opdracht die op het moment van de deadline in Replit staat, wordt gebruikt voor de beoordeling.

## Hulpmiddelen
We gebruiken in deze opdracht de volgende tools:
1. [Replit](/tools/replit/)

## Startcode
Je krijgt van de docent een kopie van de startcode. De startcode kun je alvast bekijken op https://github.com/SCW-IN/hv4-game-startcode .

## Stappenplan
Werk de planning af van boven naar beneden. Vul de planning aan en stel bij terwijl je aan de opdracht werkt.

### Basisstappen: uitleg, spelen, afgaan en punten
1. kaatsende bal
    - Bekijk de startcode
    - Run de startcode
    - Resultaat: kaatsende bal
2. teken plank
    - Zet je code in de functie ...
    - Maak je plank 50 pixels hoog en 150 pixels breed
    - Gebruik de variabelen blok_x blok_y blok_w en blok_h voor de x en y van de linkerbovenhoek, de breedte en de hoogte van de plank
4. Beweeg plank
    - Gebruik `pygame.key.get_pressed` om te zien welke toetsen zijn ingedrukt
    - Gebruik de toets A voor bewegen naar links en D voor bewegen naar rechts
4. Zorg dat plank niet buiten het scherm kan
    - Je kunt het volgende algoritme gebruiken om boven en onder het scherm te stuiteren
     ```
     als de Y van de bal kleiner is dan 0
       bal_speed_y = bal_speed_y * -1 # laat de bal de andere uit bewegen
     anders als de Y van de bal + de hoogte van de bal groter is dan de hoogte van het scherm
       bal_speed_y = bal_speed_y * -1 # laat de bal de andere uit bewegen
     ```
     - Breid je code uit zodat de bal ook links en rechts tegen de rand van het venster stuitert
6. Zorg dat de bal kaatst tegen je plank
     - Gebruik een `if` en `pygame.Rect.collision` om botsing te detecteren
8. Zorg dat je af bent als de bal de onderkant van het scherm raakt
9. Teken een blok in het veld
     - Maak het blok 50 pixels hoog en 150 pixels breed
     - Gebruik de variabelen blok_x blok_y blok_w en blok_h voor de x en y van de linkerbovenhoek, de breedte en de hoogte van het blok
10. Detecteer als je het blok raakt
    - Gebruik een `if` en `pygame.Rect.collision` om botsing te detecteren
    - Geef een punt als een stukje van de bal het blok raakt
    - Haal het blok weg als het geraakt is
11. laat de bal stuiteren tegen het blok
    - zorg dat de bal stuitert door te kijken aan welke kant het blok geraakt is. Je kunt het volgende algoritme gebruiken.
    ```
    als de bal het blok raakt
      als de bal naar boven beweegt en de bovenkant van de bal zit boven de onderkant van het blok
        draai snelheid_y om
      anders als de bal naar onder beweegt en de onderkant van de bal zit onder de bovenkant van het blok
        draai snelheid_y om
      anders als de bal naar rechts beweegt en de rechtekant van de bal zit rechts van de linkerkant van het blok
        draai snelheid_x om
      anders als de bal naar links beweegt en de linkerkant van de bal zit links van de rechterkant van het blok
        draai snelheid_x om
    ```
12. maak een tweede en een derde blok
    - gebruik de variabelen blok_x1 blok_y1 blok_w1 en blok_h1 voor het tweede blok
    - gebruik de variabelen blok_x2 blok_y2 blok_w2 en blok_h2 voor het derde blok
15. zet je code om naar array's
    - verander de blok_x blok_y blok_w en blok_h in array's, gebruik alleen het 0-de element
    - breid de array uit met een 2e en 3e blok en voeg loops toe, zodat alle blokken uit de array worden gebruikt
    - verwijder de oude code voor blok 2 en 3 
17. maak een heel veld met tien of meer blokken

### Uitbreidingsstappen
1. Uitlegscherm
2. Gameoverscherm
3. Bal die steeds sneller gaat
4. Meerdere levels
5. Blokken die je vaker moet raken voordat ze weg zijn
6. Blokken die van kleur veranderen
7. Overleg met je docent voor meer uitbreidingen

Ingewikkeldere uitbreidingsstappen
1. Blokken die omlaag vallen als je ze raakt en "iets" opleveren als de plank ze raakt
2. Mogelijkheid voor meerdere ballen tegelijk als een speciaal blok valt en gevangen wordt
3. Mogelijkheid om tijdelijk blokken weg te schieten als een speciaal blok valt en gevangen wordt
4. Overleg met je docent voor meer ingewikkeldere uitbreidingen

## Uitlegvideo's
{{<video id="PLpTljPS____idinvullen____1HC">}}
