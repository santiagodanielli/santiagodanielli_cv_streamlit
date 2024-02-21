"""
Hacer comentarios aquí
"""
# PAQUETES
import streamlit as st
from PIL import Image

# CREAR DASHBOARD Y DARLE NOMBRE
st.set_page_config(page_title='Santiago Danielli',
                   layout='wide')

# PARTES

descripcion = """
Como Data Analyst me especializo en brindar servicios de consultoría analítica e implementar soluciones de 
business intelligence. 
Tengo conocimiento y experiencia en las más importantes tecnologías para aportar a la toma de decisiones a 
partir de la explotación de los datos.
Mis habilidades principales radican en el uso de Power BI para el armado de dashboards y visualizaciones, 
como también los lenguajes de programación Python y SQL para la manipulación y limpieza de grandes volúmenes de 
datos.
"""

foto = Image.open('santiago_danielli_circular.png')
pin_certificado = Image.open("google_certificate_img.PNG")


# PARTE PRINCIPAL
st.title('Santiago Danielli')
st.subheader(':purple[Analista de datos]')
st.markdown(descripcion)

st.markdown('----')

columna1, columna2 = st.columns(2)
with columna1:
    st.image(foto)
with columna2:
    st.write('')
    st.write('')
    st.write('Mis datos de contacto y web')
    st.write(':e-mail: Correo: santiagodanielli0@gmail.com')
    st.write(':telephone_receiver: Tel: 11 2389-8062')
    st.link_button(":briefcase: Perfil de Linkedin", "https://www.linkedin.com/in/santiago-danielli-3a6859b2/")
    st.link_button(":mag: Web", "https://santiago-danielli.streamlit.app/")
    st.link_button(":computer: Github - Proyectos", "https://github.com/santiagodanielli")
    
st.markdown('----')

# SEGUNDA PARTE
st.subheader('EXPERIENCIA LABORAL')
st.write('*Abril 2023 - Actualidad*')
st.write('Analista de datos en Latam Research')
st.write("Tareas: gestionar y monitorear la base de datos, controlar el proceso de ETL, armado de informes.")
st.write("")
st.write('*Junio 2023 - Actualidad*')
st.write("Docente en Taller Final Integrador, Especialización en Criminología, Universidad Nacional de Quilmes")
st.write("Tareas: brindar el contenido de la materia sobre metodología de la investigación.")
st.write("")
st.write('*Octubre 2019 - Marzo 2023*')
st.write('Asistente en equipo de datos y luego Analista de datos en CNPT-AR')
st.write("Tareas: aportar al proceso de ETL, armado de informes.")
st.write("")
st.subheader('HABILIDADES TECNICAS')
st.write('Lenguajes de programación: Python (Pandas, Numpy, Matplotlib, Plotly, Seaborn, Streamlit)')
st.write('Visualización de datos y dashboards: Power BI')
st.write('Bases de datos: MySQL, SQL Server')
st.write("")
st.subheader('EDUCACION')
st.write('*2012 - 2020*')
st.write('Licenciatura en Sociología, Universidad de Buenos Aires (UBA)')
st.write("")
st.write('*2023*')
st.write('Programa de Posgrado en Estadística Aplicada en Ciencias Sociales (FLACSO)')
st.write("")
st.subheader('CERTIFICACIONES')
st.link_button("Certificado Profesional de Análisis de Datos de Google", "https://coursera.org/share/af087c2e7bab59eebcc991cd5cb903b3")
st.image(pin_certificado)
st.write("")
st.subheader('CURSOS')
st.write('Data Analysis - Coderhouse')
st.write('Introducción a bases de datos y SQL - Educación IT')
st.write('Fundamentos de Programación con SQL Server 2019 - Educación IT')
st.write("")
st.subheader('IDIOMAS')
st.write('Español: nativo')
st.write('Inglés: avanzado oral y escrito')

