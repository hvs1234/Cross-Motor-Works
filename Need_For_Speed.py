from streamlit import *
import plotly.express as px
import base64
set_page_config(page_icon=":rocket:",page_title="Need For Speed",layout="wide")
df = px.data.iris()

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.webp")

hide="""
   <style>
   #MainMenu {visibility: hidden;}
   footer {visibility: hidden;}
   header {visibility: hidden;}
   </style>
"""
page_customize= f"""
<style>
[data-testid="stAppViewContainer"] > .main{{
background-image: url("https://preview.redd.it/wc3xjjobjd841.jpg?auto=webp&s=f0524d6bb3d72507e66ad1c9ecf95273b7df9e2e");
background-size: cover;
}}

[data-testid="stSidebar"] {{
background-image: url("data:image/png;base64,{img}");
background-size: 35%;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""

def local_css(file_name):
    with open(file_name) as f:
        markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

sidebar.title("Contact Us !!!")
contact_form = """
<form action="https://formsubmit.co/3469harshsharma@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your Name" required>
<input type="email" name="email" placeholder="Your Email" required>
<textarea name="message" placeholder="Your message here" required></textarea>
<button type="submit">Send</button>
</form>
"""
# --------------------------------------------------------
sidebar.write("---")
sidebar.markdown(contact_form,unsafe_allow_html=True)
local_css("style/style.css")
sidebar.write("---")
sidebar.write("Join Our Team. Hurry Up !")
# --------------------------------------------------------
markdown(hide,unsafe_allow_html=True)
markdown(page_customize,unsafe_allow_html=True)
with container():
   left,mid,right = columns(((2,2,2)))
   with left:
      write("Welcome To :wave:")
      header("Cross Motor Works")
      text("Advanced Technology cars")
      title("Need For Speed")
      text("Build up your own speed")
      header("Car service center")
      header("Provide best build qualities")
   with mid:
      empty() 
   with right:
      write("Best car dealership")
      header("Provide Tags")
      text("Future Development vehicles")
      title("Royal Cars")
      text("Automated Technology")
      header("Fully Electric")
      header("Takeover a lease")

write("---")
header(":bulb: Details")
write(""" 
   - Company Name: Cross Motor Works :oncoming_automobile:
   - Location: Vikasnagar Dehradun Uttarakand, India :earth_asia:
   - Entry Fee: Rs 45 :dollar:
   - Open Timing: Morning-10:30 AM To 1:30 PM, Evening-3:00 PM To 8:00 PM
   - Sunday Closed
""")
write("---")
header(":rocket: Exclusive and low cost car rental")
title("NEED A LUXURY CAR ?")
header("We offer the best price luxury car rental service in dehradun")
subheader(":telephone_receiver: +91-9149349278")
subheader(":e-mail: info@motorworks.com")
subheader(":globe_with_meridians: www.motorworks.com")
title(":speech_balloon: Why texting works for car sales ?")
subheader("Business texting works for car dealerships in more than one way."
"First, it allows car dealers to stay in touch with potential buyers in a personal and low-key way."
"Many back-and-forths occur in the car buying process, and texting is quick and easy to keep on top of for all parties involved."
"The average text message is read within three minutes and has a 45 percent response rate.")
write("---")
header("Higher advanced technology")
header("Best Cars for Tech Lovers for 2023")
write("""### 
### . 2021 Ford Mustang Mach-E. An electric SUV with muscle car genes. ...
### . 2021 Mercedes-Benz S-Class. A luxury flagship sedan filled to the gills with tech. ...
### . 2021 Tesla Model Y. Stylish and tech-rich SUV. ...
### . 2021 Nissan Versa. ...
### . 2021 Ford F-150 PowerBoost Hybrid.
""")
write(" "); write(" "); write(" "); write(" ")
header("Best Supercars for 2023")
write("""###
### . McLaren 720S - the do-everything supercar. ...
### . Ferrari 296 GTB - the one to flatter your ego. ...
### . Lamborghini Huracan STO - the pinup you want to drive. ...
### . Maserati MC20 - the leftfield one. ...
### . Audi R8 - the 911 Turbo beater. ...
### . McLaren Artura - the future of McLaren. ...
### . Honda NSX - the rational one.
""")
write("---")
header("You call it going beyond :link:")
title("All Accessories available")
header("All Services available :link:")
subheader(". Car Maintenance and modification")
subheader(". Car Painting and Polishing")
subheader(". Wheel Balancing")
write("---")
title("Buy your own choice ...")
header("Best Cars Available for 2023")
write("""### 
### 1. Mustang :oncoming_automobile:
### . Model Name: Mustang Mach-E
### . Company Name: Ford
### . HP: 480
### . Price: $69,895 :dollar:
""")
write("---")
write("""### 
### 2. Lamborghini :oncoming_automobile:
### . Model Name: Aventador LP 780-4 Ultimae
### . Company Name: Automobili Lamborghini S.p.A
### . HP: 769
### . Price: $498,258 :dollar:
""")
write("---")
write("""### 
### 3. Mercedes :oncoming_automobile:
### . Model Name: Mercedes-Benz GLC
### . Company Name: Mercedes-Benz Group AG
### . HP: 255
### . Price: $43,850 :dollar:
""")
write("---")
write("""### 
### 4. Tiago :oncoming_automobile:
### . Model Name: Tata Tiago EV
### . Company Name: Tata
### . HP: 236
### . Price: $9,937 :dollar:
""")
write("---")
write("""### 
### 5. Dodge Challenger :oncoming_automobile:
### . Model Name: Challenger SRT
### . Company Name: Dodge
### . HP: 807
### . Price: $66,045 :dollar:
""")
write("---")
write("""### 
### 6. Rolls Royce :oncoming_automobile:
### . Model Name: Rolls-Royce Phantom 
### . Company Name: Ford
### . HP: 414
### . Price: $11,17,950 :dollar:
""")
write("---")
with container():
    left,mid,right = columns(((2,2,2)))
    with left:
        write("""
        ### About us
        - Persistance Plans
        - Good Requirements
        - Company Development
        - Foreign Center
        - Provided Offers
        - Less Consistency
        """)
    with mid:
        write("""
        ### Support
        - Company
        - Service Center
        - Customer Query
        - Customer Service
        - Car Driving Experience
        - Feedback
        """)
    with right:
        write("""
        ### Neighborhoods in India
        - Lutyen's Dehli
        - Jew Town
        - Santacruz, Mumbai
        - Nizamuddin
        - Halasuru
        - Little India
        """)
write("---")
text("Thanks for visiting our site !!!")
