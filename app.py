from flask import Flask, render_template, request, redirect, url_for, flash
import func
import db

app = Flask(__name__)
app.secret_key = "contactbook123"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET','POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        func.add_contact_to_db(name, phone, email, address)
        flash("✅ Contact added successfully!", "success")
        return redirect(url_for('add_contact'))

    return render_template("add.html")

@app.route('/view')
def view_contacts():
    rows = func.get_all_contacts()
    return render_template("view.html", rows=rows)

@app.route('/delete/<int:id>')
def delete_contact(id):
    func.delete_contact_from_db(id)
    flash("🗑️ Contact deleted successfully!", "danger")
    return redirect(url_for('view_contacts'))

@app.route('/update/<int:id>', methods=['GET','POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        func.update_contact_in_db(id, name, phone, email, address)
        flash("✏️ Contact updated successfully!", "info")
        return redirect(url_for('view_contacts'))

    contact = func.get_contact_by_id(id)
    return render_template("add.html", contact=contact)

if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
