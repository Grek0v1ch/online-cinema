FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY users/ /service/users/
WORKDIR /service/users
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/cinema_library.proto

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/users.proto

EXPOSE 50052
ENTRYPOINT [ "python", "main.py" ]