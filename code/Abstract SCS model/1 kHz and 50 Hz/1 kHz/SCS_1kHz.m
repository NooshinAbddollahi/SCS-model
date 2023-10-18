%% The SCS abstract model for 1kHz including noise - In this code fast AHP, ADP and slow AHP mechanisms are considered. 
clc
clear all
close all
%
t=20000 ;  % time of stimulation (ms)

sigma=0.05 ;   % sigma for Guassian noise

threshold= 0  ;          % threshold is updated based on slow AHP

for i=1:t
    
r(1,i)=normrnd(threshold,sigma)     ;     % first step: a random number with guassian distribution is chosen , if the number>threshold => spike , otherwise no spike

if r(1,i) > threshold
    spike(1,i) = 1 ;
     s=i ;
    
    break
else 
    spike(1,i) = 0 ;
   
end
end


T=1 ;                     % time since last spike

% 6 parameters
step_size= 0.002;           % step size for slow AHP   
sAHP_tau=1200 ;              % slow AHP time constant

fAHP_amp=-0.7 ;          % fast AHP amplitude
fAHP_tau=2 ;             % fast AHP time constant

ADP_amp=0.3 ;            % ADP amplitude
ADP_tau=40 ;             % ADP time constant



a=step_size ;

for i=s+1:t
  
Fast_AHP= fAHP_amp*exp(-T/fAHP_tau);  
ADP= ADP_amp* exp(-T/ADP_tau)   ;
slow_AHP= a* exp(-T/sAHP_tau)   ;
threshold=slow_AHP ;
%threshold= normrnd(threshold,sigma) ;   % noisy threshold


C= Fast_AHP+ADP ;     % Combined fast AHP and ADP
C= normrnd(C,sigma)     ;   % noisy 

%C ;
  
    if   C > threshold
          spike(1,i)= 1 ;
          a= slow_AHP+ step_size ;
          T= 1 ;
          
    else
        spike(1,i)= 0 ;  
        T=T+1  ;
       
    end 
    
end 

% Plotting spike pattern 
figure
plot(1:t , spike , 'r')                                  
ylim([0 10])
xlabel('time from SCS onset (ms)')
%size(spike)

%% Calculating interspike interval

j=1 ;

for i=1:t                                                    
    if spike(1,i)==1
        v(1,j)=i ;
        j=j+1 ;
    end

end


j=1 ;


for i=1:(length(v)-1)

    ISI(1,j)=v(1,i+1)-v(1,i) ;      % ISI : interspike interval
    j=j+1 ;
end

% N7=ISI ;
% N='N7.mat' ;
% save(N) 


%% ISI histogram

x = unique(ISI)   ;    % temp vector of vals
ISI = sort(ISI)    ;     % sorted input aligns with temp (lowest to highest)
p = zeros(size(x)); % vector for freqs
% frequency for each value
for i = 1:length(x)
    p(i) = (sum(ISI == x(i)))/ (length(ISI)) ;
end
x ;
%p ;
%sum(p)
width=0.2 ;
%subplot(2,1,2) ;
figure
bar(x,p , 'r')
xlim([0 100])
xlabel('interspike interval (ms)' , 'FontSize', 10)
ylabel('p(ISI)' , 'FontSize', 10)
%set(gca,'XScale','log');



%%

%  N101k=ISI ;
%  N='N101k.mat' ;
%  save(N) 

%%
SPIKE(:,1)=spike ;
%%
 %xlswrite('Workbook.xlsx',spike)
figure
plot(1:20000,SPIKE)
ylim([0 10])









