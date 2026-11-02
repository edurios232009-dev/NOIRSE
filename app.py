import streamlit as st
 
# ---------------------------------------------------------------
# NOIRE - tienda de ropa lisa, sin logos
# Ejecuta con:  streamlit run app.py
# ---------------------------------------------------------------
 
st.set_page_config(page_title="NOIRE", page_icon="🧥", layout="wide")
 
# ---------- Paleta (cálida y fina) ----------
IVORY = "#FAF6EF"     # fondo
SAND = "#EDE3D3"      # superficies suaves
CAMEL = "#B08968"     # acento
MOCHA = "#6F4E37"     # texto secundario
ESPRESSO = "#2A1D17"  # texto principal / botones
BORDEAUX = "#6B2D33"  # detalles
 
# ---------- Productos ----------
PRODUCTO = {
    "nombre": "Sudadera lisa de algodón",
    "precio": 800,
    "descripcion": (
        "Sudadera de cuello redondo en algodón grueso y suave, "
        "de corte clásico y sin logotipos. Puños y dobladillo acanalados."
    ),
    "detalles": [
        "100% algodón de peso medio",
        "Corte regular, cuello redondo",
        "Puños y dobladillo acanalados",
        "Sin logotipo ni estampados",
    ],
    "colores": {"Camel": "#B08968", "Chocolate": "#5A3A29", "Marfil": "#E6DAC6"},
    "tallas": ["S", "M", "L", "XL"],
}
 
# ---------- Estilos ----------
st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap');
 
html, body, [class*="css"], .stApp {{
    font-family: 'Jost', sans-serif;
    background-color: {IVORY};
    color: {ESPRESSO};
}}
header[data-testid="stHeader"] {{ background: transparent; }}
.block-container {{ padding-top: 0 !important; max-width: 1200px; }}
 
.aviso {{
    background: {ESPRESSO};
    color: {SAND};
    text-align: center;
    padding: 10px 0;
    font-size: 0.85rem;
    letter-spacing: 0.08em;
    margin: 0 -9999px;
    padding-left: 9999px;
    padding-right: 9999px;
}}
.marca {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.2rem;
    font-weight: 500;
    letter-spacing: 0.35em;
    text-align: center;
    margin: 36px 0 6px 0;
    color: {ESPRESSO};
}}
.menu {{
    display: flex;
    justify-content: center;
    gap: 36px;
    padding: 14px 0 18px 0;
    border-bottom: 1px solid {SAND};
    font-size: 0.95rem;
    color: {MOCHA};
}}
.hero {{
    background: {SAND};
    padding: 70px 20px;
    text-align: center;
    margin: 28px 0 48px 0;
}}
.hero h2 {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.8rem;
    font-weight: 500;
    margin: 0 0 10px 0;
    color: {ESPRESSO};
}}
.hero p {{ color: {MOCHA}; font-size: 1.05rem; margin: 0; }}
 
.vitrina {{
    background: {SAND};
    padding: 30px;
    display: flex;
    justify-content: center;
}}
.ruta {{ color: {MOCHA}; font-size: 0.85rem; margin-bottom: 10px; }}
.producto {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
    font-weight: 500;
    line-height: 1.15;
    margin: 0 0 8px 0;
}}
.precio {{ font-size: 1.5rem; color: {BORDEAUX}; margin-bottom: 18px; }}
.desc {{ color: {MOCHA}; line-height: 1.7; margin-bottom: 18px; max-width: 460px; }}
.detalles li {{ color: {MOCHA}; margin-bottom: 6px; }}
 
.pie {{
    margin-top: 70px;
    padding: 36px 0;
    border-top: 1px solid {SAND};
    text-align: center;
    color: {MOCHA};
    font-size: 0.85rem;
}}
 
/* Botones */
div.stButton > button {{
    background: {ESPRESSO};
    color: {IVORY};
    border: none;
    border-radius: 0;
    padding: 14px 0;
    width: 100%;
    letter-spacing: 0.08em;
    font-family: 'Jost', sans-serif;
    transition: background 0.25s ease;
}}
div.stButton > button:hover {{ background: {BORDEAUX}; color: {IVORY}; }}
div.stButton > button:focus-visible {{ outline: 2px solid {CAMEL}; outline-offset: 2px; }}
 
/* Etiquetas de los selectores */
label, .stRadio label {{ color: {ESPRESSO} !important; }}
</style>
""",
    unsafe_allow_html=True,
)
 
 
def dibujar_sudadera(color: str) -> str:
    """Sudadera lisa en SVG, sin logo, del color elegido."""
    return f"""
<svg viewBox="0 0 400 460" width="380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sudadera lisa">
  <path d="M145 35 L98 52 L28 215 L82 242 L112 170 L112 400 L288 400 L288 170 L318 242 L372 215 L302 52 L255 35 Q200 78 145 35 Z"
        fill="{color}" stroke="rgba(0,0,0,0.12)" stroke-width="1.5"/>
  <path d="M145 35 Q200 90 255 35" fill="none" stroke="rgba(0,0,0,0.22)" stroke-width="6" stroke-linecap="round"/>
  <rect x="112" y="378" width="176" height="24" fill="rgba(0,0,0,0.10)"/>
  <path d="M28 215 L82 242" stroke="rgba(0,0,0,0.18)" stroke-width="14" stroke-linecap="round"/>
  <path d="M372 215 L318 242" stroke="rgba(0,0,0,0.18)" stroke-width="14" stroke-linecap="round"/>
</svg>
"""
 
 
# ---------- Estado del carrito ----------
if "carrito" not in st.session_state:
    st.session_state.carrito = []
 
# ---------- Encabezado ----------
st.markdown(
    f"""
<div class="aviso">ENVÍO GRATIS EN COMPRAS MAYORES A $1,500 MXN</div>
<div class="marca">NOIRE</div>
<div class="menu">
<span>Nuevo</span><span>Hombre</span><span>Mujer</span><span>Sudaderas</span><span>Básicos</span>
</div>
""",
    unsafe_allow_html=True,
)
 
col_vacia, col_bolsa = st.columns([6, 1])
with col_bolsa:
    st.markdown(
        f"<div style='text-align:right; color:{MOCHA}; padding-top:8px;'>"
        f"Bolsa ({len(st.session_state.carrito)})</div>",
        unsafe_allow_html=True,
    )
 
# ---------- Hero ----------
st.markdown(
    """
<div class="hero">
<h2>Lo esencial, bien hecho</h2>
<p>Prendas lisas, sin logos, pensadas para durar.</p>
</div>
""",
    unsafe_allow_html=True,
)
 
# ---------- Producto ----------
col_img, col_info = st.columns([1.1, 1], gap="large")
 
with col_info:
    st.markdown(
        f"""
<div class="ruta">Inicio / Hombre / Sudaderas</div>
<div class="producto">{PRODUCTO['nombre']}</div>
<div class="precio">${PRODUCTO['precio']:,} MXN</div>
<div class="desc">{PRODUCTO['descripcion']}</div>
""",
        unsafe_allow_html=True,
    )
 
    color_nombre = st.radio("Color", list(PRODUCTO["colores"].keys()), horizontal=True)
    talla = st.radio("Talla", PRODUCTO["tallas"], horizontal=True)
    cantidad = st.number_input("Cantidad", min_value=1, max_value=10, value=1, step=1)
 
    if st.button("AGREGAR A LA BOLSA"):
        st.session_state.carrito.append(
            {
                "producto": PRODUCTO["nombre"],
                "color": color_nombre,
                "talla": talla,
                "cantidad": int(cantidad),
                "precio": PRODUCTO["precio"],
            }
        )
        st.toast(f"Agregaste {cantidad} × {PRODUCTO['nombre']} a la bolsa")
        st.rerun()
 
    st.markdown(
        "<ul class='detalles'>"
        + "".join(f"<li>{d}</li>" for d in PRODUCTO["detalles"])
        + "</ul>",
        unsafe_allow_html=True,
    )
 
with col_img:
    st.markdown(
        f"<div class='vitrina'>{dibujar_sudadera(PRODUCTO['colores'][color_nombre])}</div>",
        unsafe_allow_html=True,
    )
 
# ---------- Bolsa ----------
if st.session_state.carrito:
    st.markdown("---")
    st.subheader("Tu bolsa")
    total = 0
    for item in st.session_state.carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        st.write(
            f"{item['producto']} · {item['color']} · talla {item['talla']} · "
            f"{item['cantidad']} × ${item['precio']:,} = **${subtotal:,} MXN**"
        )
    st.markdown(f"### Total: ${total:,} MXN")
    if st.button("VACIAR BOLSA"):
        st.session_state.carrito = []
        st.rerun()
 
# ---------- Pie ----------
st.markdown(
    "<div class='pie'>NOIRE · Ropa lisa, sin logos · © 2026</div>",
    unsafe_allow_html=True,
)
 
