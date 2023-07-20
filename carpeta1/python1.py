# Alias para el comando 'ls'
alias mialias1='ls'

# Función 'supergit' para simplificar comandos de Git
supergit() {
    if [[ $1 == "update" ]]; then
        if [[ -z $2 ]]; then
            echo "Por favor, proporciona un mensaje de commit."
        else
            echo "---------running git status"
            git status
            echo "---------running git add"
            git add .
            echo "---------running git commit -m \"$2\""
            git commit -m "$2"
            echo "---------running git push"
            git push
        fi
    elif [[ $1 == "server2" ]]; then
        echo "nothing here :)"
    else
        echo "Uso: supergit update 'mensaje del commit'"
    fi
}
