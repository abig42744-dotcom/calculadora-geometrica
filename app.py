
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import base64

st.set_page_config(
    page_title="Mi calculadora de Geometría",
    page_icon="💻",
    layout="centered"
)
# Imagen de fondo
with open("fondo.jpg", "rb") as imagen:
    fondo = base64.b64encode(imagen.read()).decode()

st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/jpg;base64,{fondo}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

</style>
""", unsafe_allow_html=True)

# Diseño y colores
st.markdown("""
<style>
.stApp {
    background-color: #F8F5FF;
}

h1 {
    color: #8064A8;
    text-align: center;
}

h2, h3 {
    color: #9879BD;
}

p {
    color: #625674;
}

/* Recuadros */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF;
    border: 2px solid #E5D9F5;
    border-radius: 15px;
    padding: 15px;
}

/* Campos para escribir */
div[data-testid="stNumberInput"] input {
    background-color: #F7F2FF;
    border: 1px solid #D9C7EF;
    border-radius: 10px;
}

/* Botón largo */
.stButton {
    width: 100%;
}
.stButton > button {
    width: 100% !important;
    display: block;
    height: 60px;
    background-color: #A88BCB;
    color: white;
    border: none;
    border-radius: 15px;
    font-size: 21px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #8D70B3;
    color: white;
}

.stButton > button:hover {
    background-color: #8D70B3;
    color: white;
}

/* Resultados */
div[data-testid="stMetric"] {
    background-color: #F6F0FF;
    border: 1px solid #E1D2F3;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# Título principal
st.title(" Mi calculadora de Geometría ")


st.write("")

st.info(" Ingresa las coordenadas de los dos puntos para comenzar: ")


# Coordenadas
st.subheader("🌷 Coordenadas de los puntos 🌷")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🌸 Punto A")
        x1 = st.number_input("X1", value=1.0)
        y1 = st.number_input("Y1", value=2.0)

with col2:
    with st.container(border=True):
        st.markdown("### 🌸 Punto B")
        x2 = st.number_input("X2", value=4.0)
        y2 = st.number_input("Y2", value=6.0)


st.write("")

# Botón
if st.button(" CALCULAR", use_container_width=True):

    # Distancia
    distancia = np.sqrt((x2-x1)**2 + (y2-y1)**2)

    # Punto medio
    xm = (x1+x2)/2
    ym = (y1+y2)/2

    # Resultados
    st.subheader(" Resultados:  💗")

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.metric("📏 Distancia", f"{distancia:.2f}")

    with col4:
        with st.container(border=True):
            st.metric("📍 Punto medio", f"({xm:.2f}, {ym:.2f})")

    # Pendiente y ecuación
    with st.container(border=True):
        if x2 != x1:
            m = (y2-y1)/(x2-x1)
            b = y1-m*x1

            st.markdown("### 🌸 Pendiente")
            st.write(f"**{m:.2f}**")

            st.markdown("### 📝 Ecuación de la recta")
            st.write(f"y = {m:.2f}x + {b:.2f}")

        else:
            st.markdown("### 🌸 Pendiente")
            st.write("No definida")

            st.markdown("### 📝 Ecuación de la recta")
            st.write(f"x = {x1}")

    # Gráfica
    st.subheader(" Plano cartesiano")

    with st.container(border=True):

        fig, ax = plt.subplots(figsize=(7, 5))

        # Puntos A y B
        ax.scatter(
            [x1, x2], [y1, y2],
            color="#B58AD9",
            s=110,
            label="Puntos A y B",
            zorder=3
        )

        # Recta
        ax.plot(
            [x1, x2], [y1, y2],
            color="#8D70B3",
            linewidth=2.5,
            label="Recta AB"
        )

        # Punto medio
        ax.scatter(
            xm, ym,
            color="#E5A6CD",
            s=110,
            label="Punto medio",
            zorder=4
        )

        # Nombres
        ax.annotate("A", (x1, y1), xytext=(6, 8),
                    textcoords="offset points")

        ax.annotate("B", (x2, y2), xytext=(6, 8),
                    textcoords="offset points")

        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.set_title("Gráfica de los puntos")

        ax.axhline(0, color="#B8A8C9")
        ax.axvline(0, color="#B8A8C9")

        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend()

        fig.patch.set_facecolor("#FFFFFF")
        ax.set_facecolor("#FAF7FF")

        st.pyplot(fig)

    st.success("¡Listo! Tus cálculos se realizaron correctamente !")
