#!/bin/bash


ghz --insecure \
-n 3 -c 1 -t 0 \
--connections=1 \
--stream-call-count=3 \
--call hello.Greeter.SayHello \
-D ./data.json \
--debug=./debug/debug1.log \
localhost:50051


# ghz --insecure \
# -n 3 -c 1 -t 0 \
# --connections=1 \
# --stream-call-count=3 \
# --call hello.Greeter.SayHello \
# -d '[{"name":"Joe"},{"name":"Kate"},{"name":"Sara"}]' \
# --debug=./debug/debug1.log \
# localhost:50051