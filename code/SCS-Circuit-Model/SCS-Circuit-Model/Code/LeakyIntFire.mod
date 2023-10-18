NEURON {
	: ARTIFICIAL_CELL means
	
	ARTIFICIAL_CELL LeakyIntFire
	RANGE m, Iext, i, taum, Cm, tauref, tausyn
	: m plays the role of voltage
}

PARAMETER {
	:Postsynaptic current time constant
	:Reset potential
	Vreset = -85 (mV) 
	:Fixed firing threshold
	Vtheta  = -51 (mV)
	: External Current
	Iext = 0 (nA)
}

: Specify units that have physiological interpretations (NB: ms is already declared)
UNITS {
  (mV) = (millivolt)
  (pF) = (picofarad)
  (pA) = (picoamps)
}


ASSIGNED {
	m(mV)
	i(pA)
	t0(ms)
	refractory
	Cm(pF)
	taum(ms)
	tauref(ms) 
	tausyn(ms)
}

FUNCTION M() {

}

FUNCTION I() {

}

INITIAL {
	t0 = t
	refractory = 0 : 0-integrates input, 1-refractory
}

NET_RECEIVE (w) {
	if (refractory == 0) { : inputs integrated only when excitable

		:6.5
		i=i+(-i/tausyn)*(t-t0)
		i=i+w
		m=m+(((Vreset-m)/taum)+((i+Iext)/Cm))*(t-t0)
	
		:7.5
		:i=i+w
		:m=m+(((Vreset-m)/taum)+((i+Iext)/Cm))*(t-t0)
		:i=i-(i/tausyn)*(t-t0)
		
		:6.7
		:m=m+(((Vreset-m)/taum)+((i+Iext)/Cm))*(t-t0)
		:i=i+w
		:i=i-(i/tausyn)*(t-t0)
		t0 = t

		if (m > Vtheta) {
			refractory = 1
			:m = Vreset
			m = Vreset+100
			net_send(tauref, refractory)
			net_event(t)
		}
	}else if (flag == 1) { : ready to integrate again
		t0 = t
		refractory = 0
		m = Vreset
	}
}
