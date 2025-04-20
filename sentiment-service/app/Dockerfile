# sentiment-service/app/Dockerfile
FROM golang:1.24.2-alpine as builder

WORKDIR /app
COPY . .
RUN go build -o sentiment-service .

# final image
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/sentiment-service .
EXPOSE 8080
CMD ["./sentiment-service"]