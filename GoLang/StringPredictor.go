package stringpredictor

import (  
    "fmt"
)

type stringpredictor struct {  
    corpus      [6]string
    lastName    string
    totalLeaves int
	leavesTaken int
}

func New(lastName string, totalLeave int, leavesTaken int) stringpredictor {  
	corpus := [6]string{"a", "corp"}
    sp := stringpredictor {corpus, lastName, totalLeave, leavesTaken}
    return sp
}

func (sp stringpredictor) LeavesRemaining() {  
    fmt.Printf("%s %s has %d leaves remaining", sp.lastName, (sp.totalLeaves - sp.leavesTaken))
}