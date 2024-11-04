from flask import Flask, request, jsonify
import logging
import os
from datetime import datetime

app = Flask(__name__)

os.makedirs('logs', exist_ok=True)

date_str = datetime.now().strftime('%Y-%m-%d')
log_file = f'logs/app_{date_str}.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'CONNECT', 'TRACE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'CONNECT', 'TRACE'])
def catch_all(path):
    url = request.url
    headers = dict(request.headers)
    data = request.get_data(as_text=True) if request.data else None
    method = request.method
    
    logging.info(f"URL: {url}")
    logging.info(f"Method: {method}")
    logging.info(f"Headers: {headers}")
    logging.info(f"Request Body: {data}")

    response_data = {
        "message": "Request received and logged",
        "url": url,
        "method": method,
        "headers": headers,
        "body": data
    }
    response = jsonify(response_data)
    
    logging.info(f"Response: {response_data}\r\n")
    
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
