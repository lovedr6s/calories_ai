import webview
import threading
import uvicorn


def run_gui():
    uvicorn.run("app.webgui.gui:app", host="127.0.0.1", port=5000, reload=False)


if __name__ == "__main__":
    threading.Thread(target=run_gui, daemon=True).start()
    webview.create_window("Lovedr6s", "http://127.0.0.1:5000", width=350, height=450, resizable=False)
    webview.start()
