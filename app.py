import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Smart Solar Micro Hub", layout="wide")
st.markdown("""
<style>
:root {
    color-scheme: light !important;
}
</style>
""", unsafe_allow_html=True)
# ---------- MOBILE DETECTION FLAG ----------
# 📱 Detect screen width
# 📱 SAFE MOBILE DETECTION
screen_width = streamlit_js_eval(
    js_expressions='window.innerWidth',
    key='screen_width'
)

# Initialize only once
if "is_mobile" not in st.session_state:
    st.session_state.is_mobile = False

# Update ONLY when valid value comes
if isinstance(screen_width, (int, float)):
    st.session_state.is_mobile = screen_width < 768

# AUTO DETECT SCREEN SIZE
# Default (CSS will handle mobile)
# until we implement JS detection


st.markdown("<style>body { margin: 0; }</style>", unsafe_allow_html=True)
st.markdown("""
<style>

/* NAVBAR BOX */
.navbar-container {
    background: #ffffff;
    padding: 10px 20px;
    border-bottom: 1px solid #e2e8f0;

    display: flex;
    align-items: center;
    justify-content: space-between;

    z-index: 10;
}
.nav-btn {
    padding: 8px 16px;
    border-radius: 10px;
    border: 1px solid transparent;
    background: transparent;
    color: #64748b;
    font-weight: 500;
    transition: all 0.25s ease;
}

.nav-btn:hover {
    background: #f1f5f9;
    color: #0f172a;
}

/* ACTIVE TAB */
.nav-active {
    background: #dcfce7 !important;
    color: #16a34a !important;
    border: 1px solid #bbf7d0 !important;
    font-weight: 600;
}
button {
    white-space: nowrap !important;
    min-width: 100px;
}
 button:hover {
    background: #ecfdf5 !important;
    border-color: #22c55e !important;
    color: #16a34a !important;
}
/* ALIGN CONTENT CENTER */


/* REDUCE BUTTON SIZE */
button {
    padding: 6px 12px !important;
    font-size: 13px !important;
    min-width: auto !important;
}


</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>


/* REMOVE INTERNAL GAP */
div[data-testid="stVerticalBlock"] {
    gap: 0rem !important;
}

/* REMOVE FIRST CHILD SPACE */
div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: 0rem !important;
    padding-top: 0rem !important;
}


 
 
</style>
""", unsafe_allow_html=True)




st.markdown("""
<style>

/* FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background-color: #f8fafc !important;
}

body {
    background-color: #f8fafc;
}

/* HERO SECTION */
.hero {
    background: linear-gradient(135deg, #16a34a, #2563eb);
    padding: 40px;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-bottom: 10px;
}

.hero h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 16px;
    opacity: 1;
    color: #e2e8f0;
}

/* CARDS */
.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    text-align: center;
    margin-top: 12px;
    margin-bottom: 12px;
    border: 1px solid #e2e8f0;
    transition: all 0.25s ease;
    color: #1e293b;
}
.component-card {
    background: #f8fafc;
    border: 2px solid #22c55e;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 15px;
    transition: 0.3s;
}

.component-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 8px 20px rgba(34,197,94,0.2);
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.12);
}
.section-title {
    font-size: 22px;
    font-weight: 600;
    color: #0f172a;
    margin-top: 10px;
    margin-bottom: 10px;
}
/* 🔍 Search box styling */
div[data-testid="stTextInput"] {
    background: white;
    padding: 10px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 10px;
}

div[data-testid="stTextInput"] input {
    border: none !important;
    outline: none !important;
}
/* HOW STEPS */
.step {
    text-align: center;
    padding: 15px;
    border-radius: 12px;
    background: #f8fafc;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}
.step-card {
    text-align: center;
    padding: 20px;
}

.step-circle {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #22c55e, #3b82f6);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: bold;
    margin: auto;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}

.step-title {
    font-weight: 600;
    margin-top: 12px;
    color: #1e293b;
}

.step-desc {
    font-size: 13px;
    color: #64748b;
    margin-top: 5px;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* 📱 GLOBAL MOBILE SPACING FIX */
@media (max-width: 768px) {

    /* Main container padding */
    .block-container {
        padding: 1rem !important;
    }

    /* Reduce section spacing */
    .card {
        margin-top: 8px !important;
        margin-bottom: 8px !important;
        padding: 15px !important;
    }

    /* Reduce step card spacing */
    .step-card {
        padding: 12px !important;
    }

    /* Fix headings spacing */
    h1, h2, h3 {
        margin-bottom: 8px !important;
    }

    /* Reduce gap between sections */
    div[data-testid="stVerticalBlock"] {
        gap: 0.5rem !important;
    }

}
/* 📱 MOBILE HERO FIX */
@media (max-width: 768px) {

    .hero {
        padding: 20px !important;
        border-radius: 12px !important;
    }

    .hero h1 {
        font-size: 22px !important;
    }

    .hero p {
        font-size: 13px !important;
    }

}

/* 🌞 RESPONSIVE SOLAR SECTION */
.solar-flex {
    display: flex;
    gap: 30px;
    align-items: center;
}

/* 📱 MOBILE FIX */
@media (max-width: 768px) {
    .solar-flex {
        flex-direction: column !important;
        text-align: center;
    }
}
/* 📱 MOBILE BUTTON FIX */
@media (max-width: 768px) {

    button {
        width: 100% !important;
        padding: 12px !important;
        font-size: 15px !important;
        border-radius: 12px !important;
    }

}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* 🔥 FORCE SELECTBOX FULL WHITE */
div[data-baseweb="select"] * {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* SELECT BOX MAIN */
div[data-baseweb="select"] {
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 10px !important;
}

/* DROPDOWN */
ul[role="listbox"] * {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* 🔥 NUMBER INPUT FULL FIX */
div[data-testid="stNumberInput"] * {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* 🔥 TEXT INPUT FULL FIX */
div[data-testid="stTextInput"] * {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* 🔥 INPUT FIELD BORDER */
input {
    background-color: #ffffff !important;
    color: #0f172a !important;
    border: none !important;
}

/* 🔥 REMOVE DARK MODE ROOT */
html, body, .stApp {
    background-color: #f8fafc !important;
    color: #0f172a !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* 🔥 FIX SELECTBOX (BLACK BAR ISSUE) */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #0f172a !important;
    border: 1px solid #e2e8f0 !important;
}

/* DROPDOWN MENU */
ul[role="listbox"] {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* 🔥 FIX NUMBER INPUT */
div[data-testid="stNumberInput"] input {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* 🔥 FIX TEXT INPUT (SEARCH BAR) */
div[data-testid="stTextInput"] input {
    background-color: #ffffff !important;
    color: #0f172a !important;
}

/* 🔥 FIX INPUT CONTAINER (IMPORTANT) */
div[data-testid="stTextInput"],
div[data-testid="stNumberInput"] {
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 10px !important;
}

/* 🔥 REMOVE DARK BACKGROUND FROM ALL INPUT WRAPPERS */
div[data-baseweb="input"] {
    background-color: #ffffff !important;
}

/* 🔥 FORCE LIGHT MODE */
section[data-testid="stSidebar"],
section[data-testid="stMain"] {
    background-color: #f8fafc !important;
}

</style>
""", unsafe_allow_html=True)


# ---------- NAVIGATION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------- TOP NAVBAR ----------

# ---------- FIXED NAVBAR ----------


# ---------- CLEAN SINGLE NAVBAR ----------

# ---------- RESPONSIVE NAVBAR ----------

is_mobile = st.session_state.get("is_mobile", False)

# 📱 MOBILE VIEW → SIDEBAR MENU
if is_mobile:
    st.markdown("### 🌞 Smart Solar Micro Hub")


    # Sync sidebar with page (SAFE FIX)
    if "page" not in st.session_state:
     st.session_state.page = "Home"

    menu = st.sidebar.radio(
    "☰ Menu",
    ["Home", "Calculate", "About"],
    index=["Home","Calculate","About"].index(st.session_state.page),
    key="Menu"
)

# ✅ Only update if user changes sidebar
   # ✅ SAFE SYNC (NO OVERRIDE)
    if "Menu" in st.session_state:
      st.session_state.page = st.session_state.Menu

# 💻 DESKTOP VIEW → KEEP OLD NAVBAR
else:
    st.markdown('<div class="navbar-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([5,5])

    with col1:
        st.markdown("### 🌞 Smart Solar Micro Hub")

    with col2:
        st.markdown('<div class="navbar-right">', unsafe_allow_html=True)
        b1, b2, b3 = st.columns([1,1,1], gap="small")

        current = st.session_state.page

        with b1:
            if st.button("Home", key="home_btn"):
                st.session_state.page = "Home"
                st.rerun()
            st.markdown(
                f"<style>#home_btn button {{ {'background:#dcfce7; color:#16a34a; border:1px solid #bbf7d0;' if current=='Home' else ''} }}</style>",
                unsafe_allow_html=True
            )

        with b2:
            if st.button("Calculate", key="calc_btn"):
                st.session_state.page = "Calculate"
                st.rerun()
            st.markdown(
                f"<style>#calc_btn button {{ {'background:#dcfce7; color:#16a34a; border:1px solid #bbf7d0;' if current=='Calculate' else ''} }}</style>",
                unsafe_allow_html=True
            )

        with b3:
            if st.button("About", key="about_btn"):
                st.session_state.page = "About"
                st.rerun()
            st.markdown(
                f"<style>#about_btn button {{ {'background:#dcfce7; color:#16a34a; border:1px solid #bbf7d0;' if current=='About' else ''} }}</style>",
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
# ---------- HOME ----------
if st.session_state.page == "Home":
    
    # ---------- HERO SECTION ----------
    st.markdown("""
    <div class="hero">
        <h1>🌞 Smart Solar Micro Hub</h1>
        <p>Transform your rooftop into a clean energy source with smart solar insights</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
   
    # ---------- FEATURES ----------
    import streamlit as st

    is_mobile = st.session_state.get("is_mobile", False)

    if is_mobile:
      col1 = st.container()
      col2 = st.container()
      col3 = st.container()
    else:
      col1, col2, col3 = st.columns(3)
    

    with col1:
        st.markdown("""
        <div class="card">
            <h3>⚡ Precise Calculations</h3>
            <p>Estimate exact solar requirements based on your usage</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>💰 Cost Savings</h3>
            <p>Calculate ROI, payback period and long-term savings</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🌍 Environmental Impact</h3>
            <p>Track CO₂ reduction and sustainability benefits</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

    

    # ---------- HOW IT WORKS ----------
    st.markdown("""
<div style="
background:white;
padding:20px;
border-radius:16px;
box-shadow:0px 4px 15px rgba(0,0,0,0.05);
margin-top:20px;
margin-bottom:20px;
">
<h2>⚙️ How It Works</h2>
</div>
""", unsafe_allow_html=True)

    if is_mobile:
     c1 = st.container()
     c2 = st.container()
     c3 = st.container()
     c4 = st.container()
    else:
     c1, c2, c3, c4 = st.columns(4)

    with c1:
     st.markdown("""
     <div class="step-card">
        <div class="step-circle">1</div>
        <div class="step-title">Enter Details</div>
        <div class="step-desc">
        Provide your location, rooftop area, and list your electrical appliances
        </div>
    </div>
    """, unsafe_allow_html=True)

    with c2:
     st.markdown("""
     <div class="step-card">
        <div class="step-circle">2</div>
        <div class="step-title">Smart Analysis</div>
        <div class="step-desc">
        Our system calculates optimal panel placement and energy generation potential
        </div>
    </div>
    """, unsafe_allow_html=True)

    with c3:
     st.markdown("""
     <div class="step-card">
        <div class="step-circle">3</div>
        <div class="step-title">View Results</div>
        <div class="step-desc">
        Get detailed reports on costs, savings, and environmental impact
        </div>
    </div>
    """, unsafe_allow_html=True)

    with c4:
     st.markdown("""
     <div class="step-card">
        <div class="step-circle">4</div>
        <div class="step-title">Take Action</div>
        <div class="step-desc">
        Use insights to make informed decisions about solar installation
        </div>
    </div>
    """, unsafe_allow_html=True)


   # ---------- WHY CHOOSE SOLAR ----------
    st.markdown("""
     <div style="
     background: #f1f5f9;
     padding: 30px;
     border-radius: 16px;
     box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
     margin-top: 20px;
     ">

     <div class="solar-flex">

     <!-- LEFT TEXT -->
     <div style="flex:1;">
     <h2 style="color:#0f172a;">Why Choose Solar Energy?</h2>

     <p style="color:#334155; margin-top:10px;">✔ Reduce electricity bills by up to 90%</p>
     <p style="color:#334155;">✔ Protection from rising energy costs</p>
     <p style="color:#334155;">✔ Increase property value</p>
     <p style="color:#334155;">✔ Low maintenance with 25+ year lifespan</p>
     <p style="color:#334155;">✔ Government incentives and subsidies</p>
     <p style="color:#334155;">✔ Energy independence and reliability</p>

     </div>

     <!-- RIGHT IMAGE -->
     <div style="flex:1; text-align:center;">
     <img src="https://images.unsplash.com/photo-1614366502473-e54666693b44?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxzdXN0YWJsZSUyMGVuZXJneSUyMGdyZWVuJTIwZW52aXJvbm1lbnR8ZW58MXx8fHwxNzc0MzMzMzI5fDA&ixlib=rb-4.1.0&q=80&w=1080"
     style="
     width:100%;
     max-width:340px;
     height:220px;
     object-fit:cover;
     border-radius:16px;
     box-shadow:0px 8px 25px rgba(0,0,0,0.2);
     ">
     </div>
     </div>
     """, unsafe_allow_html=True)

    # ---------- CTA ----------
    st.markdown("""
      <div style="
      background: linear-gradient(135deg, #16a34a, #2563eb);
      padding:25px;
      border-radius:14px;
      text-align:center;
      color:white;
      margin-top:20px;
      ">
      <h3>🚀 Ready to Start Your Solar Journey?</h3>
      </div>
    """, unsafe_allow_html=True)

    

    if st.button("⚡ Go to Calculate Section →", use_container_width=True):
      st.session_state.page = "Calculate"   # 🔥 IMPORTANT
      st.rerun()
     
      

elif st.session_state.page == "Calculate":
    st.markdown("""
     <div style="
     background: linear-gradient(135deg, #16a34a, #2563eb);
     padding:20px;
     border-radius:14px;
     color:white;
     text-align:center;
     margin-bottom:20px;
     ">
     <h2>⚡ Smart Solar Analysis Dashboard</h2>
     <p>Analyze your solar potential, savings & sustainability</p>
     </div>
     """, unsafe_allow_html=True)
    
    
    

    
    city_data = {
            "Hyderabad, Telangana": {"sun": 5.5, "rate": 7.5},
            "Mumbai, Maharashtra": {"sun": 5.0, "rate": 8.0},
            "Delhi, Delhi": {"sun": 4.5, "rate": 7.0},
            "Chennai, Tamil Nadu": {"sun": 5.5, "rate": 6.5},
            "Bangalore, Karnataka": {"sun": 5.2, "rate": 7.2},
            "Kolkata, West Bengal": {"sun": 4.8, "rate": 6.8},
            "Pune, Maharashtra": {"sun": 5.3, "rate": 7.5},
            "Ahmedabad, Gujarat": {"sun": 5.8, "rate": 6.5},
            "Jaipur, Rajasthan": {"sun": 6.0, "rate": 6.0},
            "Lucknow, Uttar Pradesh": {"sun": 4.7, "rate": 6.8}
        }

    st.markdown("""
<div style="
background:#ffffff;
padding:20px;
border-radius:16px;
box-shadow:0px 4px 15px rgba(0,0,0,0.05);
border:1px solid #e2e8f0;
margin-bottom:10px;
">
<h3 style="margin:0;">📍 Location & Property Details</h3>
</div>
""", unsafe_allow_html=True)

       # 🔹 Select City
    st.markdown("<p style='font-weight:600; margin-bottom:8px;'>📍 Select Your City</p>", unsafe_allow_html=True)
    selected_city = st.selectbox("", list(city_data.keys()), label_visibility="collapsed")
  
    sun_hours = city_data[selected_city]["sun"]
    electricity_rate = city_data[selected_city]["rate"]

      # 🔹 Info Box
    st.markdown(f"""
<div style="
background:#eef2f7;
padding:14px;
border-radius:10px;
margin-top:10px;
font-size:14px;
color:#1e293b;
border:1px solid #e2e8f0;
">
☀ Avg. sun hours: {sun_hours}h/day &nbsp;&nbsp;&nbsp;
⚡ Electricity rate: ₹{electricity_rate}/kWh
</div>
""", unsafe_allow_html=True)

      # 🔹 Roof Area
    roof_area = st.number_input(
       "Available Roof Area (sq ft)",
       min_value=100,
       max_value=5000,
       value=500,
       help="Measure your rooftop space available for solar panels"
    )
    

    st.markdown("<br>", unsafe_allow_html=True)
    

    
    st.markdown("""
        <div style="
        background:#ffffff;
        padding:20px;
        border-radius:16px;
        box-shadow:0 4px 20px rgba(0,0,0,0.06);
        border:1px solid #e2e8f0;
        margin-bottom:15px;
        ">
        <h3 style="color:#0f172a; font-weight:600;">⚡ Add Your Appliances</h3>
        <p style="color:#64748b;">Select appliances and usage to calculate energy consumption</p>
        </div>
        """, unsafe_allow_html=True)

   
    # Device data
    device_data = {
       "Lighting": {
           "LED Bulb": 10,
           "Tube Light": 20,
           "CFL": 15,
           "Halogen Lamp": 50
    },

    "Cooling": {
        "Fan": 75,
        "Ceiling Fan": 80,
        "Table Fan": 60,
        "Cooler": 200,
        "AC (1 Ton)": 1200,
        "AC (1.5 Ton)": 1800,
        "AC (2 Ton)": 2500
    },

    "Kitchen": {
        "Refrigerator": 150,
        "Microwave": 1200,
        "Induction Stove": 1800,
        "Electric Kettle": 1500,
        "Mixer Grinder": 500,
        "Dishwasher": 1300,
        "Toaster": 800
    },

    "Heating": {
        "Water Heater (Geyser)": 2000,
        "Room Heater": 1500,
        "Electric Iron": 1000
    },

    "Electronics": {
        "TV": 100,
        "Laptop": 60,
        "Desktop Computer": 200,
        "WiFi Router": 10,
        "Mobile Charger": 5,
        "Gaming Console": 150
    },

    "Laundry": {
        "Washing Machine": 500,
        "Dryer": 2000
    },

    "Cleaning": {
        "Vacuum Cleaner": 1200,
        "Water Pump": 750
    },

    "Others": {
        "Elevator (small)": 3000,
        "Printer": 50,
        "Air Purifier": 60,
        "Inverter": 100
    }
}   
     # Category selection
    category = st.selectbox("Select Category", list(device_data.keys()))
    # Store device data permanently
    if "devices" not in st.session_state:
      st.session_state.devices = {}
    
    devices = device_data[category]

    

    i = 0
    

    search = st.text_input("🔍 Search devices...")
    st.markdown("<br>", unsafe_allow_html=True)

    filtered_devices = {
    d:p for d,p in devices.items()
    if search.lower() in d.lower()
    }

    if st.session_state.get("is_mobile", False):
      cols = [st.container()]
    else:
      cols = st.columns(2)    # 2 columns
    i = 0
    for device, power in filtered_devices.items():

     col = cols[i % len(cols)]

     selected = device in st.session_state.devices
     card_bg = "#dcfce7" if selected else "#ffffff"
     border = "#22c55e" if selected else "#e2e8f0"

     with col:
        st.markdown(f"""
        <div style="
        background:{card_bg};
        padding:16px;
        border-radius:14px;
        border:1.5px solid {border};
        box-shadow:0 4px 12px rgba(0,0,0,0.05);
        margin-bottom:12px;
        ">
        <div style="font-weight:600;">{device}</div>
        <div style="color:#64748b; font-size:13px;">{power} W</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "➕" if not selected else "✔ Added",
            key=f"add_{device}",
            use_container_width=True
        ):
            st.session_state.devices[device] = {
                "power": power,
                "hours": 5,
                "qty": 1
            }

     i += 1

   

    # Calculate consumption
    total_consumption = 0

    for device, data in st.session_state.devices.items():
      power = data["power"]
      qty = data["qty"]
      hours = data["hours"]

      total_consumption += power * qty * hours

    total_consumption = total_consumption / 1000
    
    st.markdown("""
<div style="
background:#ffffff;
padding:18px;
border-radius:14px;
border:1px solid #e2e8f0;
margin-top:10px;
margin-bottom:10px;
">
<h3>🧾 Selected Devices</h3>
</div>
""", unsafe_allow_html=True)


    if not st.session_state.devices:

     st.markdown("""
      <div style="
      background:#ffffff;
      padding:40px;
      border-radius:16px;
      border:1px solid #e2e8f0;
      text-align:center;
      color:#64748b;
      box-shadow:0px 4px 15px rgba(0,0,0,0.05);
      ">
      <h4>🏠 No devices added yet</h4>
      <p>Select from the device library</p>
      </div>
      """, unsafe_allow_html=True)

    else:
     for device, data in st.session_state.devices.items():

      energy = (data["power"] * data["qty"] * data["hours"]) / 1000

      # 🔥 ENERGY LEVEL COLOR (smart UI)
      if energy < 1:
        bar_color = "#22c55e"   # green
      elif energy < 3:
        bar_color = "#f59e0b"   # orange
      else:
        bar_color = "#ef4444"   # red

      # 🔥 GLASS CARD UI
      st.markdown(f"""
      <div style="
      background: #ffffff;
      padding:20px;
      border-radius:18px;
      border:1px solid #e2e8f0;            
      margin-bottom:15px;
      box-shadow:0px 8px 25px rgba(0,0,0,0.08);
      ">

      <div style="display:flex; justify-content:space-between;">
        <div>
            <b style="font-size:18px;">{device}</b><br>
            <span style="color:#64748b;">⚡ {energy:.2f} kWh/day</span>
        </div>
      </div>

      <!-- 🔥 ENERGY BAR -->
      <div style="
        margin-top:10px;
        height:8px;
        border-radius:10px;
        background:#e5e7eb;
        overflow:hidden;
      ">
        <div style="
            width:{min(100, energy*20)}%;
            height:100%;
            background:{bar_color};
            transition:0.3s;
        "></div>
      </div>

      </div>
     """, unsafe_allow_html=True)

      # 🔹 CLEAN SLIDER SECTION
      if st.session_state.is_mobile:
        col1 = st.container()
        col2 = st.container()
      else:
         col1, col2 = st.columns(2)

      with col1:
        qty = st.slider(
            f"🔢 Quantity ({device})",
            1, 10, data["qty"],
            key=f"qty_{device}"
        )

      with col2:
        hours = st.slider(
            f"⏱ Hours/day ({device})",
            1, 24, data["hours"],
            key=f"hours_{device}"
        )
  
     # SAVE VALUES
      st.session_state.devices[device]["qty"] = qty
      st.session_state.devices[device]["hours"] = hours

      # 🔴 REMOVE BUTTON
     if st.button(f"❌ Remove {device}", key=f"remove_{device}"):
        del st.session_state.devices[device]
        st.rerun()

     st.markdown("<div style='margin-bottom:25px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"""
    <div style="
    background:#ffffff;
    padding:20px;
    border-radius:16px;
    box-shadow:0 4px 20px rgba(0,0,0,0.06);
    border:1px solid #e2e8f0;
    margin-bottom:15px;
    ">
    🔋 Total Daily Consumption: {round(total_consumption,2)} kWh
    </div>
    """, unsafe_allow_html=True)
    st.write(f"📊 Estimated Monthly Consumption: {round(total_consumption*30,2)} kWh")
    
    if total_consumption == 0:
       st.warning("⚠ Please select at least one appliance")
    st.markdown("<br><br>", unsafe_allow_html=True)
    generate = st.button("⚡ Generate Smart Report", use_container_width=True)

    if generate:

     with st.spinner("⚡ Analyzing your energy usage..."):
        import time
        time.sleep(1.5)

     if total_consumption == 0:
        st.warning("⚠ Please select at least one appliance before generating report")
        st.stop()

     monthly_units = total_consumption * 30
        # Required capacity based on consumption
     required_capacity = monthly_units / 30 / sun_hours  # kW needed

        # Max capacity based on roof
     max_capacity = roof_area / 100

        # Final capacity (min of both)
     capacity = min(required_capacity, max_capacity)

     panels = capacity / 0.4

     daily_gen = capacity * sun_hours
     monthly_gen = daily_gen * 30

        

     annual_savings = monthly_gen * 12 * electricity_rate
     co2 = monthly_gen * 12 * 0.82 / 1000

     score = int((monthly_gen / monthly_units) * 50) if monthly_units != 0 else 0

     st.markdown("""
     <div style="
     background:#ffffff;
     padding:20px;
     border-radius:16px;
     box-shadow:0 4px 20px rgba(0,0,0,0.06);
     border:1px solid #e2e8f0;
     margin-bottom:15px;
     ">
     <h3>📊 Solar Analysis Report</h3>
     </div>
     """, unsafe_allow_html=True)

     st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

     st.markdown(f"""
             <div style="text-align:center; margin-bottom:20px;">
          <div style="
            width:120px;
            height:120px;
            border-radius:50%;
            background: linear-gradient(135deg, #16a34a, #2563eb);
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:34px;
            color:white;
            margin:auto;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
          ">
            {score}
         </div>
         <h3 style="margin-top:10px;">Sustainability Score</h3>
         </div>
         """, unsafe_allow_html=True)
     solar_percent = min(100, (monthly_gen / monthly_units) * 100) if monthly_units != 0 else 0
     col1, col2, col3, col4 = st.columns(4)

     col1.metric("🔆 Panels Required", int(panels))
     col2.metric("⚡ Energy Coverage", f"{round(solar_percent,1)}%")
     col3.metric("💰 Annual Savings", f"₹{int(annual_savings)}")
     col4.metric("🌍 CO₂ Reduction", f"{round(co2,2)} tons")

     st.markdown("<br>", unsafe_allow_html=True)
     st.markdown("---")
        
     st.subheader("💰 Financial Insights")

     investment = capacity * 50000
     payback = investment / annual_savings if annual_savings != 0 else 0

     col1, col2 = st.columns(2)

     col1.metric("Investment", f"₹{int(investment)}")
     col2.metric("Payback (Years)", f"{round(payback,1)}")
     st.markdown("---")
     st.markdown("<br>", unsafe_allow_html=True)

     st.subheader("⚡ Energy Analysis")
     st.write(f"🌞 Sun Hours Used: {sun_hours} h/day")
     st.write(f"💡 Electricity Rate: ₹{electricity_rate}/kWh")
     col1, col2 = st.columns(2)

     with col1:
        st.write(f"🔋 Daily Consumption: {round(total_consumption,2)} kWh")
        st.write(f"📊 Monthly Consumption: {round(monthly_units,2)} kWh")

     with col2:
        st.write(f"☀️ Daily Generation: {round(daily_gen,2)} kWh")
        st.write(f"📈 Monthly Generation: {round(monthly_gen,2)} kWh")
        st.markdown("<br>", unsafe_allow_html=True)
        # Graph
     st.markdown("---")
     st.markdown("""
     <div style="
     background:#ffffff;
     padding:20px;
     border-radius:16px;
     box-shadow:0 4px 20px rgba(0,0,0,0.06);
     border:1px solid #e2e8f0;
     margin-bottom:15px;
     ">
     <h3>📈 Energy Visualization</h3>
     </div>
     """, unsafe_allow_html=True)
        
     labels = ['Solar', 'Grid']
        
     solar_percent = (monthly_gen / monthly_units) * 100 if monthly_units != 0 else 0
     grid_percent = 100 - solar_percent
     if solar_percent == 0 and grid_percent == 0:
      sizes = [1, 0]
     else:
       sizes = [solar_percent, grid_percent]
     solar_val = monthly_gen
     grid_val = max(0, monthly_units - monthly_gen)

     df = {
     "Source": ["Solar", "Grid"],
     "Energy": [solar_val, grid_val]
       }

     fig_pie = px.pie(
     df,
     names="Source",
     values="Energy",
     hole=0.6
     )

     fig_pie.update_layout(
     height=300,
     margin=dict(t=10, b=10, l=10, r=10)
     )

     st.plotly_chart(fig_pie, use_container_width=True)
     months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        
     season_factor = {
        "Hyderabad, Telangana": [0.95,1,1.1,1.2,1.3,1.2,0.8,0.75,1,1.05,1,0.95],
        "Delhi, Delhi": [0.8,0.9,1.1,1.2,1.3,1.1,0.7,0.6,0.9,1,0.9,0.8],
        "Mumbai, Maharashtra": [0.85,0.9,1,1.1,1.2,1.0,0.6,0.5,0.9,1,0.95,0.85]
        }

     factors = season_factor.get(selected_city, [1]*12)
     gen_data = [monthly_gen * f for f in factors]
     cons_data = [monthly_units * (0.9 + 0.2*f) for f in factors]

     fig_line = go.Figure()

     fig_line.add_trace(go.Scatter(
     x=months,
     y=gen_data,
     mode='lines+markers',
     name='Solar Generation'
     ))

     fig_line.add_trace(go.Scatter(
     x=months,
     y=cons_data,
     mode='lines+markers',
     name='Consumption',
     line=dict(dash='dash')
     ))

     fig_line.update_layout(
     height=350,
     margin=dict(t=20, b=20),
     xaxis_title="Month",
     yaxis_title="Energy (kWh)"
     )

     st.plotly_chart(fig_line, use_container_width=True)

     st.markdown("---")
     st.markdown("### 📊 Energy Comparison Dashboard")

     col1, col2 = st.columns(2)

     col1.metric("Monthly Consumption", f"{round(monthly_units,1)} kWh")
     col2.metric("Solar Generation", f"{round(monthly_gen,1)} kWh")

     difference = monthly_gen - monthly_units

     if difference >= 0:
      st.success(f"✔ Surplus Energy: {round(difference,1)} kWh")
     else:
      st.error(f"⚠ Deficit Energy: {round(abs(difference),1)} kWh")
     st.markdown("---")
     st.markdown("""
        <div style="
        background:#f0fdf4;
        padding:20px;
        border-radius:14px;
        margin-top:20px;
        ">
        <h3>💡 Smart Recommendations</h3>
        </div>
        """, unsafe_allow_html=True)
        
        
    if "monthly_gen" in locals() and "monthly_units" in locals():

     if monthly_gen > monthly_units:
        st.success("✔ Your solar system can fully cover your energy needs")
     else:
        st.warning("⚠ Consider increasing panel capacity")

     if panels > 20:
        st.info("✔ Suitable for large rooftop installation")

     if total_consumption > 10:
        st.warning("⚠ High consumption detected – optimize usage")

     st.write("✔ Consider adding battery storage for backup")

# ---------- ABOUT ----------
elif st.session_state.page == "About":
    st.markdown("""
         <div class="card">
         <h1>🌞 About Solar Energy</h1>
         <p>Learn how solar power works and why it is the future of clean energy</p>
         </div>
         """, unsafe_allow_html=True)
    st.markdown("""
<img src="https://images.unsplash.com/photo-1762958266408-5a8278e26506?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxzb2xhciUyMHBvd2VyJTIwdGVjaG5vbG9neSUyMGNsZWFuJTIwZW5lcmd5fGVufDF8fHx8MTc3NDMzMzMyOXww&ixlib=rb-4.1.0&q=80&w=1080"
style="
width:100%;
height:260px;
object-fit:cover;
border-radius:18px;
margin-top:15px;
box-shadow:0px 8px 25px rgba(0,0,0,0.15);
">
""", unsafe_allow_html=True)
    
    st.markdown("""
     <div class="card">
     Solar energy is a renewable and sustainable source of power that converts sunlight into electricity.
     It helps reduce electricity costs, lower carbon emissions, and promote clean energy usage.
     </div>
     """, unsafe_allow_html=True)
    

    st.markdown("---")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # HOW IT WORKS
    st.markdown('<div class="section-title">⚡ How Solar Energy Works</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <img src="https://cdn-icons-png.flaticon.com/512/869/869869.png" width="50"/>
            <h4>Solar Panels</h4>
            <p>Capture sunlight and convert it into DC electricity.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <img src="https://cdn-icons-png.flaticon.com/512/2933/2933245.png" width="50"/>
            <h4>Inverter</h4>
            <p>Converts DC electricity into AC power.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <img src="https://cdn-icons-png.flaticon.com/512/1048/1048953.png" width="50"/>
            <h4>Battery</h4>
            <p>Stores energy for later use.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # COMPONENTS
    st.markdown('<div class="section-title">⚙️ Key Components</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="component-card">
<b>🔆 Solar Panels</b>
<p>Convert sunlight into electricity. Typically rated at 300-450W per panel. Monocrystalline panels offer higher efficiency while polycrystalline are more cost-effective.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="component-card">
<b>🔌 Inverter</b>
<p>Converts DC power from panels to AC power for home use. String inverters are common, while micro-inverters offer panel-level optimization.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="component-card">
<b>🔋 Battery Storage (Optional)</b>
<p>Stores excess energy for use during night or power outages. Lithium-ion batteries are most common.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="component-card">
<b>🏠 Mounting Structure</b>
<p>Secure framework to hold panels on rooftops. Must be sturdy and positioned for optimal sun exposure.</p>
</div>
""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # BENEFITS
    st.markdown('<div class="section-title">🌍 Benefits</div>', unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    with col1:
     st.markdown("""
     <div class="card">
     <b>💰 Reduce Electricity Bills</b>
     <p>Save up to 90% on monthly electricity costs and protect yourself from rising energy prices</p>

     <b>🌱 Environmental Benefits</b>
     <p>Reduce carbon footprint and contribute to fighting climate change with clean, renewable energy</p>
     </div>
     """, unsafe_allow_html=True)
    with col2:
     st.markdown("""
     <div class="card">
     <b>⚡ Energy Independence</b>
     <p>Generate your own power and reduce dependence on unreliable grid electricity</p>

     <b>🏡 Increase Property Value</b>
     <p>Homes with solar installations have higher resale values and attract eco-conscious buyers</p>
     </div>
     """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # FACTS
    st.markdown('<div class="section-title">📊 Solar Facts</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average solar panel lifespan", "25+ Years")
    col2.metric("Efficiency after 25 years", "80%+")
    col3.metric("Powers 200 homes", "1 MW")

    st.markdown("---")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # IMAGES (SIDE BY SIDE)
    st.markdown('<div class="section-title">🔍 Solar in Action</div>', unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <img src="https://cleanenergyactionproject.com/wp-content/uploads/2023/11/house-with-solar-panels.jpg">
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <img src="https://www.anernstore.com/cdn/shop/articles/Components_of_a_residential_solar_power_system_wit.png?v=1754999192&width=1200">
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # INDIA SECTION
    

    st.markdown("""
<div style="
background: linear-gradient(135deg, #f0fdf4, #ecfeff);
padding: 30px;
border-radius: 18px;
border: 1px solid #d1fae5;
box-shadow: 0px 6px 20px rgba(0,0,0,0.05);">

<h3 style="margin-bottom:10px;"> Solar Energy in India</h3>

<p>
India receives approximately 5,000 trillion kWh of solar radiation annually,
making it one of the most favorable locations for solar energy in the world.
</p>

<ul>
<li>30–40% subsidy on residential solar</li>
<li>Net metering policies</li>
<li>Low-interest loans</li>
<li>Tax benefits</li>
</ul>

<p>
India aims to achieve 500 GW renewable capacity by 2030.
</p>

</div>
""", unsafe_allow_html=True)