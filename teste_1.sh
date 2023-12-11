#! /bin/bash
seq 1 4000 | xargs -n1 -I -P200 curl --location 'localhost:9999/client' \
--header 'Content-Type: application/json' \
--data '{
      "id": "d41d8cd98f00b204e9800998ecf8427e",
        "name": "Nome do cliente",
        "email": "email@email.com",
        "celphone": "11999999999",
        "status": true,
        "hash":"3adgacc51d95682f1c85f94223335be0adcb99963a2d18906294b5901f10c446"
}'