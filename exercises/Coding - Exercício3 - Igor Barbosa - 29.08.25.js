function main() {
    var n1, n2, n3, media;

    window.alert("Qual a sua nota na primeira avaliação? ");
    n1 = Number(window.prompt('Enter a value for n1'));
    window.alert("Qual a sua nota na segunda avaliação: ");
    n2 = Number(window.prompt('Enter a value for n2'));
    window.alert("Qual a sua nota no seminário? ");
    n3 = Number(window.prompt('Enter a value for n3'));
    media = n1 + n2 + n3 / 3;
    window.alert("A sua média é: " + media);
    if (media >= 7) {
        window.alert("Aprovado, muito bem! ");
    } else {
        window.alert("Reprovado, se esforce um pouco mais ... ");
    }
}
