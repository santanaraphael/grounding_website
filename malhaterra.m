in = xlsread('terraio.xlsx',1,'B2:B11');
% Entradas %
icc = in(1);
te = in(2);
h = in(3);
A = in(4);
B = in(5);
area = A*B;
roa = in(6);
hs = in(7);
ros = in(8);
tetam = in(9);
tetaa = in(10);

% Valores máximos para passo e toque %
ich = 0.116/sqrt(te);
vtoque0 = (1000+1.5*roa)*ich;
vpasso0 = (1000+6*roa)*ich;

% Fator de correção da brita %
cs = 1 - (0.09*(1-(roa/ros))/(2*hs+0.09));

% Valores máximos levando em consideração a brita %

vtoque = (1000+1.5*cs*roa)*ich;
vpasso = (1000+6*cs*roa)*ich;
xlswrite('terraio.xlsx',vtoque,1,'F2')
xlswrite('terraio.xlsx',vpasso,1,'H2')
% Dimensionamento do Condutor da Malha de Terra %

s = icc/(226.53*sqrt((1/te)*log(((tetam-tetaa)/(234+tetaa))+1)));
d0 = 2*sqrt(s/pi);
d = d0/1000;

% Layout da malha %

g = gcd (A,B);

for i = 1:500
    ea = g/i;
    na =(A/ea)+1;
    nb =(B/ea)+1;
    ltotal = A*nb + B*na;
    rmalha = roa*((1/ltotal)+(1/sqrt(20*area))*(1+(1/(1+h*sqrt(20/area))))); % Fórmula de Sverak 
    n = sqrt(na*nb); % não tenho certeza se devemos arredondar, se precisar, usar ceil
    kii = 1/((2*n)^(2/n));
    kh = sqrt(1+h);
    ki = 0.656 + 0.172*n;
    km = (1/(2*pi))*(log(((ea^2)/(16*h*d))+(((ea+2*h)^2)/(8*ea*d))-(h/(4*d)))+(kii/kh)*log(8/(pi*(2*n-1))));
    vmalha = (roa*km*ki*icc)/ltotal;
    nmax = max(na,nb);
    kp = 1/(pi*((1/(2*h))+(1/(ea+h))+(1/ea)*(1-0.5^(nmax-2))));
    vpsm = (roa*kp*ki*icc)/ltotal;
    inlog0 = 1;
    inlog1 = 1;
    for j=1:nmax
        inlog0 = inlog0*(((j+1)*ea+0)/2*ea);
    end
    kc0 = (1/(2*pi))*(log((h^2+0^2)+((h^2+(ea+0)^2))/(h*d*(h^2+ea^2)))+2*log(inlog0));
    
    for j=1:nmax
        inlog1 = inlog1*(((j+1)*ea+1)/2*ea);
    end
    kc1 = (1/(2*pi))*(log((h^2+1^2)+((h^2+(ea+1)^2))/(h*d*(h^2+ea^2)))+2*log(inlog1));
    
    kc = kc1- kc0;
    vcerca = (roa*kc*ki*icc)/ltotal;
    
    %% Adicionar na planilha resultados %%
    contador = i+14;
    alfa = num2str(contador);
    cell = strcat('A',alfa);
    celltoque = strcat('B',alfa);
    cellpasso = strcat('C',alfa);
    cellcerca = strcat('D',alfa);
    cellrmalha = strcat('E',alfa);
    cellea = strcat('F',alfa);
    xlswrite('terraio.xlsx',i,1,cell)
    xlswrite('terraio.xlsx',vmalha,1,celltoque)
    xlswrite('terraio.xlsx',vpsm,1,cellpasso)
    xlswrite('terraio.xlsx',vcerca,1,cellcerca)
    xlswrite('terraio.xlsx',rmalha,1,cellrmalha)
    xlswrite('terraio.xlsx',ea,1,cellea)

    
    %if (vcerca<=vtoque) && (vmalha<=vtoque) && (vpsm<=vpasso) && (rmalha<=5)
     %   break
    %end
      
       
    
    
end



%{
for i = 1:10000
    teste = G/i;
    teste2 = num2str(i)
    cell = strcat('F',teste2)
    if i == 23
        break
    end
    
    xlswrite('terraio.xlsx',i,1,cell)
end
%}
