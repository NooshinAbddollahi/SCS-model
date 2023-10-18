
clear
close all

%use this script to generate QQ uncorrelated OU Noise traces for use with
%simplified P&D neuron.  Only need x(i).  OU Noises will have unit
%amplitudes; scaling will occur within NEURON.
for QQ = 1:30
fname = ['MRG_Base_0p01_0p5tau_' num2str(QQ) '.txt'];
%parameters
t_start = 0;          %simulation start time
t_end = 1000;          %simuation end time
dt = 0.005;            %time step.  Should match NEURON.
tau = 0.5;            %relaxation time.  5 ms consistent with Prescott and Senjowski 2008.  On Prescott's advice, 0.5 ms might be better for channel noise (5 ms was appropriate for synaptic noise).
c = 0.0004;                %diffusion constant, or related to variance per Gillespie 1996.  Baseline OU Noise variance such that SD --> 1/100 of signal.  multiply by 2, 5, 10, 20 for weak --> strong noise.
x0 = 0;               %initial value for stochastic variable x
mu = 0;               %mean of stochatic process x
y0 = 0;               %initial value for integral x 
start_dist = 0;    %start of OU pdf 
end_dist = 2.0;       %end of OU pdf
cond_scale = 1; %conductance scalar, in nS or nA, depending on application to NEURON.

%time
T = t_start:dt:t_end;

%compute x and y
i = 1;
x(1) = mu; 
y(1) = y0;
for t=t_start+dt:dt:t_end
   i = i + 1; 
   r1 = randn;
   r2 = randn;
   x(i) = (x(i-1))*exp(-dt/tau) + sqrt((c*tau*0.5)*(1-(exp(-dt/tau))^2))*r1;
   y(i) = y(i-1) + x(i-1)*tau*(1-exp(-dt/tau))+sqrt((c*tau^3*(dt/tau-2*(1-exp(-dt/tau))+0.5*(1-exp(-2*dt/tau))))-((0.5*c*tau^2)*(1-exp(-dt/tau))^2)^2/((c*tau/2)*(1-exp(-2*dt/tau))))*r2+((0.5*c*tau^2)*(1-exp(-dt/tau))^2)/(sqrt((c*tau/2)*(1-(exp(-dt/tau))^2)))*r1;
end

x = (x+ x0).*cond_scale;
%x(x<0)=0; %set all negative conductance values (which don't make sense) to 0.

%pdf for OU process
k = 0; j = start_dist:dt:end_dist;
for l=start_dist:dt:end_dist
    k = k + 1;
    p(k) = sqrt((1/tau)/(pi*c))*exp(-(1/tau)*(l-mu)^2/(c)); 
end

%save OU Noise
dlmwrite(['OUNoise_' fname], x, ' ');
end