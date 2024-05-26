from concurrent import futures
import json

import grpc

from users_pb2 import (
    Status,
    ExistResponse,
    MarksResponse,
    RatingResponse,
    Nill
)

import users_pb2_grpc


class UsersService(users_pb2_grpc.UsersServicer):

    def UserExist(self, request, context):
        for user in USERS:
            if user['username'] == request.username:
                if user['password'] == request.password:
                    return ExistResponse(status=Status.EXIST)
                return ExistResponse(status=Status.INCORRECT_PASSWORD)
        return ExistResponse(status=Status.NOT_EXIST)
    
    def UserMarks(self, request, context):
        for user in USERS:
            if user['username'] == request.username:
                return MarksResponse(marks=user['marks'])
        return MarksResponse(marks=[])

    def FilmRating(self, request, context):
        rating = 0.0
        cnt = 0
        for user in USERS:
            for mark in user['marks']:
                if mark['film_id'] == request.film_id:
                    cnt += 1
                    rating += mark['mark']
        if cnt == 0:
            return RatingResponse(rating=-1.0)
        return RatingResponse(rating=rating/cnt)
    
    def UserMarksUpdate(self, request, context):
        with open('data/users.json', 'w', encoding='utf-8') as file:
            for user in USERS:
                if user['username'] == request.username:
                    for mark in user['marks']:
                        if mark['film_id'] == request.film_id:
                            mark['mark'] = request.mark
                            json.dump(USERS, file, indent=2)
                            return Nill()
                    user['marks'].append({'film_id': request.film_id, 'mark': request.mark})
                    json.dump(USERS, file, indent=2)
                    return Nill()
            json.dump(USERS, file, indent=2)
            return Nill()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(UsersService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    with open("data/users.json", 'r', encoding='utf-8') as file:
        USERS = json.load(file)
    serve()
