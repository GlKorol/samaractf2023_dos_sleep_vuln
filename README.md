# DOS via sleep

Пример уязвимого к DOS веб приложения через фукнцию `time.sleep`. 

Для удобства чекер и эксплоит вынесены в отдельные папки, и также написаны скрипты, которые уже реализуют циклы..  

Для эксплуатации (filename url): `./exploit/exploit.sh http://host:port/await?timeout=10`

Для чекера (filename url timeout): `./checker/checker.sh http://host:port/ 1`

Синхронный код (vuln)
```shell
docker build -t web_dos . 
docker run -p 8000:8000 --name 'web_dos' --rm  -d web1_dos
```

Асинхронный код (protected)
```shell
cd async_version
docker build -f DockerfileAsync -t web_dos_async . 
docker run -p 8001:8001 --name 'web_dos_async' --rm  -d web_dos_async
```

