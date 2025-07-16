from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

items = [
    {'id': 1, 'name': 'Apple'},
    {'id': 2, 'name': 'Banana'},
    {'id': 3, 'name': 'Cherry'}
]

def get_item(item_id):
    return next((item for item in items if item['id'] == item_id), None)

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update(item_id):
    item = get_item(item_id)
    if not item:
        return "Item not found", 404
    if request.method == 'POST':
        item['name'] = request.form['name']
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)