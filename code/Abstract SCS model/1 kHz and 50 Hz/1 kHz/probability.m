%%  netword of neurons with different parameters for (amplirude and time constant) 
clc
clear all
close all
%%
load('N11k.mat')

load('N21k.mat')

load('N31k.mat')

load('N41k.mat')

load('N51k.mat')

load('N61k.mat')

load('N71k.mat')

load('N81k.mat')

load('N91k.mat')

load('N101k.mat')





j=1  ;
for i=1:length(N11k)
    S(1,j)=N11k(1,i) ;
    j=j+1 ;
end


for i=1:length(N21k)
    S(1,j)=N21k(1,i) ;
    j=j+1 ;
end

for i=1:length(N31k)
    S(1,j)=N31k(1,i) ;
    j=j+1 ;
end

for i=1:length(N41k)
    S(1,j)=N41k(1,i) ;
    j=j+1 ;
end

for i=1:length(N51k)
    S(1,j)=N51k(1,i) ;
    j=j+1 ;
end

for i=1:length(N61k)
    S(1,j)=N61k(1,i) ;
    j=j+1 ;
end

for i=1:length(N71k)
    S(1,j)=N71k(1,i) ;
    j=j+1 ;
end

for i=1:length(N81k)
    S(1,j)=N81k(1,i) ;
    j=j+1 ;
end

for i=1:length(N91k)
    S(1,j)=N91k(1,i) ;
    j=j+1 ;
end

for i=1:length(N101k)
    S(1,j)=N101k(1,i) ;
    j=j+1 ;
end





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
width=0.2 ;
%subplot(2,1,2) ;
figure
bar(xx,p )
%xlim([0 150])
xlabel('interspike interval (ms)' , 'FontSize', 10)
ylabel('p(ISI)' , 'FontSize', 10)
%set(gca,'XScale','log');





%%
xx=xx' ;
p=p' ;












