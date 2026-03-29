import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/v1')
def hello():
    # 1. Grab the name tag Apigee pinned to the request!
    # If the header is missing for some reason, it defaults to 'Unknown User'
    user_email = request.headers.get('X-User-Email', 'Unknown User')
    
    # 2. Log it securely to Google Cloud Logging
    print(f"SECURITY LOG: API accessed successfully by {user_email}")
    
    # 3. Send a custom response back to the user
    return f"Hello {user_email} from Cloud Run!\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))