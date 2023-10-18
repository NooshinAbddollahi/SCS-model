%%  netword of neurons with different parameters for (amplirude and time constant) 
clc
clear all
close all
%%
load('N1.mat')
N1 ;
load('N2.mat')
N2 ;
load('N3.mat')
N3 ;
load('N4.mat')
N4 ;
load('N5.mat')
N5 ;
load('N6.mat')
N6 ;
load('N7.mat')
N7 ;
load('N8.mat')
N8 ;
load('N9.mat')
N9 ;
load('N10.mat')
N10;




j=1  ;
for i=1:length(N1)
    S(1,j)=N1(1,i) ;
    j=j+1 ;
end


for i=1:length(N2)
    S(1,j)=N2(1,i) ;
    j=j+1 ;
end

for i=1:length(N3)
    S(1,j)=N3(1,i) ;
    j=j+1 ;
end

for i=1:length(N4)
    S(1,j)=N4(1,i) ;
    j=j+1 ;
end

for i=1:length(N5)
    S(1,j)=N5(1,i) ;
    j=j+1 ;
end

for i=1:length(N6)
    S(1,j)=N6(1,i) ;
    j=j+1 ;
end

for i=1:length(N7)
    S(1,j)=N7(1,i) ;
    j=j+1 ;
end

for i=1:length(N8)
    S(1,j)=N8(1,i) ;
    j=j+1 ;
end

for i=1:length(N9)
    S(1,j)=N9(1,i) ;
    j=j+1 ;
end

for i=1:length(N10)
    S(1,j)=N10(1,i) ;
    j=j+1 ;
end


size(S)


%%

xx = unique(S)   ;    % temp vector of vals
S = sort(S)    ;     % sorted input aligns with temp (lowest to highest)
p = zeros(size(xx)); % vector for freqs
% frequency for each value
for i = 1:length(xx)
    p(i) = (sum(S == xx(i)))/ (length(S)) ;
end
xx ;
%p ;
%sum(p)
width=0.1 ;
%subplot(2,1,2) ;
figure
bar(xx,p, width )
%xlim([0 150])
xlabel('interspike interval (ms)' , 'FontSize', 10)
ylabel('p(ISI)' , 'FontSize', 10)
%set(gca,'XScale','log');



%%


%xx=xx'
%%

%p=p'








