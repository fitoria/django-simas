#Bueno para crear en modo produccion algunos campos y modificar algunos:

#crear campos:
ALTER TABLE pagina_actividad ADD COLUMN fecha1 datetime;

#modificar un campo:
ALTER TABLE pagina_seccion CHANGE nombre nombre varchar(50);
ALTER TABLE pagina_seccion CHANGE slug slug varchar(50);

ALTER TABLE pagina_subseccion CHANGE nombre nombre varchar(50);
ALTER TABLE pagina_subseccion CHANGE nombre nombre varchar(50);

#Crear los adjuntos a las actividades y noticias nose para que?
ALTER TABLE pagina_noticia ADD COLUMN adjunto varchar(100);
ALTER TABLE pagina_actividad ADD COLUMN adjunto varchar(100);
