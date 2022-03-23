// Desarrolado por:
// Francisco Javier Gutierrez G.
// Hexacta 2021

package main

import (
	"fmt"
	"os"
        "os/exec"
	"syscall"
)

func main() {
	// referencia
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Utilizando: %s ip-addr\n", os.Args[0])
		os.Exit(1)
	}

	// Configuracion de ubicacion de comando nikto
	binary, lookErr := exec.LookPath("/usr/bin/nikto")
	if lookErr != nil {
		panic(lookErr)
	}
        
 	// instalación de argumentos
        args := []string{"nikto", "-output=../REPORTS/web_security_report.txt", "-h", os.Args[1]}

	env := os.Environ()

	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
