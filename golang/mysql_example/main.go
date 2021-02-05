package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

type User struct {
	Name string `json:"name"`
	Age  uint16 `json:"age"`
}

func main() {
	db, err := sql.Open("mysql", "root:toor@tcp(127.0.0.1:3306)/golang")
	fmt.Println(err)
	if err != nil {
		panic(err)
	}

	// Check connection
	err = db.Ping()
	if err != nil {
		panic(err)
	}

	defer db.Close()

	// // Insert Data
	// insert, err := db.Query("INSERT INTO `users` (`name`, `age`) VALUES('Alex', 25)")
	// if err != nil {
	// 	panic(err)
	// }
	// defer insert.Close()

	// Select Data
	res, err := db.Query("SELECT `name`, `age` from `users`")

	if err != nil {
		panic(err)
	}

	for res.Next() {
		var user User
		err = res.Scan(&user.Name, &user.Age)
		if err != nil {
			panic(err)
		}
		fmt.Printf("User: %s with age: %d \n", user.Name, user.Age)
	}

	fmt.Println("Connect to DB")
}
