# Select_Menu_Combination_System

# init
`pip3 install -r requirements.txt`

# add new component
1. Go to folder /src
2. Add component: `python3 manage.py startapp component_name`
3. add Config in settings.py

# superuser ac
1. superuser ac
```
admin
smcsadmin
```
2. user ac
```
user
smscuser
```

# command
`docker compose down -v`
1. run local
```
docker-compose up -d
```
2. run on railway
```
docker-compose --env-file ../.env.prod up -d
```
Apply migrations: `docker compose exec api python manage.py migrate`
# CI/CD Process
1. Runs tests and linting on push or pull requests to the main branch.
```
Linting: Runs `flake8` to check code style
Testing: Sets up a MySQL service (mysql:9), installs dependencies, and runs python manage.py test.
```
Ensure tests pass locally:`docker compose exec api python manage.py test`
2. Builds and pushes a Docker image to Docker Hub.
```
Build and Push: Builds the Docker image (yoyo200181/smcs:${{ github.sha }}) and pushes to Docker Hub.
```
3. Deploys to a production environment (assumed to be Railway based on .env.prod).