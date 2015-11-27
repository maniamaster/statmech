reset
set term pdf
set output 't0.pdf'
set xlabel 'q'
set ylabel 'p'
set xrange [-2:2]
set yrange [-2:2]
set size ratio -1

p 't=0.dat' t 't=0, N=2000' with points pt 7 ps 0.1
set output 't10.pdf'
p 't=10.dat' t 't=10, N=2000' with points pt 7 ps 0.1
set output 't50.pdf'
p 't=50.dat' t 't=50, N=2000' with points pt 7 ps 0.1
set output 't250.pdf'
p 't=250.dat' t 't=250, N=2000' with points pt 7 ps 0.1 
set output 't500.pdf'
p 't=500.dat' t 't=500, N=2000' with points pt 7 ps 0.1
set output 't1000.pdf'
p 't=1000.dat' t 't=1000, N=2000' with points pt 7 ps 0.1

set output
