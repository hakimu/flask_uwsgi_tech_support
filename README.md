### This is a Flask app being served by uWSGI.

The application entry point is:

```
app = Flask(__name__)
```

The app is run with the Python agent with the following command:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --http :8080 -w app:app --single-interpreter --enable-threads
```
