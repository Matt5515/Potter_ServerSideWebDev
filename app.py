from flask import Flask, render_template
from flask.views import MethodView

app = Flask(__name__)

class Test(MethodView):

    def get(self):
        return 'Returned a test!!'
    
    def post(self):
        return 'Created a test!!'

    def put(self):
        return 'Modified a test!!'

    def delete(self):
        return 'Deleted a test!!'


app.add_url_rule('/testing', view_func=Test.as_view('testing'))


# if __name__ == "__main__":
#     app.run(debug=True)