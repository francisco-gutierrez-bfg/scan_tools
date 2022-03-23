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
	if len(os.Args) != 3 {
		fmt.Fprintf(os.Stderr, "Utilizando ip: %s\n", os.Args[1])
		os.Exit(1)
	}

	// Configuracion de ubicacion de comando HYDRA
	binary, lookErr := exec.LookPath("/usr/bin/hydra")
	if lookErr != nil {
		panic(lookErr)
	}

	// instalación de argumentos
	args := []string{"hydra", "-L", "diccionarios/wordlists/users.lst", "-P", "diccionarios/wordlists/passwords.lst", os.Args[1], os.Args[2]}

	env := os.Environ()

	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}

