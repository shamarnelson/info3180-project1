"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for,flash, send_from_directory
from werkzeug.utils import secure_filename
from .forms import CreateProperty


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


@app.route('/property', methods=['POST'])
def property():
    createproperty = CreateProperty()
    if request.method == "POST":
        if createproperty.validate_on_submit():
            try:
                file = request.files['photo']
                filename = secure_filename(file.filename)
                filename = reduce_filename(filename)
                property = Property(request.form['title'], request.form['description'], request.form['numofbeds'], request.form['numofbaths'], request.form['price'], request.form['type'], request.form['location'], filename)
                db.session.add(property)
                db.session.commit()
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('Sucessfully Added Property', 'success')
                return redirect(url_for('properties'))
            except:
                flash('Error Adding Property', 'danger')
                return redirect(url_for('home')) 
        flash_errors(createproperty)
    return render_template('property.html', form=createproperty)

@app.route("/property/<propertyid>")
def get_property(propertyid):
    property = db.session.query(Property).get(propertyid)
    return render_template('sproperty.html', place=property)

@app.route('/properties')
def properties():
    items = db.session.query(Property).all()
    return render_template('properties.html', items=items)

@app.route('/uploads/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

def reduce_filename(filename):
    extension = filename[-4:]
    main =  filename[:-4]
    if len(main) > 255:
        main = main[:250]
    return main + extension
   

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
