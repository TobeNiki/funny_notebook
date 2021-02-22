package bfCodeCreate

import (
	"strings"
)

// GenerateBf bfCode default parameter
type GenerateBf struct {
	array  []int
	MAX    int
	list   []int
	m      int
	flag   []int
	bfCode string
}

func maxDecision(self *GenerateBf) {
	self.MAX = 0
	for _, item := range self.array {
		if self.MAX < item {
			self.MAX = item
		}
	}
}

func decisiveDecision(self *GenerateBf) {
	var r int
	var sumValue int
	var r1, r2 int
	for index := 0; index < self.MAX; index++ {
		if index == 0 {
			continue
		}
		sumValue = index
		for _, ai := range self.array {
			r1 = ai / index
			r2 = (ai + index) / index

			if ai-r1*index > r2*index-ai {
				r = r2*index - ai
				sumValue = sumValue + r2
			} else {
				r = ai - r1*index
				sumValue = sumValue + r1
			}

			sumValue = sumValue + r
			self.list = append(self.list, sumValue)
		}
	}
}

func mDecision(self *GenerateBf) {
	self.m = 10000000000
	var li int
	for index := 0; index < len(self.list); index++ {
		li = self.list[index]
		if self.m > li {
			self.m = li
			//std := i
		}
	}
}

func plusWrite(self *GenerateBf) {
	for index := 0; index < self.m; index++ {
		self.bfCode = self.bfCode + "+"
	}
}

func forWrite(self *GenerateBf) {
	self.bfCode = self.bfCode + "["
	for _, item := range self.array {
		r1 := item / self.m
		r2 := (item + self.m) / self.m
		self.bfCode = self.bfCode + ">"

		if item-r1*self.m > r2*self.m-item {
			self.flag = append(self.flag, -(r2*self.m - item))
			for index := 0; index < r2; index++ {
				self.bfCode = self.bfCode + "+"
			}
		} else {
			self.flag = append(self.flag, item-r1*self.m)
			for index := 0; index < r1; index++ {
				self.bfCode = self.bfCode + "+"
			}
		}
	}
}

func rePointer2LoopCounter(self *GenerateBf) {
	for index := 0; index < len(self.array); index++ {
		self.bfCode = self.bfCode + "<"
	}
	self.bfCode = self.bfCode + "-"
	self.bfCode = self.bfCode + "]"
}

func roundUp(self *GenerateBf) {
	for index := 0; index < len(self.array); index++ {
		self.bfCode = self.bfCode + ">"
		if self.flag[index] < 0 {
			for j := 0; j < -self.flag[index]; j++ {
				self.bfCode = self.bfCode + "-"
			}
		} else {
			for j := 0; j < self.flag[index]; j++ {
				self.bfCode = self.bfCode + "+"
			}
		}
		self.bfCode = self.bfCode + "."
	}
}

func newLine(self *GenerateBf) {
	self.bfCode = self.bfCode + ">++++++++++++."
}

// Execution parameter ASCII text return brainfu()k code
func Execution(text string) string {
	var self GenerateBf
	charSlice := strings.Split(text, "")
	for _, char := range charSlice {
		self.array = append(self.array, int(char[0]))
	}
	if len(self.array) != 0 {
		maxDecision(&self)
		decisiveDecision(&self)
		mDecision(&self)
		plusWrite(&self)
		forWrite(&self)
		rePointer2LoopCounter(&self)
		roundUp(&self)
		newLine(&self)
	}
	return self.bfCode
}
