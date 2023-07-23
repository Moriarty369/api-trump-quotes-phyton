from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q=technology")
    response.raise_for_status()
    response_data = response.json()
    quote = response_data["message"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Si das click en mi linda cara te doy un consejo sobre tecnología", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="trump_face.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()