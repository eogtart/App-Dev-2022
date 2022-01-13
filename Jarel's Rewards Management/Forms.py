from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField, DateField
from flask_wtf.file import FileField


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])


class CreateRewardForm(Form):
    name = StringField('Name of Reward', [validators.Length(min=1, max=150), validators.DataRequired()])
    desc = StringField('Reward Description', [validators.Length(min=1, max=500), validators.DataRequired()])
    points = IntegerField('Points to Redeem Reward', [validators.number_range(min=100, max=99999, message="An integer between 1 & 100000"), validators.DataRequired()])
    date = DateField('Expiry Date of Reward', [validators.DataRequired()])
    type = RadioField('Reward Type', choices=[('V', 'Voucher'), ('C', 'Cashback'), ('U', 'Unknown')], default='U')


class CreateRecipeForm(Form):
    name = StringField('Recipe Name', [validators.length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Recipe Description', [validators.length(min=1, max=4000), validators.DataRequired()])
    price = IntegerField('Price', [validators.number_range(min=1, max=100000, message="An integer between 1 & 100"), validators.DataRequired()])
    ing1 = TextAreaField('Ingredient1', [validators.length(min=1, max=200), validators.DataRequired()])
    ing2 = TextAreaField('Ingredient2', [validators.length(min=1, max=200), validators.DataRequired()])
    ing3 = TextAreaField('Ingredient3', [validators.length(min=1, max=200), validators.DataRequired()])
    ing4 = TextAreaField('Ingredient4', [validators.length(min=1, max=200), validators.DataRequired()])
    ing5 = TextAreaField('Ingredient5', [validators.length(min=1, max=200), validators.DataRequired()])
    food_img = FileField('Food Image')
