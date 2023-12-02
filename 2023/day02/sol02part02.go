package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	lines := getInputLines()
	gamePowerSum := 0
	for _, line := range lines {
		gameInfo := strings.Split(line, ": ")[1]
		maxCountMap := map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}
		gamePower := 1
		for _, set := range strings.Split(gameInfo, "; ") {
			for _, reveal := range strings.Split(set, ", ") {
				countAndColor := strings.Split(reveal, " ")
				color := countAndColor[1]
				count, _ := strconv.Atoi(countAndColor[0])
				if maxCountMap[color] < count {
					maxCountMap[color] = count
				}
			}
		}
		for _, value := range maxCountMap {
			gamePower *= value
		}
		gamePowerSum += gamePower
	}

	fmt.Println(gamePowerSum)
}

func getInputLines() []string {
	file, _ := os.ReadFile("2023/day02/input.txt")
	return strings.Split(string(file), "\n")
}
