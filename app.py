from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
	now = datetime.datetime.now()
	return render_template('hello.html',name=name, now=now)

if __name__ == '__main__':
  app.run()

