# PAQUETES
import streamlit as st
from PIL import Image

# CREAR DASHBOARD Y DARLE NOMBRE
st.set_page_config(page_title='Santiago Danielli',
                   layout='wide')

# PARTES

sobre_mi = """
Soy Licenciado en Sociología por la Universidad de Buenos Aires y realice estudios de posgrados en estadística aplicada.
Tengo más de tres años de experiencia como analista de datos, anteriormente en un organismo de derechos humanos y a
actualmente en una empresa de investigación de mercado.

En estos años, realice programas educativos y cursos para adquirir conocimientos en herramientas fundamentales para la 
administración de bases de datos y el análisis de datos para la toma de decisiones (SQL, Python y Power BI)"""

foto = Image.open('foto.png')


# PARTE PRINCIPAL
st.header('Santiago Danielli')
st.subheader('Sociólogo y analista de datos')
st.write('¡Bienvenidos! Construí está versión de mi CV con Python y la librería Streamlit.')
st.markdown('----')
columna1, columna2 = st.columns([1, 2])
with columna1:
    st.image(foto, caption='Este soy yo. Un gusto')
with columna2:
    st.write('Mis datos de contacto')
    st.write('Correo: santiagodanielli0@gmail.com')
    st.write('Tel: 11 2389-8062')
    st.write('Perfil de Linkedin: www.linkedin.com/in/santiago-danielli-3a6859b2')
    st.write('Vivo en Posadas, Misiones, Argentina', ':flag-ar:')
    st.markdown(sobre_mi)


# SEGUNDA PARTE

columna1, columna2 = st.columns(2)
with columna1:
    st.subheader('Experiencia')
    st.write('Abril 2023 - Actualidad')
    st.write('Administrador de base de datos y analista de datos en Latam Research')
    st.write('Octubre 2019 - Marzo 2023')
    st.write('Analista de datos en Dirección de Producción y Sistematización de la Información del CNPT-AR')
    st.subheader('Educación')
    st.write('2012 - 2020')
    st.write('Licenciatura en Sociología, Universidad de Buenos Aires (UBA)')
    st.write('2023')
    st.write('Programa de Posgrado en Estadística Aplicada en Ciencias Sociales (FLACSO)')
    st.subheader('Cursos y certificaciones')
    st.write('Data Analysis - Coderhouse')
    st.write('Introducción a bases de datos y SQL - Educación IT')
    st.write('Fundamentos de Programación con SQL Server 2019 - Educación IT')
    st.write('Certificado Profesional de Análisis de Datos de Google - Coursera')
with columna2:
    st.subheader('Herramientas de software')
    st.write('Excel')
    st.write(':chart_with_upwards_trend:',':chart_with_upwards_trend:',':chart_with_upwards_trend:',':chart_with_upwards_trend:',':chart_with_upwards_trend:')
    st.write('Power BI')
    st.write(':chart_with_upwards_trend:',':chart_with_upwards_trend:',':chart_with_upwards_trend:')
    st.write('SQL')
    st.write(':chart_with_upwards_trend:',':chart_with_upwards_trend:')
    st.write('Python')
    st.write(':chart_with_upwards_trend:',':chart_with_upwards_trend:')
    st.subheader('Idioma Inglés')
    st.write('Escrito y oral nivel intermedio')
    st.subheader('Habilidades blandas')
    st.write('Atención al detalle, pensamiento analítico, planificación y buen manejo de los tiempos y objetivos, trabajo en equipo')


