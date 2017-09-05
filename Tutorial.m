A = rand(3,3)
A(1:2, 2) = 4
I = A*inv(A)

t = linspace(0,4,1e3)
y1= cos(t/2) .* exp(-t)
y2 = cos(t/2) .* exp(-5*t)

figure
hold on
plot(t, y1)
plot(t, y2)
legend('Slow','Fast')