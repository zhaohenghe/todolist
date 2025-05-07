#!/bin/bash
docker run -it -v $(pwd)/tasks.json:/app/tasks.json todolist "$@