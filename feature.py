from flask import Flask
FAI=Flask(__name__)


@FAI.route('/StringResponse')
def StringResponse():
    return '<center><h1>Hai!!...This is the first Response of flask'

@FAI.route('/SecondStringResponse')
def SecondStringResponse():
    return '<center><h1>Hello!!....This is the Second Response of flask'

if __name__ == '__main__':
    FAI.run(debug=True)