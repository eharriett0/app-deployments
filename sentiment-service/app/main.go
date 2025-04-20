package main

import (
	"log"
	"net/http"

	"github.com/eharriett0/app-deployments/sentiment-service/handlers"
)

func healthz(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("ok"))
}

func main() {
	http.HandleFunc("/analyze", handlers.Analyze)
	http.HandleFunc("/healthz", healthz)

	log.Println("Starting server on :8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
