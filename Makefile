shell:
	docker exec -it $(shell docker ps --filter=name=$(NAME) -q) sh

NAME=flask-restful