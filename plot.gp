filename="data.dat"
set xlabel "Contenders (N)"
set ylabel "Mbps"
set term postscript enhanced color dashed
set out "figure.eps"
plot filename using 1:2 title "Average Throughput" with lines linestyle 1 linewidth 1, \
"" using 1:2:3 notitle with yerrorbars linestyle 1 linewidth 1
