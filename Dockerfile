# Stage build
FROM python:3.12-alpine AS build
WORKDIR /app
RUN apk add --no-cache build-base libffi-dev openssl-dev
COPY app/requirements.txt .
RUN mkdir -p /install && pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage final
FROM python:3.12-alpine
WORKDIR /app
RUN apk add --no-cache libstdc++ libgcc
COPY --from=build /install /usr/local
COPY app/ .
EXPOSE 5000
CMD ["python", "main.py"]
