package main

import (
	"errors"
	"fmt"
	"log"
)

func error1() {
	// Create error and send to Println and log
	err := errors.New("height can't be negative")
	fmt.Println(err.Error())
	log.Fatal(err)
}

func error2() {
	// Если необходимо отформатировать значения
	err := fmt.Errorf("a height of %0.2f is invalid", -2.33333)
	fmt.Println(err.Error())
	fmt.Println(err)
}

func main() {
	error1()
	error2()
}
