FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY cinema-library/ /service/cinema-library/
WORKDIR /service/cinema-library
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/cinema_library.proto

EXPOSE 50051
ENTRYPOINT [ "python", "main.py" ]