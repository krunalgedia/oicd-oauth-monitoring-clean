import os
from flask import Flask, request

app = Flask(__name__)

# Change this back to just '/'
@app.route('/')
def hello():
    user_email = request.headers.get('X-User-Email', 'Unknown User')
    
    # Log it securely to Google Cloud Logging
    print(f"SECURITY LOG: API accessed successfully by {user_email}")
    
    # Send a custom response back to the user
    return f"Hello {user_email} from Cloud Run!\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))