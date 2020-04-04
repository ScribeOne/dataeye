# DataEye

Backend for IoT-data-collection

### Get going

It's recommended to use a virtualenv. Name it `venv` like in the .gitignore to prevent files from getting into the repository.

Install required python packages:
 `pip install -r requirements.txt`

Create database tables:
`./manage.py migrate` 

Run the server:
 `./manage.py runserver 0.0.0.0:8000`

### Start a postgres docker
```
docker run -p 5432:5432 \
                   -e 'POSTGRES_USER=Testuser' \
                   -e 'POSTGRES_PASSWORD=testpassword' \
                   -e 'POSTGRES_DB=mydockerdb' \
                   -v dataeye_postgres-data:/var/lib/postgresql/data \
                   --network=mynetwork \
                   -d postgres:12
```

### Run backend with docker

Run backend-server and postgres database:
 `docker-compose up -d --build`
 
