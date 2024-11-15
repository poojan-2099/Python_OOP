from flask import Flask, abort
from flask_restful import Api, Resource, reqparse

app=Flask(__name__)
api=Api(app)

video_put_args=reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="likes of the video")

# names={"a":{"age":12, "gender":"male"},
#        "b":{"age":15, "gender":"female"}}

# class HelloWord(Resource):
#     def get(self, name):
#         return names[name]

videos={}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="Video Id is not exist")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201

api.add_resource(Video, "/video/<int:video_id>")

if __name__=="__main__":
    app.run(debug=True)