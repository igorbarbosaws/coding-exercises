function main() {
    var n1, n2, n3, soma;

    window.alert("Escreva um número:  ");
    n1 = Number(window.prompt('Enter a value for n1'));
    window.alert("Escreva outro número: ");
    n2 = Number(window.prompt('Enter a value for n2'));
    window.alert("Escreva o último número:  ");
    n3 = Number(window.prompt('Enter a value for n3'));
    soma = n1 + n2 + n3;
    window.alert("A soma é:  " + soma);
}
