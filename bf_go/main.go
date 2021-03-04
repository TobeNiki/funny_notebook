package main

import (
	"fmt"
	"net/http"
	"path"
	"strconv"
	"strings"
)

var port = 5000

type RootHandler struct{}

func (h *RootHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	var head string
	head, r.URL.Path = ShiftPath(r.URL.Path)
	if head == "" && r.Method == "GET" {
		Index(w)
	}
}

func Index(w http.ResponseWriter) {
	w.Write([]byte("root handler"))
}
func ShiftPath(p string) (head, tail string) {
	p = path.Clean("/" + p)
	i := strings.Index(p[1:], "/") + 1
	if i <= 0 {
		return p[1:], "/"
	}
	return p[1:i], p[i:]
}

type UserHandler struct{}

func (h *UserHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	var head string
	head, r.URL.Path = ShiftPath(r.URL.Path)

	// この時に /users/:id のようなpathは head => users、 後続の処理で使うリクエストpath = /1 となっている。
	//users/usersで起動
	if head == "users" && r.Method == "GET" {
		GetUsers(w)
		return
	}

	// もう一度ShftPathを行う。ここでは head => 1というint64の数字のはずである。
	head, r.URL.Path = ShiftPath(r.URL.Path)
	id, err := strconv.ParseInt(head, 10, 64)
	if err != nil {
		http.Error(w, fmt.Sprintf("invalid params. head: %s", head), http.StatusBadRequest)
		return
	}

	switch r.Method {
	case "GET":
		GetUser(w, id)
		return
	}
}
func GetUsers(w http.ResponseWriter) {
	w.Write([]byte("get users"))
}

func GetUser(w http.ResponseWriter, id int64) {
	w.Write([]byte(fmt.Sprintf("get user. id: %d", id)))
}

func RequestLog(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Printf("[%s] %s\n", r.Method, r.URL.Path)
		next.ServeHTTP(w, r)
	})
}

type AppHandler struct {
	RootHandler RootHandler
	UserHandler UserHandler
}

func (h *AppHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	var head string
	head, r.URL.Path = ShiftPath(r.URL.Path)

	switch head {
	case "":
		h.RootHandler.ServeHTTP(w, r)
		return
	case "users":
		h.UserHandler.ServeHTTP(w, r)
		return
	default:
		http.Error(w, fmt.Sprintf("method not allowed request. req: %v", r.URL), http.StatusMethodNotAllowed)
		return
	}

	http.Error(w, "Not Found", http.StatusNotFound)
}

func main() {
	fmt.Println("Server Start....")
	h := &AppHandler{
		UserHandler: UserHandler{},
	}

	router := RequestLog(h)
	if err := http.ListenAndServe(fmt.Sprintf(":%d", port), router); err != nil {
		panic(err)
	}
}
