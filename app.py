import streamlit as st

st.title("SafeText")

st.sidebar.header("Menú de Navegación")

opcion = st.sidebar.selectbox("Elige una sección", ["Página Principal", "Simulador", "Ayuda"])

usuario = st.sidebar.text_input("Tu nombre")

if opcion == "Página Principal":
    st.subheader(f"Bienvenido/a {usuario}")
    st.write("SafeText es un simulador educativo sobre el 'sexting', en el que se dan consejos sobre que hacer en estos casos y simula el compartir contenido multimedia de manera 'segura', y, al mismo tiempo, demostrar que no hay opción digital totalmente segura para esta actividad")
elif opcion == "Simulador":
    st.subheader("Simulador de Envío Protegido")
    st.write("Aquí deberás subir un archivo de prueba y configurar todo para simular el compartir estos archivos. Por favor evita subir una fotografía o video real, solo archivos de prueba")
   
    archivo = st.file_uploader("sube una imagen de prueba (ej. dibujo o avatar):", type=["jpg", "png", "jpeg"])
    st.markdown("### ⚙️ Ajustes de Seguridad")
   
    tiempo = st.slider("Tiempo de Visualización (segundos):", min_value=5,max_value=60, value=10, step=5)
   
    bloquear_captura = st.checkbox("Bloquear captura de pantalla", value=True)
    bloquear_descarga = st.checkbox("Bloquear descarga del archivo", value=True)
    bloquear_reenvio = st.checkbox("Bloquear reenvío del archivo", value=True)
   
    if st.button("Simular Envío Seguro"):
        if archivo is not None:
            st.success(f"Archivo '{archivo.name}` subido con éxito")
            st.info(f"Tiempo de visualización configurado: {tiempo} segundos")
            st.info(f"Bloquear captura de pantalla: {'Sí' if bloquear_captura else 'No'} ")
            st.info(f"Bloquear descarga del archivo: {'Sí' if bloquear_descarga else 'No'} ")
            st.info(f"Bloquear reenvío del archivo: {'Sí' if bloquear_reenvio else 'No'} ")
            st.balloons()
            st.write("Recuerda que esta es una simulación educativa, no crea enlaces ni sube archivos a Internet. Este simulador tiene como objetivo concienciar y educar sobre los riesgos del sexting. Piensa antes de participar en este tipo de actividades. Si eres menor de edad evita compartir contenido íntimo y busca ayuda si recibes contenido de índole sexual sin pedirlo o estás en una situación de acoso o extorsión con este tipo de contenido")
        else:
            st.error("Por favor, sube un archivo antes de simular el envío") 

else:
    st.subheader("Centro de Ayuda")
    st.write("Recomendaciones y Recursos")
   
    pestana1, pestana2, pestana3 = st.tabs(["💡 Consejos", "⚖️ Legal", "🆘 Apoyo"])
   
    with pestana1:
        st.markdown("### Consejos para Evitar Riesgos")
        st.write(""" * **Piensa antes de enviar**: Reflexiona sobre las posibles consecuencias de compartir contenido íntimo. Ningún medio es 100% seguro. * **Desconfía de falsas seguridades:** Las aplicaciones que prometen total seguridad pueden ser burladas por medios externos. """)
   
    with pestana2:
        st.markdown("### Marco Legal")
        st.warning(""" * El sexting puede tener implicaciones legales, especialmente si involucra a menores de edad. Es importante conocer las leyes locales y las posibles consecuencias legales antes de participar en estas actividades * Este simulador prioriza la educación y la concienciación sobre los riesgos asociados al sexting, y no promueve ni fomenta la participación en actividades ilegales. """)
   
    with pestana3:
        st.markdown("### Canales de Apoyo")
        st.info(""" * No borres evidencia: Si te encuentras en una situación de acoso o extorsión, conserva cualquier evidencia que pueda ser útil para las autoridades * Acércate a orientadores, profesores, adultos o autoridades de confianza para recibir apoyo y orientación * Contacta con organizaciones de ayuda a víctimas de acoso o extorsión sexual en línea para obtener ayuda profesional """)
