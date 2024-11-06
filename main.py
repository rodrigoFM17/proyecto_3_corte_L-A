from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from maquinaTuringSuma import TuringMachineRomanSum
from maquinaTuringResta import TuringMachineRomanSubtraction
from maquinaTuringMultiplicacion import TuringMachineRomanMultiplication
from maquinaTuringDivision import TuringMachineRomanDivision

app = Flask(__name__)
app.secret_key= "secret"

class Form(FlaskForm):
    number1 = StringField("numero 1", validators=[DataRequired()])
    number2 = StringField("numero 2", validators=[DataRequired()])
    operator = SelectField(
        "seleccione una operacion",
        choices=[("add", "+"), ("substract", "-"), ("multiply", "x"), ("divide", "/")],
        validators=[DataRequired()]
    )
    operate = SubmitField("Realizar operacion")

@app.route('/', methods=['GET', 'POST'])
def operar():
    form = Form()
    result = None
    if form.validate_on_submit():
        number1 = form.number1.data
        number2 = form.number2.data
        operator = form.operator.data
        turing = None
        input_tape = number1 + "#" + number2

        if operator == "add":
            turing = TuringMachineRomanSum(input_tape)
        elif operator == "substract":
            turing = TuringMachineRomanSubtraction(input_tape)
        elif operator == "multiply":
            turing = TuringMachineRomanMultiplication(input_tape)
        elif operator == "divide":
            turing = TuringMachineRomanDivision(input_tape)
        
        result = turing.run()

        print(operator, result)

        flash(f"{number1}, {number2}", "success")
        
    return render_template("index.html", form=form, result=result)

if __name__=="__main__":
    app.run(debug=True)