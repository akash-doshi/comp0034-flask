from flask import Flask, render_template, flash, redirect, url_for
from app.main.forms import signupForm
from app import create_app

app = create_app()
app.app_context().push()
app.run(debug=True)

