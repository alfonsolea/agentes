import tempfile
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from crew_app import BackendDevelopmentCrew
import streamlit as st
import os
import sys

# streamlit run multiagentes/src/multiagentes/streamlit_app.py

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))


os.environ["GEMINI_API_KEY"] = "AIzaSyBzIQL912ZfFzk85SmDV4HFIR5C-LygU_c"


def read_workplan(file, file_type):
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_type}') as tmp_file:
        tmp_file.write(file.getvalue())
        tmp_file_path = tmp_file.name

    try:
        if file_type == 'txt':
            loader = TextLoader(tmp_file_path)
        elif file_type == 'pdf':
            loader = PyPDFLoader(tmp_file_path)
        elif file_type == 'docx':
            loader = Docx2txtLoader(tmp_file_path)
        else:
            return "Formato de archivo no soportado."

        documents = loader.load()
        text = "\n".join([doc.page_content for doc in documents])
    finally:
        os.unlink(tmp_file_path)

    return text.encode('utf-8')


def main():
    st.title("Generador de Código Backend")

    # Carga del plan de trabajo
    st.header("Plan de Trabajo")
    uploaded_file = st.file_uploader(
        "Carga tu plan de trabajo aquí!!", type=["txt", "pdf", "docx"])

    workplan_content = None
    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1].lower()

        with st.spinner('Leyendo el plan de trabajo...'):
            # Leer el archivo
            workplan_content = read_workplan(uploaded_file, file_type)

            st.success("Plan de trabajo cargado con éxito!")
            st.subheader("Contenido del Plan de Trabajo:")
            st.text_area("Contenido del Plan de Trabajo:",
                         workplan_content.decode('utf-8'), height=300)

    # Iniciar generación de código
    if st.button("Generar Código Backend"):
        # Validar que haya un plan de trabajo cargado
        if workplan_content is None:
            st.error(
                "Por favor, carga un plan de trabajo antes de generar el código.")
        else:
            crew = BackendDevelopmentCrew(
                workplan_content=workplan_content.decode('utf-8'))

            # Mostrar progreso
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Ejecutar tareas
            with st.spinner('Ejecutando tareas...'):
                result = crew.kickoff(
                    inputs={"workplan_content": workplan_content.decode('utf-8')})

            st.success("¡Código backend generado con éxito!")

            # Mostrar el resultado final
            st.header("Resultado Final")
            st.text_area("Resultado:", result)

            # Mostrar código generado
            st.header("Código Generado")
            if st.checkbox("Mostrar código"):
                try:
                    with open("final_project.zip", "rb") as file:
                        st.download_button(
                            label="Descargar código",
                            data=file,
                            file_name="final_project.zip",
                            mime="application/zip"
                        )
                except FileNotFoundError:
                    st.error(
                        "El archivo final_project.zip no se ha generado aún. Por favor, genera el código primero.")


if __name__ == "__main__":
    main()
