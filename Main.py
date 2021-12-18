from flask import Flask
from flask_restful import Resource, Api
from GetObjs import getObjs
from Movie import Movie
from Link import Link
from Rating import Rating
from Tag import Tag

app = Flask(__name__)
api = Api(app)


class movies(Resource):
    def get(self):
        return getObjs('movies.csv', Movie)


class links(Resource):
    def get(self):
        return getObjs('links.csv', Link)


class ratings(Resource):
    def get(self):
        return getObjs('ratings.csv', Rating)


class tags(Resource):
    def get(self):
        return getObjs('tags.csv', Tag)


api.add_resource(movies, '/movies/')
api.add_resource(links, '/links/')
api.add_resource(ratings, '/ratings/')
api.add_resource(tags, '/tags/')

if __name__ == '__main__':
    app.run(debug=True)
