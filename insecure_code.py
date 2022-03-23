from flask import Flask, request
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    """
    curl http://127.0.0.1:8000/?name=20220101.txt
    """
    name = request.args.get('name', '')
    file = '/src/public/' + name
    with open(file) as f:
        text = f.read()
        return text
  elif request.method == 'POST':
    """
    curl http://127.0.0.1:8000/ -X POST \
      -H "Content-Type: application/json" \
      --data '{"name": "20220101.txt", "message": "メッセージ\n"}'
    """
    name = request.json['name']
    message = request.json['message']

    file = '/src/public/' + name
    with open(file, 'w') as f:
      f.write(message)

    return 'save\n'

app.run(port=8000, host='0.0.0.0', debug=True)
