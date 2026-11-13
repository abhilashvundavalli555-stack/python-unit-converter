from flask import Flask, render_template, request

from converter import UNIT_FACTORS, convert_value

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    form = {
        "category": "Length",
        "value": "",
        "from_unit": "Meters (m)",
        "to_unit": "Kilometers (km)",
    }
    result = None
    error = None

    if request.method == "POST":
        form.update(
            category=request.form.get("category", ""),
            value=request.form.get("value", "").strip(),
            from_unit=request.form.get("from_unit", ""),
            to_unit=request.form.get("to_unit", ""),
        )
        try:
            value = float(form["value"])
            result = convert_value(
                value, form["category"], form["from_unit"], form["to_unit"]
            )
        except ValueError as exc:
            error = str(exc) or "Enter a valid number."

    return render_template(
        "index.html",
        categories=UNIT_FACTORS,
        form=form,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
