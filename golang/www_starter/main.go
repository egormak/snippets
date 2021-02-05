package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type User struct {
	Name       string
	Age        uint16
	Money      int16
	Avg_grades float64
	Happiness  float64
	Hobbies    []string
}

func (u User) getAllInfo() string {
	return fmt.Sprintf("User name is: %s. He is %d and he has money equal: %d", u.Name, u.Age, u.Money)
}

func (u *User) setNewName(newName string) {
	u.Name = newName
}

func homePage(w http.ResponseWriter, r *http.Request) {
	bob := User{"Bob", 25, -50, 4.2, 0.8, []string{"Football", "Skate"}}
	// fmt.Fprintf(w, `<h1> Main text </h1>`)
	tmpl, _ := template.ParseFiles("templates/home_page.html")
	tmpl.Execute(w, bob)
}

func contactsPage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello Contacts")
}

func handleRequest() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/contacts/", contactsPage)
	http.ListenAndServe(":8080", nil)
}

func main() {
	fmt.Println("Hello World")
	handleRequest()
}
