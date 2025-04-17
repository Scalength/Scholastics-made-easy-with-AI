from groq import Groq
import re, os, keyboard, pyperclip, time, pyautogui as pygui


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extract_answer_letter(text):
    match = re.search(r"\b([A-D])\b", text)
    if match:
        return match.group(1)
    return None


def AI_Inquiry(text):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""Answer of the correct letter only please. {text}"""
        }
    ],
    model="llama-3.3-70b-versatile",
)
    return(chat_completion.choices[0].message.content)

def drag_click(x, y, xx, yy, duration=0.2):
    pygui.moveTo(x, y)
    pygui.mouseDown()
    pygui.moveTo(xx, yy, duration=duration)
    pygui.mouseUp()
    
def click(x, y):
    pygui.moveTo(x, y)
    pygui.mouseDown()
    time.sleep(1)
    pygui.mouseUp()
    
def clickanswer(x, y, duration=0.2):
    # Move the mouse to the location smoothly
    pygui.moveTo(x, y, duration=duration)
    time.sleep(0.2)

    # Click the location with mouseDown and mouseUp
    pygui.mouseDown()
    pygui.mouseUp()
    time.sleep(0.5)  # Slight delay after the click to ensure it's registered

attempts = 0
max_attempt = 10
running = True
paused = False

def startQuizNow():
    global attempts
    while attempts < max_attempt:
        click(179, 615)
        drag_click(23, 195, 1810, 615)
        pygui.hotkey("ctrl", "c")
        
        clipboard_text = pyperclip.paste()
        
        answer_coords = {
            "A": (206, 311),
            "B": (1185, 319),
            "C": (215, 423),
            "D": (1139, 433)
        }
        answer = extract_answer_letter(AI_Inquiry(clipboard_text))
        # Check if copied_text is one of the answers and perform the corresponding clicks
        if answer in answer_coords:
            # Click the start of the quiz (focus the quiz)
            pygui.click(193, 760)

            # Perform the answer selection click
            clickanswer(answer_coords[answer][0], answer_coords[answer][1])
            # Click the final submit button (common for all answers)
            click(1721, 951)

        attempts += 1
        
        
    

while True:
    if keyboard.is_pressed("e"):  # Press 'e' to restart the process
        print("Starting")
        attempts = 0
        startQuizNow()
        time.sleep(1)
