-- Database seeding --

-- Datos de Cars (cambio el VIN del registro 5 por tener el mismo que el registro 6

INSERT INTO Car (VIN, Manufacturer, Model,Year, Color) VALUES 
('3K096I98581DHSNU','Volkswagen','Tiguan',2019,'Blue'),
('ZM8G7BEUQZ97IH46V' ,	'Peugeot','Rifter' 	,	2019, 	'Red'),
('RKXVNNIHLVVZOUB4M' ,	'Ford'   , 'Fusion' 	,	2018, 	'White'),
('HKNDGS7CU31E9Z7JW' ,	'Toyota','RAV4',2018,'Silver'),
('DAM41UDN3CHU2WVF5' ,	'Volvo' ,'V60 Cross Country',2019,'Gray'),
('DAM41UDN3CHU2WVF6' ,	'Volvo' ,'V60',2019,'Gray');

-- Crea Customer

INSERT INTO Customer (`Customer ID`,Name, Phone_number, Email,Address, City,`State/Province`, Country, zip_code) VALUES
(10001 ,'Pablo Picasso','+34 636 17 63 82','-','Paseo de la Chopera 14','Madrid','Madrid','Spain','28045'),
(20001,'Abraham Lincoln','+1 305 907 7086','-','120 SW 8th St','Miami','Florida','United States','33130'),
(30001 ,'Napoléon Bonaparte','+33 1 79 75 40 00','-','40 Rue du Colisée','Paris','Île-de-France','France','75008');

-- Crea Sales persons

INSERT INTO Salesperson (`Staff ID`,Name,Store) VALUES 
(00001 ,'Petey Cruiser','Madrid'),
(00002,'Anna Sthesia', 'Barcelona'),
(00003,'Paul Molive', 'Berlin'),
(00004,'Gail Forcewind','Paris'),
(00005,'Paige Turner', 'Mimia'),
(00006,'Bob Frapples', 'Mexico City'),
(00007,'Walter Melon', 'Amsterdam'),
(00008,'Shonda Leer', 'São Paulo');

-- Crea Invoices (**) Tuve que cambiar dos datos porque los índices empiezan en 1 y había dos ceros

INSERT INTO Invoice (Invoice_Number, `date`,`Car`,`Customer`,`Sales Person`) VALUES 
('852399038', STR_TO_DATE('22-08-2018','%d-%m-%Y'),'1','1','3'),
('731166526',str_to_date('31-12-2018','%d-%m-%Y'),'3','3','5'),
('271135104',str_to_date('22-01-2019','%d-%m-%Y'),'2','2','7');

