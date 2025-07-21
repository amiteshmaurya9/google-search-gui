import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def perform_search():
    query = search_entry.get()
    output_box.delete(1.0, tk.END)

    if not query:
        output_box.insert(tk.END, "Please enter a search query.\n")
        return

    try:
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(20)

        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        for i, result in enumerate(results[:5], 1):
            output_box.insert(tk.END, f"{i}. {result.text}\n")

        driver.quit()

    except Exception as e:
        output_box.insert(tk.END, f"Error: {str(e)}")

# GUI layout
window = tk.Tk()
window.title("Google Search Automation")
window.geometry("500x400")

tk.Label(window, text="Enter Search Query:", font=("Arial", 12)).pack(pady=10)
search_entry = tk.Entry(window, width=50, font=("Arial", 12))
search_entry.pack()

tk.Button(window, text="Start Search", command=perform_search, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

output_box = scrolledtext.ScrolledText(window, width=60, height=15, font=("Consolas", 10))
output_box.pack(pady=10)

window.mainloop()
