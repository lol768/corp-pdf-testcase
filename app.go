package main

import (
	"net/http"
)

func main() {
	addCorp := func(h http.Handler) http.HandlerFunc {
		return func(w http.ResponseWriter, r *http.Request) {
			w.Header().Add("Cross-Origin-Resource-Policy", "same-origin")
			h.ServeHTTP(w, r)
		}
	}

	http.Handle("/", addCorp(http.FileServer(http.Dir("static"))))
	http.ListenAndServe(":8080", nil)
}
