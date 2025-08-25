
import webbrowser
import os

def main():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "aaron.html"))
    webbrowser.open(f"file://{html_path}")
    print("Opened aaron.html in your default browser.")

if __name__ == "__main__":
    main()
