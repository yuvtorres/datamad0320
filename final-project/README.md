**Título**

Energia real

**Descripción del Proyecto**

Basic: API que devuelve la matriz de generación eléctrica instantanea, y un pronóstico de esta generación para las próximas horas. Aunque las comercializadoras nos vendan "energía limpia", en realidad nuestro energía viene de la matriz que se encuentré soportando el sistema en ese momento. Ésta matríz se configura a su vez por mérito económico (precio), entre otras cosas. 

EL objetivo de esta API es hacer conciente a la gente de donde viene la energía que consume y darle un pronóstico de tecnologías de generación para las siguientes 24 horas...

La infraestructura a usar para los datos serán bases de datos de Amazon. Y se presentaran con Leaflet.

**Módulos de Python**

- Flask (API)
- boto3 (almacenamiento de datos)
- pandas (manejo de datos)
- Scikit Learn (Pronósticos)
- Leaflet (Pronósticos)
- Request (Input meterologico y otros)
- BeautifulSoup (Input meterologico y otros)
