# Effective Mobile Web Application

Простое веб-приложение с Nginx в качестве reverse proxy, запущенное в Docker-контейнерах.

## Архитектура

Client -> Nginx:80 -> Backend:8080
(reverse proxy)


- **Nginx**: Принимает запросы на порту 80 и проксирует их на бэкенд
- **Backend**: Python HTTP-сервер, слушает порт 8080, доступен только внутри Docker-сети

## Технологии

- Docker & Docker Compose
- Nginx (Alpine Linux)
- Python 3.11 (Alpine Linux)
- HTTP Server из стандартной библиотеки Python

## Запуск проекта

### Предварительные требования

- Docker (>= 20.10.0)
- Docker Compose (>= 2.0.0)

### Инструкция по запуску

1. Клонируйте репозиторий:
```bash
git clone <your-repo-url>
cd effective-mobile-app
```
2. Запустите приложение
```bash
docker-compose up -d
```
3. Проверьте статус контейнеров:
```bash
docker-compose ps
```
