from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('Task', validators=[DataRequired()])  #validators are the list of validation checks, here it specifies field cant be empty
    description = TextAreaField('Description',validators=[DataRequired()])
    priority = SelectField('Task Priority', choices = [("High", "High"), ("Medium", "Medium"),("Low", "Low")], validators = [DataRequired()])
    completed = SelectField('Completed Task?', choices = [("YES", "Completed"), ("NO", "Not Completed")], validators = [DataRequired()])
    
    submit = SubmitField("Add Todo")