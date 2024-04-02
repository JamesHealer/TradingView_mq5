import threading
import time
from seleniumwire import webdriver
from seleniumwire.utils import decode
import json
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://in.tradingview.com/chart/N0NndNaR/?symbol=NSE%3AINFY")

# Define your cookie
cookie = {
    'name': 'sessionid',
    'value': '266zasrqc8uriryvn2ybkmu0l6fciddt',
    'path': '/',
    'domain': '.tradingview.com',  # Change to the domain of the website
    'secure': True,
    'httpOnly': True
}

driver.add_cookie(cookie)

driver.get("https://tradingview.com/chart/N0NndNaR/?symbol=NSE%3AINFY")


def monitor_requests():
    try:
        while True:
            # Process requests that have been captured
            for request in driver.requests:
                if "list_fires" in request.url and request.response:
                    print(f"URL containing 'list_fires': {request.url}")
                    body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                    body_dict = json.loads(body)
                    fireTime = body_dict['r'][0]['fire_time']
                    message = body_dict['r'][0]['message']
                    print(fireTime)
                    print(message)
            # Clear processed requests to avoid re-processing them
            del driver.requests

            # Wait a short period before checking again
            time.sleep(1)
            try:
                button = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/button[1]")
                button.click()
            except Exception:
                pass

    except KeyboardInterrupt:
        print("Stopping monitoring...")


# Run the monitoring in a background thread
thread = threading.Thread(target=monitor_requests)
thread.start()

print("Monitoring started. Press Ctrl+C to stop.")
try:
    # Keep the main thread alive to allow interrupt
    while thread.is_alive():
        thread.join(timeout=1)
except KeyboardInterrupt:
    print("Stopping script...")

# Cleanup
driver.quit()