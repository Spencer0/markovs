package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("$ Welcome! Press Enter To Finish Your Sentence\n")
	for {
		fmt.Print("$ ")
		cmdString, err := reader.ReadString('\n')
		fmt.Println("Input : " , cmdString)
		if err != nil {
			fmt.Println(" err ", err)
		}
	}
}