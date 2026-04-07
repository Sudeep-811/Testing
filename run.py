from app import create_app, db
from app.monitor import monitor_loop
import threading

app = create_app()


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    thread = threading.Thread(target=monitor_loop)
    thread.daemon = True
    thread.start()

    app.run(debug=True, host='0.0.0.0')