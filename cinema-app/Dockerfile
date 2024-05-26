FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY cinema-app/ /service/cinema-app/
WORKDIR /service/cinema-app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/cinema_library.proto

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/users.proto

EXPOSE 5000
ENV FLASK_APP=main.py
ENTRYPOINT [ "flask", "run", "--host=127.0.0.1"]