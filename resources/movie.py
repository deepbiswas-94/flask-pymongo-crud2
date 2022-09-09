from flask import Response, request,jsonify
from database.models import Movie
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

class MoviesApi(Resource):
  """Movie List APIs"""
  @jwt_required()
  def get(self):
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200    

class MovieApi(Resource):
  """Movie Single APIs"""
  def put(self, id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    movie = Movie.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)