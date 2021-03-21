"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for,flash, send_from_directory
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from .models import UserProperty
import os


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
    return render_template('about.html', name="Real Estate")


@app.route('/property', methods=['GET', 'POST'])
def property():
    """ displays form for new property"""
    form = PropertyForm
    
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data 
        numofbeds = form.numofbeds.data
        numofbaths = form.numbaths.data
        description = form.description.data
        propertyType = form.propertyType.data
        photo = form.photo.data
        price = form.price.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        userproperty= UserProperty(title,description,numofbaths,numofbeds,propertyType,price,filename)
        db.session.add(userproperty)
        db.session.commit()
        flash(' Form Submitted!', category= "sucesss")
        return redirect(url_for('property'))
    return render_template('property.html', form=form)  

def get_uploaded_images():
    rootdir=os.getcwd()
    lst=[]
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
          lst.append(file)
    lst.pop(0)
    return lst

@app.route('/upload/<filename>')
def get_image(filename):
    root_dir=os.getcwd()
    return send_from_directory(os.path.join(root_dir,app.config['UPLOAD_FOLDER']),filename)


@app.route("/properties")
def properties():
    users= db.session.query(UserProperty).all()
    return render_template("properties.html", property= users )
   

@app.route('/property/<propertyid>')
def user_pro(propertyid):
    userprop= UserProperty.query.filter_by(id=propertyid).first()
    return render_template("userproperty.html", userpro= UserProperty)


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


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
