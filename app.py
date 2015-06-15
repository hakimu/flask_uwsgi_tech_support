from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hellooooo World!!!"

if __name__ == '__main__':
  app.run()

# NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --http :8080 -w app:app --single-interpreter --enable-threads
