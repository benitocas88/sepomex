build:
	docker build -t ebe/geomex:latest .

yarn: build
	docker run -it --rm \
	--volume $(CURDIR)/src:/opt/geomex \
	--workdir /opt/geomex/static \
	ebe/geo:latest yarn install

webpack: yarn
	docker run -it --rm \
	--volume $(CURDIR)/src:/opt/geomex \
	--workdir /opt/geomex/static \
	ebe/geo:latest npx webpack --watch --mode=development

up:
	docker-compose up -d --build

geo:
	docker-compose exec geoapp flask geo

stop:
	docker stop $(shell docker ps -aq --filter name='geo*')

rm: stop
	docker rm $(shell docker ps -aq --filter name='geo*')

restart:
	docker-compose restart

restore:
	cat geomex.sql | docker exec -i geomaria mysql -u root --password=secret geomex

upgrade:
	docker-compose exec geoapp flask db upgrade
