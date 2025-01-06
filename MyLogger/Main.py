from App import app
from Logger import Logger
import threading

if __name__ == '__main__':
    import Routes
    threading.Thread(target=Logger, daemon=True).start()
    app.run(port=5001)
