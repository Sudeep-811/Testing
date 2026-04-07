import time
import requests
from app import db, create_app
from app.models import Monitor

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return "UP" if response.status_code == 200 else "DOWN"
    except:
        return "DOWN"


def monitor_loop():
    app = create_app()

    with app.app_context():
        while True:
            monitors = Monitor.query.all()

            for monitor in monitors:
                status = check_url(monitor.url)
                monitor.status = status

            db.session.commit()

            print("Checked all monitors...")
            time.sleep(10)  # check every 10 sec