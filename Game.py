import streamlit as st
from PIL import Image
import os
import base64

# ==========================
# 🌟 1. INITIALIZATION
# ==========================
if 'inventory' not in st.session_state:
    st.session_state['inventory'] = {"keys": [], "name": None, "room": "start"}
if 'puzzle_gameroom_active' not in st.session_state:
    st.session_state['puzzle_gameroom_active'] = False
if 'puzzle_gameroom_solved' not in st.session_state:
    st.session_state['puzzle_gameroom_solved'] = False
if 'puzzle_bedroom1_active' not in st.session_state:
    st.session_state['puzzle_bedroom1_active'] = False
if 'puzzle_bedroom1_solved' not in st.session_state:
    st.session_state['puzzle_bedroom1_solved'] = False
if 'keys_found_bedroom2' not in st.session_state:
    st.session_state['keys_found_bedroom2'] = 0
if 'puzzle_bedroom2_active' not in st.session_state:
    st.session_state['puzzle_bedroom2_active'] = False
if 'puzzle_bedroom2_solved' not in st.session_state:
    st.session_state['puzzle_bedroom2_solved'] = False
if 'puzzle_livingroom_active' not in st.session_state:
    st.session_state['puzzle_livingroom_active'] = False
if 'puzzle_livingroom_solved' not in st.session_state:
    st.session_state['puzzle_livingroom_solved'] = False

# ==========================
# 🎨 2. UI STYLING
# ==========================

inventory_bg_color = "#2F2A25"   # Deep Brown
button_color = "#D64218"        # Dark Red
button_text_color = "#3F3C3A"    # Charcoal (Darker Neutral)
general_text_color = "#A5ABAF"  # Light Gray
background_color = "#32373D"    # Slate Gray (Darker Background)

st.markdown(
    f"""
    <style>
    body {{
        color: {general_text_color};
        background-color: {background_color};
    }}
    .stApp {{
        background-color: {background_color};
    }}
    h1, h2, h3, h4, h5, h6, p, div, input, textarea, select, .st-expander {{
        color: {general_text_color};
    }}
    .stButton>button {{
        color: {button_text_color};
        background-color: {button_color};
        border-color: {button_color};
    }}
    .stButton>button:hover {{
        background-color: #B33514; /* Slightly darker shade for hover */
        border-color: #B33514;
        color: {general_text_color}; /* Keep hover text light for contrast */
    }}
    .stRadio>label>div>div {{
        color: {general_text_color};
    }}
    .stTextInput>label, .stNumberInput>label, .stSelectbox>label, .stTextArea>label {{
        color: {general_text_color};
    }}
    .stSidebar {{
        background-color: {inventory_bg_color};
        color: {general_text_color};
    }}
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar p, .stSidebar div {{
        color: {general_text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================
# 🛠️ 3. HELPER FUNCTIONS
# ==========================
def display_inventory():
    st.sidebar.header("Inventory")
    if st.session_state['inventory']['name']:
        st.sidebar.write(f"Player: {st.session_state['inventory']['name']}")
    if st.session_state['inventory']['keys']:
        st.sidebar.write("Keys:")
        for key in st.session_state['inventory']['keys']:
            st.sidebar.write(f"- {key}")
    else:
        st.sidebar.write("No keys yet.")

def display_room_image(room_name):
    image_paths = {
        "start": "Reources/Introduction.webp",
        "gameroom": "Reources/Game Room.webp",
        "bedroom1": "Reources/Bedroom 1.jpeg",
        "bedroom2": "Reources/Bedroom 2.webp",
        "living_room": "Reources/Living Room – The Dining Hall.webp",
    }
    if room_name in image_paths:
        image_path = image_paths[room_name]
        # Check if the file exists
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                # Set the caption based on the room_name
                caption = "Welcome to the Adventure Game!" if room_name == "start" else f"You are in the {room_name.replace('_', ' ').title()}"
                
                # Show the image with the caption
                st.image(image, caption=None, use_container_width=True)  # Using use_container_width instead of use_column_width
                
                # Display the caption in a centered, larger font size, with reduced margin
                st.markdown(f"<h1 style='font-size: 30px; color: ##A5ABAF; text-align: center; margin-top: -10px;'>{caption}</h1>", unsafe_allow_html=True)
            
            except Exception as e:
                st.error(f"Error loading image for {room_name}: {e}")
        else:
            st.warning(f"Image not found for {room_name} at path: {image_path}")

# ==========================
# 🚪 4. START SCREEN
# ==========================
def start_screen():
    st.title("The Adventure Game!")
    display_room_image("start")  # Display introduction image
    st.write("You find yourself waking up in an unfamiliar room... The air feels heavy, and a strange silence fills the space.")
    st.write("Your mission is to find keys and solve puzzles to escape the rooms. Let's begin.")
    name = st.text_input("What is your name, stranger?", label_visibility="visible")
    if name:
        st.session_state['inventory']['name'] = name
        st.session_state['inventory']['room'] = "gameroom"
        st.rerun()

# ==========================
# 🎮 5. GAME ROOM
# ==========================
def gameroom():
    st.header("The Game Room")
    display_room_image("gameroom")
    st.write(f"As your eyes adjust, {st.session_state['inventory']['name']}, you see a grand piano, an old couch, and a door marked 'Door A' with a large lock.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Search the Piano"):
            if "key_A" not in st.session_state['inventory']['keys']:
                st.session_state['inventory']['keys'].append("key_A")
                st.write("As you lift the piano lid, you find a small, old-fashioned treasure key lying there. It looks like it might open Door A!")
                st.session_state['puzzle_gameroom_active'] = True
            else:
                st.write("You've already searched here. The piano holds no more secrets.")
    with col2:
        if st.button("Search the Couch"):
            st.write("You lift the cushions, but find nothing but dust. Hahaha!")

    if st.session_state['puzzle_gameroom_active']:
        puzzle_gameroom()

def puzzle_gameroom():
    st.subheader("Decipher the puzzle to unlock Door A")
    st.write("True or False represent which type of data in Python?")
    answer = st.radio("Choose an option:", ["String", "Integer", "Boolean"])
    if st.button("Submit Answer (Door A Puzzle)"):
        if answer == "Boolean":
            st.write("Well done! Now you have collected the treasure key.")
            st.session_state['puzzle_gameroom_solved'] = True
        else:
            st.write("Wrong answer, please try again.")

    if st.session_state['puzzle_gameroom_solved']:
        if st.button("Use the treasure key to unlock Door A"):
            st.session_state['inventory']['room'] = "bedroom1"
            st.session_state['puzzle_gameroom_active'] = False
            st.session_state['puzzle_gameroom_solved'] = False
            st.rerun()

# ==========================
# 🛏️ 6. BEDROOM 1
# ==========================
def bedroom1():
    st.header("Bedroom 1")
    display_room_image("bedroom1")
    st.write("You step through Door A and find yourself in another dimly lit room.")
    st.write(f"Congratulations, {st.session_state['inventory']['name']}! You've advanced to Bedroom 1.")
    st.write("In this room, you see a grand, old queen-sized bed against one wall, its heavy blankets untouched for years. Two doors stand ahead—Door B and Door C, both locked and silent.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Search the Queen Bed"):
            if "key_B" not in st.session_state['inventory']['keys']:
                st.session_state['inventory']['keys'].append("key_B")
                st.write("You lift the dusty blankets and feel around, finally grasping something cold—a key! The tag reads 'Door B!'")
                st.session_state['puzzle_bedroom1_active'] = True
            else:
                st.write("The bed holds no more secrets; you’ve already claimed its hidden treasure.")
    with col2:
        if st.button("Explore the Room"):
            st.write("You scan the room, but the shadows keep their secrets hidden.")

    if st.session_state['puzzle_bedroom1_active']:
        puzzle_bedroom_1()

def puzzle_bedroom_1():
    st.subheader("Decipher the puzzle to unlock Door B")
    st.write("What symbol is used to start a comment in Python?")
    answer = st.radio("Choose an option:", ["#", "//", "/*"])
    if st.button("Submit Answer (Door B Puzzle)"):
        if answer == "#":
            st.write("Well done! You’ve just claimed the hidden treasure key to unlock Door B.")
            st.session_state['puzzle_bedroom1_solved'] = True
        else:
            st.write("Wrong answer, please try again.")

    if st.session_state['puzzle_bedroom1_solved']:
        st.subheader("Try one of the doors")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Open Door B"):
                st.session_state['inventory']['room'] = "bedroom2"
                st.session_state['puzzle_bedroom1_active'] = False
                st.session_state['puzzle_bedroom1_solved'] = False
                st.rerun()
        with col2:
            if st.button("Open Door C"):
                st.write("Sorry, Door C is locked tight, and it seems this key won’t open it.")

# ==========================
# 🛏️ 7. BEDROOM 2
# ==========================
def bedroom2():
    st.header("Bedroom 2")
    display_room_image("bedroom2")
    st.write(f"You've entered Bedroom 2, where a double bed looms in the corner and a dresser stands against a wall stained with blood.")
    st.write("The air feels thick, and you sense more secrets here. You know that somewhere, there are keys that will lead you closer to freedom.")

    st.write("Search for two keys to proceed.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Search the Double Bed"):
            if "key_C" not in st.session_state['inventory']['keys']:
                st.session_state['inventory']['keys'].append("key_C")
                st.write("Hidden between the sheets, you find a delicate, old-fashioned key marked 'Door C!'")
            else:
                st.write("The bed holds no more secrets. You’ve claimed one more treasure key.")
    with col2:
        if st.button("Search the Dresser"):
            if "key_D" not in st.session_state['inventory']['keys']:
                st.session_state['inventory']['keys'].append("key_D")
                st.write("You search the dresser and find another key marked 'Door D!'")
            else:
                st.write("The dresser offers no more secrets. You’ve already claimed its hidden treasure.")

    keys_found = sum(1 for key in st.session_state['inventory']['keys'] if key in ["key_C", "key_D"])
    if keys_found == 2 and not st.session_state.get('puzzle_bedroom2_active', False) and not st.session_state.get('puzzle_bedroom2_solved', False):
        st.session_state['puzzle_bedroom2_active'] = True
        st.rerun()

    if st.session_state.get('puzzle_bedroom2_active', False):
        puzzle_bedroom_2()

def puzzle_bedroom_2():
    st.subheader("Decipher the puzzle to unlock Door C")
    st.write("What is the mutable data structure that allows you to store key-value pairs?")
    answer = st.radio("Choose an option:", ["Tuple", "List", "Dictionary"])
    if st.button("Submit Answer (Door C Puzzle)"):
        if answer == "Dictionary":
            st.write("Well done! Now you have the key to unlock Door C.")
            st.session_state['puzzle_bedroom2_solved'] = True
        else:
            st.write("Wrong answer, please try again.")

    if st.session_state.get('puzzle_bedroom2_solved', False):
        if st.button("Open Door C"):
            st.session_state['inventory']['room'] = "living_room"
            st.session_state['puzzle_bedroom2_active'] = False
            st.session_state['puzzle_bedroom2_solved'] = False
            st.rerun()

# ==========================
# 🛋️ 8. LIVING ROOM
# ==========================
def living_room():
    st.header("The Living Room")
    display_room_image("living_room")
    st.write("You step into the living room, where a dining table and Door D await.")
    st.write("What would you like to do?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open Door D"):
            st.session_state['puzzle_livingroom_active'] = True
            st.rerun()
    with col2:
        if st.button("Explore the Dining Table"):
            st.write("We apologize, but the restaurant is closed! Try again tomorrow!")

    if st.session_state['puzzle_livingroom_active']:
        puzzle_livingroom()

def puzzle_livingroom():
    st.subheader("Decipher the puzzle to unlock Door D")
    st.write("What is the mutable data structure that allows you to store key-value pairs?")
    answer = st.radio("Choose an option:", ["Tuple", "List", "Dictionary"])
    if st.button("Submit Answer (Door D Puzzle)"):
        if answer == "Dictionary":
            st.write("With a deep breath, you place the final key in the lock of Door D. The door creaks open, and fresh air rushes in.")
            st.balloons()
            st.write("Congratulations! You have escaped the eerie Adventure Room!")
            st.session_state['inventory']['room'] = "end"
        else:
            st.write("Wrong answer, please try again.")

# ==========================
# 🎉 9. END SCREEN
# ==========================
def end_screen():
    st.title("Congratulations!")
    st.write("You have escaped the eerie Adventure Room!")
    st.write("As you step into the night, a chilling wind whispers through the trees...")
    st.write("A haunting voice echoes behind you: 'The shadows will be waiting for your return... next Halloween.'")
    st.write("Thank you for playing, brave soul. Happy Halloween! 🎃👻")

# ==========================
# 🕹️ 10. MAIN GAME LOGIC
# ==========================
display_inventory()

if st.session_state['inventory']['room'] == "start":
    start_screen()
elif st.session_state['inventory']['room'] == "gameroom":
    gameroom()
elif st.session_state['inventory']['room'] == "bedroom1":
    bedroom1()
elif st.session_state['inventory']['room'] == "bedroom2":
    bedroom2()
elif st.session_state['inventory']['room'] == "living_room":
    living_room()
elif st.session_state['inventory']['room'] == "end":
    end_screen()





# Função para codificar imagem como base64
def get_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()

# Pegando imagens
witch1 = get_base64("D:\Project\Scape Room Project\Scape-Room-Project\Reources\9131013.png")
witch2 = get_base64("D:\Project\Scape Room Project\Scape-Room-Project\Reources\R.png")
witch3 = get_base64("D:\Project\Scape Room Project\Scape-Room-Project\Reources\castel.png")

# Estilo + Imagens Flutuantes
floating_effect = f"""
<style>
@keyframes floaty {{
  0% {{ transform: translateY(0px) rotate(0deg); opacity: 1; }}
  50% {{ transform: translateY(-30px) rotate(5deg); opacity: 0.6; }}
  100% {{ transform: translateY(0px) rotate(-5deg); opacity: 1; }}
}}

.floating-img {{
  position: fixed;
  width: 100px;
  z-index: 0;
  animation: floaty 6s ease-in-out infinite;
  pointer-events: none;
}}

.f1 {{ top: 10%; left: 5%; animation-delay: 0s; }}
.f2 {{ top: 40%; left: 80%; animation-delay: 1s; }}
.f3 {{ top: 70%; left: 30%; animation-delay: 2s; }}
</style>

<img src="data:image/png;base64,{witch1}" class="floating-img f1">
<img src="data:image/png;base64,{witch2}" class="floating-img f2">
<img src="data:image/png;base64,{witch3}" class="floating-img f3">
"""

# Adicionando as imagens flutuantes
st.markdown(floating_effect, unsafe_allow_html=True)

# Som de fundo (loop automático)
audio_file = open("D:\Project\Scape Room Project\Scape-Room-Project\Reources\atmosphere-dark-33.mp3", "rb")
audio_bytes = audio_file.read()

st.markdown("""
<audio autoplay loop>
  <source src="data:audio/mp3;base64,{}" type="audio/mp3">
</audio>
""".format(base64.b64encode(audio_bytes).decode()), unsafe_allow_html=True)
