from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert")
def convert():
    number = request.args.get("number", "0")

    try:
        number = float(number)
    except ValueError:
        number = 0

    amount = number * 0.00025

    return render_template(
        "converting.html",
        number=number,
        amount=amount
    )


@app.route("/payout")
def payout():
    number = request.args.get("number", "0")
    amount = request.args.get("amount", "0")

    return render_template(
        "payout.html",
        number=number,
        amount=amount
    )


@app.route("/sandbox-payout", methods=["POST"])
def sandbox_payout():

    data = request.get_json()

    sandbox_id = data.get("sandbox_id", "").strip()
    sandbox_email = data.get("sandbox_email", "").strip()
    phone = data.get("phone", "").strip()
    address = data.get("address", "").strip()
    number = data.get("number", "")
    amount = data.get("amount", "")

    # Password is deliberately NOT accepted, stored, or logged.

    print("\n==============================")
    print("SANDBOX PAYOUT REQUEST")
    print("==============================")
    print(f"Sandbox ID: {sandbox_id}")
    print(f"Sandbox Email: {sandbox_email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")
    print(f"Number: {number}")
    print(f"Calculated Amount: ${amount}")
    print("==============================\n")

    return jsonify({
        "success": True,
        "message": "Sandbox payout submitted successfully."
    })


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
