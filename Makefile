IMAGE_NAME = myapp
CONTAINER_NAME = myapp-container

build:
	docker build -t $(IMAGE_NAME) .

typing: build
	docker run --rm -v $(PWD):/app $(IMAGE_NAME) uv run mypy .

run:
	docker run -it --rm -v $(PWD):/app --name $(CONTAINER_NAME) $(IMAGE_NAME) bash

clean:
	docker rmi $(IMAGE_NAME)

.PHONY: build typing run clean