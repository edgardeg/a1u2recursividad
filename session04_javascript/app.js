alert("Funciones recursivas")

function factorial(n) {
    // instrucciones de la recursividad

    if (n === 0) {
        return 1;
    }

    return n * factorial(n-1);

}

alert(factorial(5))