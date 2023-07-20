alias mialias1='ls'

supergit() {
    if[[ $1 == "update" ]]; then
        if[[ -z $2 ]]; then
            echo "Por favor, proporcionr un mensaje de comit."
        else
            echo "---------running git status"
            git status
            echo "---------running git add"
            git add
            echo "---------running git commit -m $2"
            git commit -m "$2"
            echo "---------running git push"
            git push
        fi
    elif [[ $1 == "server2" ]]; then
        echo "nothing here :)"
    else
        echo "update: status, add ., commit, push"
    fi
}