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
	// go run goNmapScan.go IP
	// referencia
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Utilizando: %s ip-addr\n", os.Args[0])
		os.Exit(1)
	}

	// Configuracion de ubicacion de comando NMAP
	binary, lookErr := exec.LookPath("/usr/bin/nmap")
	if lookErr != nil {
		panic(lookErr)
	}

	// instalación de argumentos
	//args := []string{"nmap", "-v", "-A", os.Args[1]}
	args := []string{"nmap", "-sV", "--script=vulscan/vulscan.nse", os.Args[1]}

	env := os.Environ()

	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
