from wf import WApp, render_template


app = WApp(host="localhost", port=80)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", title="Welcome", message="Welcome to the Simple Web Framework!")


if __name__ == '__main__':
    app.run()
