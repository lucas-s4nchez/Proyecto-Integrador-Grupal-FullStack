CREATE DATABASE lawebdelcafe;
use lawebdelcafe;

CREATE TABLE categoria
(
id_categoria int not null auto_increment,
categoria varchar(20) not null,
CONSTRAINT id_categoria_pk PRIMARY KEY (id_categoria)
);

CREATE TABLE productos
(
id_productos int not null auto_increment,
nombre varchar(20) not null,
precio int not null,
descripcion varchar(30) not null,
stock varchar(4) not null,
id_categoria int,
CONSTRAINT id_productos_pk PRIMARY KEY (id_productos),
CONSTRAINT id_categoria_fk FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
);

CREATE TABLE comentarios 
(
id_comentarios int auto_increment,
mensaje varchar(100) not null, 
fecha date, 
id_productos int, 
id_usuario int, 
CONSTRAINT id_comentarios_pk PRIMARY KEY (id_comentarios), 
CONSTRAINT id_producto_fk FOREIGN KEY (id_productos) REFERENCES productos (id_productos), 
CONSTRAINT id_usuario_fk FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);

CREATE TABLE usuarios
(
id_usuario int not null auto_increment,
nombre varchar(20) not null,
apellido varchar(20) not null,
email varchar(20),
contraseña varchar(15),
rol varchar(20),
CONSTRAINT id_usuario_pk PRIMARY KEY (id_usuario)
);

INSERT INTO categoria (id_categoria, categoria) VALUES ( '1', 'Cafe Expreso');

INSERT INTO productos (id_productos, nombre, precio, descripcion, stock, id_categoria) VALUES 
('1', 'Expreso', '320', 'Italiano', 'SI', '1'); 

INSERT INTO categoria (id_categoria, categoria) VALUES ('2', 'Reposteria' ); 

INSERT INTO productos (id_productos, nombre, precio, descripcion, stock, id_categoria) VALUES ('2', 'Cheescake', '400', 'Pastel de Varios Sabores', 'SI', '2');

INSERT INTO categoria (id_categoria, categoria) VALUES ('3', 'Comida' );

INSERT INTO productos (id_productos, nombre, precio, descripcion, stock, id_categoria) VALUES ('3', 'Croissant', '350', 'Croissant de jyq', 'SI', '3');

select * from categoria;

UPDATE categoria
SET 
categoria= "cafeteria"
where id_categoria="1" ;

INSERT INTO usuarios (id_usuario, nombre, apellido, email, contraseña, rol) VALUES ( '1', "Guillermo", "Garcia", "guillermo@gmail.com", "12345", ""), ("2", "Micaela", "Lopez", "micalopez@gmail.com", "23456", "");

INSERT INTO comentarios (id_comentarios, mensaje, fecha, id_productos, id_usuario) VALUES ("1", "Delicioso cheesecake", "2022-10-02", "2", "2"), ("2", "excelente la calidad del cafe", "2022-11-01", "1", "1");

select * from comentarios;

SELECT id_usuario, nombre, email
FROM usuarios;

SELECT prod.id_productos, cat.categoria, prod.precio  FROM categoria as cat
inner join productos as prod
on cat.id_categoria= prod.id_categoria;
