package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var constraints = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

func main() {
	lines := getInputLines()
	gameIdSum := 0
	for _, line := range lines {
		gameIdAndInfo := strings.Split(line, ": ")
		gameId, _ := strconv.Atoi(strings.Split(gameIdAndInfo[0], " ")[1])
		if isGameEligible(gameIdAndInfo[1]) {
			gameIdSum += gameId
		}
	}

	fmt.Println(gameIdSum)
}

func isGameEligible(s string) bool {
	for _, set := range strings.Split(s, "; ") {
		for _, reveal := range strings.Split(set, ", ") {
			countAndColor := strings.Split(reveal, " ")
			count, _ := strconv.Atoi(countAndColor[0])
			if constraints[countAndColor[1]] < count {
				return false
			}
		}
	}
	return true
}

func getInputLines() []string {
	file, _ := os.ReadFile("2023/day02/input.txt")
	return strings.Split(string(file), "\n")
}
