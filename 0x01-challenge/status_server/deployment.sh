# Example deployment script
#!/bin/bash
export FLASK_APP=api.v1.app
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=5000
