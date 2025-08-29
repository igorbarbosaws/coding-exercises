function main() {
    var num1, num2, num3, media;

    window.alert("Digite um número:  ");
    num1 = Number(window.prompt('Enter a value for num1'));
    window.alert("Digite outro número:  ");
    num2 = Number(window.prompt('Enter a value for num2'));
    window.alert("Digite o ultimo número:  ");
    num3 = Number(window.prompt('Enter a value for num3'));
    media = num1 + num2 + num3 / 3;
    window.alert("A média é:  " + media);
}
