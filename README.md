# Reseptisovellus

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään ruokareseptit-sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan reseptejä. 
* Käyttäjä pystyy lisäämään kuvia reseptiin.
* Käyttäjä näkee sovellukseen lisätyt reseptit.
* Käyttäjä pystyy etsimään reseptejä hakusanalla.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät reseptit.
* Käyttäjä pystyy valitsemaan reseptille yhden tai useamman luokittelun (esim. jälkiruoka, vegaaninen). 
* Käyttäjä pystyy lisäämään kommentteja resepteille.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

