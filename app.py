from flask import Flask,render_template,jsonify
import random
import threading
import time






app=Flask(__name__)
timers=[0,0,0,0,0,0]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/timer")
def timer():
    value=random.randint(1,100)
    return jsonify({
        "values":timers
    })
def update_timer(id,r):
    while True:
        timers[id]=random.randint(1,100)
        time.sleep(r)
refresh_rates=[0.5,1,2,3,5,7]
threads_started = False

@app.before_request
def initialize_threads():

    start_threads()
def start_threads():

    global threads_started

    if threads_started:
        return

    refresh_rates = [
        0.5,
        1,
        2,
        3,
        5,
        7
    ]

    for i in range(6):

        t = threading.Thread(
            target=update_timer,
            args=(i, refresh_rates[i])
        )

        t.daemon = True
        t.start()

    threads_started = True


if __name__ == "__main__":
   app.run(debug=True)
