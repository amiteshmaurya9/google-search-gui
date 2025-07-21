# Google Search Automation GUI using Python and Selenium

This is a simple Python GUI application that performs a Google search based on user input using **Tkinter** and **Selenium**. It automates the browser to search the query on Google and displays the top results in a scrollable text area.

---

## 💡 Features

- User-friendly Tkinter GUI.
- Automates Google search using Selenium.
- Displays top 5 search result titles.

---

## 🛠️ Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (must match your Chrome version)
- Required Python packages:

```bash
pip install selenium
🚀 Run the Application
bash
Copy
Edit
python main.py
🧠 How It Works
Takes a search term from the user

Opens Chrome using Selenium

Searches the query on Google

Extracts titles of the top 5 results (<h3> elements)

Displays the results in the GUI

⚠️ Notes
If you get No results found, try increasing the time.sleep(20) line to give Google more time to load.

Google might change its structure or block bot-like behavior.

👨‍💻 Developer
Amitesh Maurya
🔗 amiteshmaurya.com


