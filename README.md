# Ex03 Places Around Me
## Date: 12/02/2026

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google.

### STEP 3
Using ```<map>``` tag name the map.

### STEP 4
Create clickable regions in the image using ```<area>``` tag.

### STEP 5
Write HTML programs for all the regions identified.

### STEP 6
Execute the programs and publish them.

## CODE
kumbakonam.html
```
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>KUMBAKONAM MAP</h1>
    <br />
    <img src="{% static 'kumbakonammap.png' %}">

    <map name="map">
      <area
        alt="Kumbakonam_big_Masjid "
        title=" Kumbakonam_big_Masjidt"
        href="Kumbakonam_big_Masjid.html"
        coords="387,298,385,298"
        shape="rect"
      />
      <area
        alt="Mahamaham_Kulam"
        title="Mahamaham_Kulam"
        href="Mahamaham_Kulam.html"
        coords="526,295,528,295"
        shape="rect"
      />
      <area
        target=""
        alt="St._Mary’s_Cathedral"
        title="St._Mary’s_Cathedral"
        href="st_marys_cathedral.html"
        coords="582,294,578,297"
        shape="rect"
      />
    </map>
  </body>
</html>
```
Kumbakonam_big_Masjid.html
```
{% load static %}
<!DOCTYPE html>
<html>
<head>
<title>Kumbakonam Big Masjid</title>

<style>
body{
    font-family: Arial;
    background-color:#f5f5f5;
}

.container{
    width:900px;
    margin:auto;
    background:white;
    padding:20px;
}

img{
    width:100%;
    border-radius:10px;
}
</style>

</head>

<body>

<div class="container">

<img src="{% static 'masjid.avif' %}" alt="Kumbakonam Big Masjid">

<p>
The Kumbakonam Big Masjid, also called Masjid-e-Azam, is one of the oldest and most important mosques in the city of Kumbakonam in Tamil Nadu.
</p>

<p>
The mosque was built many years ago when Muslim traders and families settled in Kumbakonam.
</p>

<p>
It is also known as Masjid-e-Azam, meaning “Great Mosque.”
</p>

<p>
It represents the religious harmony of Kumbakonam, a city famous for many temples and different places of worship.
</p>

<p>
<b>Address:</b> Sarangapani South Street, Valayapettai Agraharam, Thanjavur Main Road, Kumbakonam – 612001, Tamil Nadu, India.
</p>

</div>


```
Mahamaham_Kulam.html
```
{% load static %}
<!DOCTYPE html>
<html>
<head>

<title>Mahamaham Kulam ,Kumbakonam</title>

<style>

body{
background-color:#c3d9df;
font-family:Arial;
}

.container{
width:900px;
margin:auto;
}

img{
width:100%;
border-radius:12px;
}

</style>

</head>

<body>

<div class="container">

<h1 align="center">Mahamaham Kulam ,Kumbakonam</h1>

<img src="{% static 'kulam.jpg' %}">

<p>
The Mahamaham Kulam (Mahamaham Tank) is a famous and sacred temple tank located in the city of Kumbakonam in Tamil Nadu.
</p>

<p>
The tank was built many centuries ago during the rule of the Chola dynasty. Later, kings of the Nayak dynasty renovated and improved the tank by building strong stone steps and mandapams around it.
</p>

<p>
Mahamaham Tank is believed to be a very sacred place for Hindus. According to tradition, the waters of many holy rivers such as Ganges River, Yamuna River, and Saraswati River are believed to meet in this tank.
</p>

<p>
The tank contains 20 sacred wells, each representing different holy rivers of India. Devotees believe that bathing in the tank during the Mahamaham festival removes sins and brings blessings.
</p>

<p>
Today, Mahamaham Tank is an important religious and historical landmark of Kumbakonam and attracts many pilgrims and visitors.
</p>

<p>
<b>Address:</b> Maha Maham Tank, Kanmani Devi Nagar, Kumbakonam – 612001, Thanjavur District, Tamil Nadu, India.
</p>

</div>

</body>
</html>
```
st_marys_cathedral.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<title>St. Mary’s Cathedral, Kumbakonam</title>

<style>

body{
    font-family: "Times New Roman", serif;
    text-align:center;
    margin:40px;
}

img{
    width:500px;
    margin-top:20px;
}

p{
    width:70%;
    margin:auto;
    margin-top:15px;
    font-size:18px;
    line-height:1.6;
}

h1{
    color:#2c3e50;
}

h2{
    margin-top:30px;
}

</style>

</head>

<body>

<h1>St. Mary’s Cathedral, Kumbakonam</h1>

<img src="{% static 'cathedral.avif' %}" alt="St Mary's Cathedral">

<p>
St. Mary’s Cathedral is an important Catholic church located in the city of Kumbakonam. 
The church was built in the 19th century by Catholic missionaries to serve the growing 
Christian community in the region.
</p>

<p>
Later, when the Roman Catholic Diocese of Kumbakonam was formed in 1899, this church 
became its main cathedral. The cathedral is dedicated to Mother Mary, who is greatly 
respected by Christians.
</p>

<p>
Over the years, the church was renovated and expanded to accommodate more worshippers.
</p>

<p>
St. Mary’s Cathedral is known for its beautiful architecture and religious importance, 
and it is one of the important Christian landmarks in Kumbakonam.
</p>

<h2>Address:</h2>

<p>
Kamaraj Road, John Selvaraj Nagar,<br>
Kumbakonam – 612001,<br>
Thanjavur District,<br>
Tamil Nadu, India.
</p>

</body>
</html>
```

## OUTPUT

<img width="1901" height="995" alt="Screenshot 2026-03-16 131725" src="https://github.com/user-attachments/assets/260d125f-ff31-4d4e-a974-e3e64d5adb91" />

<img width="1916" height="1070" alt="Screenshot 2026-03-16 131210" src="https://github.com/user-attachments/assets/6e285253-e1f5-440b-8c7f-4812c54ae89e" />

![Uploading Screenshot 2026-03-16 131230.png…]()

![Uploading mp3.png…]()

## RESULT
The program for implementing image maps using HTML is executed successfully.
