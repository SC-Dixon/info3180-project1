"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.models import Property
from app.forms import PropertyForm

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods = ['GET', 'POST'])
def newproperty():
    """Render website's add new property page."""
    form = PropertyForm()

    if form.validate_on_submit():
        photo = form.photo.data

        photoname=secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photoname))

        nobathrooms = form.number_of_bathrooms.data
        nobedrooms = form.number_of_bedrooms.data
        type = form.type.data
        description = form.description.data
        location = form.location.data
        propertytitle = form.property_title.data
        price = form.price.data
        newproperty = Property(propertytitle,nobedrooms,nobathrooms,location,price,description,type,photoname)
        db.session.add(newproperty)
        db.session.commit()

        flash('The Property was Added Successfully', 'success')
        return redirect(url_for('viewproperties'))
    flash_errors(form)
    return render_template('newproperty.html', form=form)
        


@app.route('/properties')
def viewproperties():
    """Render website's view list of properties page."""
    properties = Property.query.all()
    print(properties)
    return render_template('properties.html', propertieslist = properties)

@app.route('/properties/<propertyid>')
def viewproperty(propertyid):
    """Render website's view details of single property page."""
    property =Property.query.filter(Property.id==propertyid).all()[0]

    return render_template('property.html', property=property)
    
@app.route("/uploads/<filename>")
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
