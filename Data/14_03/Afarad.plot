set locale
set decimalsign
set terminal pngcairo enhanced font 'Times Roman,10'
set output "test.png"
set title "Apparition des instabilités de Faraday en fonction de la fréquence"
plot "ffa.txt" u 1:2:3 with yerrorbars title "valeurs expérimentales" font 'Times Roman,5'

