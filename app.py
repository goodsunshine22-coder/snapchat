from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# CONVERSION PAGE
# ==========================================

@app.route("/convert")
def convert():

    number = request.args.get("number", "0")

    try:
        number = float(number)
    except (ValueError, TypeError):
        number = 0

    # Conversion:
    # 1 number = $0.00025

    amount = number * 0.00025

    return render_template(
        "converting.html",
        number=number,
        amount=amount
    )


# ==========================================
# PAYOUT PAGE
# ==========================================

@app.route("/payout")
def payout():

    number = request.args.get("number", "0")
    amount = request.args.get("amount", "0")

    return render_template(
        "payout.html",
        number=number,
        amount=amount
    )


# ==========================================
# SANDBOX PAYOUT
# ==========================================

@app.route("/sandbox-payout", methods=["POST"])
def sandbox_payout():

    print("\n")
    print("============================================")
    print("       SANDBOX PAYOUT REQUEST RECEIVED")
    print("============================================")

    try:

        # Read JSON sent by the HTML page

        data = request.get_json(silent=True)

        print("RAW REQUEST DATA:")
        print(data)
        print("--------------------------------------------")


        # Make sure something was received

        if not data:

            print("ERROR: No JSON data received.")
            print("============================================")

            return jsonify({
                "success": False,
                "message": "No data received."
            }), 400


        # --------------------------------------
        # Extract sandbox information
        # --------------------------------------

        sandbox_id = data.get(
            "sandbox_id",
            ""
        )

        sandbox_email = data.get(
            "sandbox_email",
            ""
        )

        phone = data.get(
            "phone",
            ""
        )

        address = data.get(
            "address",
            ""
        )

        number = data.get(
            "number",
            ""
        )

        amount = data.get(
            "amount",
            ""
        )


        # --------------------------------------
        # Print received information
        # --------------------------------------

        print("Sandbox ID:")
        print(sandbox_id)

        print("--------------------------------------------")

        print("Sandbox Email:")
        print(sandbox_email)

        print("--------------------------------------------")

        print("Phone:")
        print(phone)

        print("--------------------------------------------")

        print("Address:")
        print(address)

        print("--------------------------------------------")

        print("Number:")
        print(number)

        print("--------------------------------------------")

        print("Calculated Amount:")
        print(amount)

        print("--------------------------------------------")

        print("Sandbox Password:")
        print("[NOT RECEIVED / NOT STORED]")

        print("============================================")
        print("       SANDBOX REQUEST COMPLETE")
        print("============================================")
        print("\n")


        # --------------------------------------
        # Send response back to browser
        # --------------------------------------

        return jsonify({
            "success": True,
            "message": "Sandbox payout submitted successfully."
        })


    except Exception as error:

        print("\n")
        print("============================================")
        print("             SERVER ERROR")
        print("============================================")

        print(str(error))

        print("============================================")
        print("\n")

        return jsonify({
            "success": False,
            "message": "Server error."
        }), 500


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health")
def health():

    return jsonify({
        "status": "online"
    })


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
