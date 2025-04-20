package handlers

import (
	"encoding/json"
	"net/http"
)

type Request struct {
	Text string `json:"text"`
}

type Response struct {
	Sentiment string `json:"sentiment"`
}

func Analyze(w http.ResponseWriter, r *http.Request) {
	var req Request
	_ = json.NewDecoder(r.Body).Decode(&req)

	// Dummy logic
	sentiment := "neutral"
	if req.Text != "" {
		sentiment = "positive"
	}

	resp := Response{Sentiment: sentiment}
	json.NewEncoder(w).Encode(resp)
}
