from flask import render_template


def return_to_index(form):
    return render_template('index.html', form=form)