build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down --remove-orphans

clean:
	docker compose down -v --remove-orphans

exec:
	docker compose exec regvd /bin/bash

e:
	$(MAKE) exec
