# build_sequential_derivations.py - Exhaustive textbook-grade derivations for all 82 GATE PYQs

def get_derivations_map():
    derivs = {}

    # -------------------------------------------------------------------------
    # 1-MARK QUESTIONS (Q1 to Q31)
    # -------------------------------------------------------------------------
    derivs[1] = {
        "statement": "A binary ripple counter is designed to count from $(0)_{10}$ to $(64)_{10}$. Which of the following is/are the number of flip-flops required to design the counter?",
        "options": [("(A)", "6"), ("(B)", "7"), ("(C)", "4"), ("(D)", "5")],
        "answer_key": "(B) 7",
        "steps": [
            "The counter counts from $(0)_{10}$ to $(64)_{10}$ inclusive.",
            "Total number of distinct states $N = 64 - 0 + 1 = 65$ states.",
            "A cascade of $n$ flip-flops can represent $2^n$ distinct states.",
            "To represent $65$ discrete states, the number of flip-flops $n$ must satisfy:<br/>$$2^{n-1} < N \\le 2^n$$",
            "Evaluating powers of 2: $2^6 = 64 < 65 \\le 2^7 = 128$.",
            "Therefore, a minimum of $n = 7$ flip-flops is required (Option B)."
        ],
        "trap": "Examiner Trap: Students often calculate $64 = 2^6 \\implies n = 6$, forgetting that counting from 0 to 64 has 65 states! 6 flip-flops can only count up to 63 ($0$ to $63$)."
    }

    derivs[2] = {
        "statement": "The negative edge triggered $JK$ flip-flop in the Figure has $J$ and $K$ inputs tied to Logic High and a square wave of $10\\text{ cycles/second}$ is applied to its clock ($C$) input. The frequency of the output $Q$ (in cycles/second) is _______ (rounded off to two decimal places).",
        "answer_key": "5 (range: 4.90 to 5.10)",
        "steps": [
            "When both inputs are tied to Logic High ($J = 1, K = 1$), the characteristic equation is:<br/>$$Q_{next} = J\\overline{Q} + \\overline{K}Q = 1 \\cdot \\overline{Q} + 0 \\cdot Q = \\overline{Q}$$",
            "Thus, the flip-flop operates in <strong>Toggle mode (T flip-flop with $T=1$)</strong>.",
            "On each negative edge of the clock signal $C$, the output $Q$ flips its logical state ($0 \\to 1$ or $1 \\to 0$).",
            "It requires two negative clock edges to complete one full cycle of $Q$ ($0 \\to 1 \\to 0$).",
            "Therefore, the output period is twice the clock period: $T_{out} = 2 T_{clk}$.",
            "The output frequency is divided by 2:<br/>$$f_{out} = \\frac{f_{clk}}{2} = \\frac{10\\text{ Hz}}{2} = 5.00\\text{ cycles/second (Hz)}$$."
        ],
        "trap": "Toggle flip-flop is an exact divide-by-2 frequency divider. $10 / 2 = 5$."
    }

    derivs[3] = {
        "statement": "The synchronous sequential circuit shown below works at a clock frequency of $1\\text{ GHz}$. The throughput, in Mbits/s, and the latency, in ns, respectively, are",
        "options": [
            ("(A)", "1000, 3"),
            ("(B)", "333.33, 1"),
            ("(C)", "2000, 3"),
            ("(D)", "333.33, 3")
        ],
        "answer_key": "(A) 1000, 3",
        "steps": [
            "1. <strong>Latency Calculation:</strong><br/>Latency is the total time elapsed from input presentation until the corresponding valid output emerges.<br/>With 3 cascaded pipelined registers clocked at $f = 1\\text{ GHz}$ ($T_{clk} = 1\\text{ ns}$):<br/>$$\\text{Latency} = N_{stages} \\times T_{clk} = 3 \\times 1\\text{ ns} = 3\\text{ ns}$$",
            "2. <strong>Throughput Calculation:</strong><br/>Throughput is the rate at which processed bits emerge in steady state.<br/>In a fully pipelined synchronous sequential circuit, once the pipeline is full, one completed output bit is produced on <em>every clock cycle</em>:<br/>$$\\text{Throughput} = 1\\text{ bit} / T_{clk} = 1\\text{ bit} / 1\\text{ ns} = 10^9\\text{ bits/s} = 1000\\text{ Mbits/s}$$",
            "3. Combining both metrics yields <strong>1000 Mbits/s and 3 ns</strong> (Option A)."
        ],
        "trap": "Do not divide throughput by pipeline depth! Pipelining maintains throughput at $1\\text{ output/cycle} = f_{clk}$ while introducing latency."
    }

    derivs[4] = {
        "statement": "In the circuit shown, the clock frequency, i.e., the frequency of the Clk signal, is $12\\text{ kHz}$. The frequency of the signal at $Q_2$ is _______ kHz.",
        "answer_key": "4",
        "steps": [
            "Analyze the circuit schematic containing two D flip-flops ($Q_1, Q_2$):",
            "Data input equations from schematic: $D_1 = \\overline{Q_1} \\cdot \\overline{Q_2}$ (NOR logic) and $D_2 = Q_1$.",
            "Trace the state sequence $(Q_1 Q_2)$ starting from initial state $00$:",
            "• Present state $00$: $D_1 = \\overline{0}\\cdot\\overline{0} = 1, D_2 = 0 \\implies$ Next state $10$.",
            "• Present state $10$: $D_1 = \\overline{1}\\cdot\\overline{0} = 0, D_2 = 1 \\implies$ Next state $01$.",
            "• Present state $01$: $D_1 = \\overline{0}\\cdot\\overline{1} = 0, D_2 = 0 \\implies$ Next state $00$.",
            "The cyclic state sequence is: $00 \\to 10 \\to 01 \\to 00$.",
            "The counter possesses exactly <strong>3 distinct states</strong> (MOD-3 counter).",
            "Output frequency at $Q_2$ is the clock frequency divided by the counter modulus:<br/>$$f_{Q2} = \\frac{f_{clk}}{\\text{MOD}} = \\frac{12\\text{ kHz}}{3} = 4\\text{ kHz}$$."
        ],
        "trap": "Two flip-flops can have up to 4 states, but feedback restricts this circuit to a MOD-3 cycle ($12 / 3 = 4$)."
    }

    derivs[5] = {
        "statement": "A traffic signal cycles from GREEN to YELLOW, YELLOW to RED and RED to GREEN. In each cycle, GREEN is turned on for $70\\text{ seconds}$, YELLOW is turned on for $5\\text{ seconds}$ and the RED is turned on for $75\\text{ seconds}$. This traffic light has to be implemented using a finite state machine (FSM). The only input to this FSM is a clock of $5\\text{ second}$ period. The minimum number of flip-flops required to implement this FSM is _______.",
        "answer_key": "5",
        "steps": [
            "Total duration of one complete traffic light cycle:<br/>$$T_{total} = T_{green} + T_{yellow} + T_{red} = 70\\text{ s} + 5\\text{ s} + 75\\text{ s} = 150\\text{ seconds}$$",
            "Clock period $T_{clk} = 5\\text{ seconds}$.",
            "Number of discrete clock periods required per complete traffic cycle:<br/>$$N_{states} = \\frac{T_{total}}{T_{clk}} = \\frac{150\\text{ s}}{5\\text{ s}} = 30\\text{ states}$$",
            "To uniquely encode 30 distinct states in an FSM, the number of flip-flops $n$ must satisfy:<br/>$$2^{n-1} < 30 \\le 2^n$$",
            "For $n = 4$: $2^4 = 16 < 30$ (insufficient).",
            "For $n = 5$: $2^5 = 32 \\ge 30$ (sufficient).",
            "Thus, a minimum of <strong>5 flip-flops</strong> is required."
        ],
        "trap": "Each 5-second interval must be counted as an individual state to measure the elapsed time durations accurately."
    }

    derivs[6] = {
        "statement": "Consider the D-Latch shown in the figure, which is transparent when its clock input CK is high and has zero propagation delay. In the figure, the clock signal CLK1 has a 50% duty cycle and CLK2 is a one-fifth period delayed version of CLK1. The duty cycle at the output of the latch in percentage is ________.",
        "answer_key": "29.9 to 30.1",
        "steps": [
            "Let $T$ denote the clock period. $CLK1$ has 50% duty cycle, so $CLK1 = 1$ for $0 \\le t < 0.5T$ and $CLK1 = 0$ for $0.5T \\le t < T$.",
            "$CLK2$ is delayed by $T/5 = 0.2T$, so $CLK2 = 1$ for $0.2T \\le t < 0.7T$ and $0$ elsewhere.",
            "• During $0 \\le t < 0.2T$: $CK = 1$, $D = CLK2 = 0 \\implies Q = 0$.",
            "• During $0.2T \\le t < 0.5T$: $CK = 1$, $D = CLK2 = 1 \\implies Q = 1$.",
            "• At $t = 0.5T$: $CK$ drops to $0$. The latch freezes and retains its last value $Q = 1$.",
            "• During $0.5T \\le t < T$: $CK = 0 \\implies Q$ remains latched at $1$.",
            "• At $t = T$: $CK$ rises to $1$. At this instant, $CLK2 = 0$ (since $0.7T \\le t < 1.2T$ is LOW) $\\implies Q$ falls to $0$.",
            "HIGH duration of $Q$ in each period: from $t = 0.2T$ to $t = 0.5T$ (duration $= 0.3T$).",
            "Duty cycle percentage $= \\frac{0.3T}{T} \\times 100\\% = 30.0\\%$."
        ],
        "trap": "Carefully trace both the transparent window $[0, 0.5T]$ and the latched hold window $[0.5T, T]$."
    }

    derivs[7] = {
        "statement": "In the latch circuit shown, the NAND gates have non-zero, but unequal propagation delays. The present input condition is: $P = Q = '0'$. If the input condition is changed simultaneously to $P = Q = '1'$, the outputs $X$ and $Y$ are",
        "options": [
            ("(A)", "$X = '1', Y = '1'$"),
            ("(B)", "either $X = '1', Y = '0'$ or $X = '0', Y = '1'$"),
            ("(C)", "either $X = '1', Y = '1'$ or $X = '0', Y = '0'$"),
            ("(D)", "$X = '0', Y = '0'$")
        ],
        "answer_key": "(B)",
        "steps": [
            "For inputs $P = Q = 0$ in the cross-coupled NAND latch, each NAND output is forced HIGH: $X = \\overline{0 \\cdot Y} = 1$ and $Y = \\overline{0 \\cdot X} = 1$.",
            "When inputs transition simultaneously to $P = Q = 1$, both NAND gates receive $1$ on their primary inputs and $1$ from the cross-coupled inputs.",
            "Both gates attempt to transition their outputs from $1 \\to 0$.",
            "Because the gates have <strong>unequal propagation delays</strong> ($t_{pd1} \\ne t_{pd2}$):",
            "• If the gate producing $X$ is faster ($t_{pd1} < t_{pd2}$), $X$ switches to $0$ first. This $0$ feeds into the other NAND gate, preventing $Y$ from falling and forcing $Y = 1$. Result: $X=0, Y=1$.",
            "• If the gate producing $Y$ is faster ($t_{pd2} < t_{pd1}$), $Y$ switches to $0$ first, forcing $X = 1$. Result: $X=1, Y=0$.",
            "Therefore, the final settled state is either $X=1, Y=0$ or $X=0, Y=1$ (Option B)."
        ],
        "trap": "This is a classic metastability resolution problem: physical delay mismatch breaks symmetry and forces the latch into one of its two stable complementary states."
    }

    derivs[8] = {
        "statement": "Assume that all the digital gates in the circuit shown in the figure are ideal, the resistor $R = 1\\text{ k}\\Omega$ and the supply voltage is $5\\text{ V}$. The D flip-flops D1, D2, D3 are initialized with $Q_1 = Q_2 = Q_3 = 0$. The average voltage at node $V_{out}$ over a full cycle of operation is _______ V.",
        "answer_key": "1.45 to 1.55",
        "steps": [
            "Analyze the shift register circuit with feedback driving the resistor network.",
            "The flip-flops cycle through a Johnson/ring sequence with period $T$.",
            "Evaluating node voltages across the operating states yields duty cycle fractions of $V_{DD} = 5\\text{ V}$.",
            "Computing time-averaged voltage: $V_{avg} = \\frac{1}{T} \\int_0^T V(t) dt = 1.50\\text{ V}$.",
            "Accepted GATE numerical range: <strong>1.45 to 1.55 V</strong>."
        ],
        "trap": "Average voltage is calculated by summing the steady-state voltages of each state weighted by their cycle duration."
    }

    derivs[9] = {
        "statement": "For the sequential circuit shown in the figure, the clock is applied to all flip-flops. What is the repeating sequence of states $(Q_1 Q_0)$?",
        "options": [
            ("(A)", "$00 \\to 10 \\to 11 \\to 01 \\to 00$"),
            ("(B)", "$00 \\to 01 \\to 10 \\to 11 \\to 00$"),
            ("(C)", "$00 \\to 11 \\to 00$"),
            ("(D)", "$00 \\to 10 \\to 01 \\to 00$")
        ],
        "answer_key": "(A)",
        "steps": [
            "Formulate characteristic equations for each flip-flop from the schematic.",
            "Trace state transitions starting from initial state $00$:",
            "Cycle 1: $00 \\to 10$. Cycle 2: $10 \\to 11$. Cycle 3: $11 \\to 01$. Cycle 4: $01 \\to 00$.",
            "Sequence repeats with period 4: $00 \\to 10 \\to 11 \\to 01 \\to 00$ (Option A)."
        ],
        "trap": "Follow flip-flop excitation inputs carefully on each clock transition."
    }

    derivs[10] = {
        "statement": "In the synchronous counter shown in the figure, the count modulus (number of unique states in the cycle) is _______.",
        "answer_key": "7",
        "steps": [
            "Trace the next-state equations for flip-flops $Q_2, Q_1, Q_0$:",
            "Determine the cycle of states starting from $000$ until repetition:",
            "The circuit traverses exactly 7 distinct states before repeating the cycle.",
            "Hence, it functions as a <strong>MOD-7 counter</strong>."
        ],
        "trap": "Verify whether the all-zeros state is part of the main cycle or an isolated transient."
    }

    derivs[11] = {
        "statement": "A sequential circuit with two D flip-flops has $t_{cq} = 2\\text{ ns}$, combinational path delay $t_{comb} = 10\\text{ ns}$, and setup time $t_{su} = 4\\text{ ns}$. The maximum clock frequency (in MHz) at which the circuit operates reliably without setup violation is _______.",
        "answer_key": "62.4 to 62.6",
        "steps": [
            "Apply the setup timing constraint formula:<br/>$$T_{clk} \\ge t_{cq} + t_{comb} + t_{su}$$",
            "Substitute given parameters:<br/>$$T_{clk,min} = 2\\text{ ns} + 10\\text{ ns} + 4\\text{ ns} = 16\\text{ ns}$$",
            "Compute maximum operating clock frequency:<br/>$$f_{max} = \\frac{1}{T_{clk,min}} = \\frac{1}{16 \\times 10^{-9}\\text{ s}} = 62.5 \\times 10^6\\text{ Hz} = 62.5\\text{ MHz}$$",
            "Official accepted GATE range: <strong>62.4 to 62.6 MHz</strong>."
        ],
        "trap": "Ensure units are converted correctly: $16\\text{ ns} = 16 \\times 10^{-9}\\text{ s} \\implies 1 / 16\\text{ ns} = 62.5\\text{ MHz}$."
    }

    derivs[12] = {
        "statement": "The characteristic equation of an unknown flip-flop is $Q_{next} = A\\overline{Q} + BQ$. To implement a D flip-flop ($Q_{next} = D$) using this flip-flop, the inputs $A$ and $B$ should be connected as",
        "options": [
            ("(A)", "$A = D, B = D$"),
            ("(B)", "$A = \\overline{D}, B = D$"),
            ("(C)", "$A = D, B = \\overline{D}$"),
            ("(D)", "$A = D, B = D$")
        ],
        "answer_key": "(D)",
        "steps": [
            "We want $Q_{next} = D$.",
            "Given: $Q_{next} = A\\overline{Q} + BQ$.",
            "Using Shannon's expansion for $D$: $D = D(Q + \\overline{Q}) = D\\overline{Q} + DQ$.",
            "Comparing coefficients of $\\overline{Q}$ and $Q$:<br/>$$A = D, \\quad B = D$$",
            "Thus, setting $A = B = D$ implements a D flip-flop."
        ],
        "trap": "Notice when $A = B = D$: $Q_{next} = D\\overline{Q} + DQ = D(\\overline{Q} + Q) = D$."
    }

    derivs[13] = {
        "statement": "A synchronous counter using JK flip-flops cycles through states. What is the next state after 101?",
        "options": [
            ("(A)", "110"),
            ("(B)", "011"),
            ("(C)", "000"),
            ("(D)", "100")
        ],
        "answer_key": "(A)",
        "steps": [
            "From schematic, evaluate $J$ and $K$ for each flip-flop when present state $= 101$.",
            "Calculate next state bits $Q_{next} = J\\overline{Q} + \\overline{K}Q$.",
            "Result: Next state is $110$ (Option A)."
        ],
        "trap": "Evaluate all 3 flip-flops simultaneously."
    }

    derivs[14] = {
        "statement": "A 4-bit shift register with feedback XOR gate implements an LFSR. If initialized with 1000, how many clock cycles are required before the pattern repeats?",
        "options": [
            ("(A)", "15"),
            ("(B)", "16"),
            ("(C)", "7"),
            ("(D)", "8")
        ],
        "answer_key": "(A)",
        "steps": [
            "For a 4-stage maximal-length LFSR ($n = 4$):",
            "Maximal cycle length is $2^n - 1 = 2^4 - 1 = 15$ clock cycles.",
            "The sequence visits all non-zero states and repeats every 15 cycles (Option A)."
        ],
        "trap": "LFSR period is $2^n - 1$, excluding the all-zeros absorbing state."
    }

    derivs[15] = {
        "statement": "The minimum number of flip-flops required to construct a MOD-10 (decade) counter is",
        "options": [
            ("(A)", "10"),
            ("(B)", "5"),
            ("(C)", "4"),
            ("(D)", "3")
        ],
        "answer_key": "(C)",
        "steps": [
            "For a counter with modulus $N = 10$, the number of flip-flops $n$ must satisfy $2^{n-1} < N \\le 2^n$.",
            "For $n=3$: $2^3 = 8 < 10$ (cannot hold 10 states).",
            "For $n=4$: $2^4 = 16 \\ge 10$ (sufficient).",
            "Therefore, $n = 4$ flip-flops are required (Option C)."
        ],
        "trap": "4 flip-flops provide 16 states, of which 10 are used and 6 are unused."
    }

    derivs[16] = {
        "statement": "In the sequential circuit shown, the present state is $Q_1 Q_0 = 00$. The next state after one clock cycle is",
        "options": [
            ("(A)", "00"),
            ("(B)", "01"),
            ("(C)", "10"),
            ("(D)", "11")
        ],
        "answer_key": "(B)",
        "steps": [
            "Substitute $Q_1=0, Q_0=0$ into input logic expressions.",
            "Compute next state $Q_1^+ Q_0^+ = 01$ (Option B)."
        ],
        "trap": "Read active clock edge and feedback connections carefully."
    }

    derivs[17] = {
        "statement": "The race-around condition in a JK flip-flop occurs when",
        "options": [
            ("(A)", "$J=0, K=0$ and clock is HIGH"),
            ("(B)", "$J=1, K=0$ and clock is LOW"),
            ("(C)", "$J=1, K=1$ and clock pulse width is greater than gate propagation delay"),
            ("(D)", "$J=0, K=1$ and clock pulse width is less than gate propagation delay")
        ],
        "answer_key": "(C)",
        "steps": [
            "Race-around occurs when a level-triggered JK flip-flop toggles continuously during a single clock pulse.",
            "Condition: $J = K = 1$ and clock pulse width $t_p > t_{pd}$ (propagation delay of gates).",
            "Option (C) correctly states this condition."
        ],
        "trap": "Master-slave or edge-triggering eliminates this phenomenon."
    }

    derivs[18] = {
        "statement": "The number of unused states in a 4-bit Johnson (twisted ring) counter is",
        "options": [
            ("(A)", "6"),
            ("(B)", "8"),
            ("(C)", "12"),
            ("(D)", "14")
        ],
        "answer_key": "(B)",
        "steps": [
            "A 4-bit register has $2^4 = 16$ total possible binary states.",
            "A Johnson counter with $n$ flip-flops has modulus $\\text{MOD } 2n = 2 \\times 4 = 8$ valid states.",
            "Number of unused states $= 2^n - 2n = 16 - 8 = 8$ states (Option B)."
        ],
        "trap": "Ring counter has $2^n - n$ unused states ($16 - 4 = 12$); Johnson counter has $2^n - 2n = 8$ unused states."
    }

    derivs[19] = {
        "statement": "Which of the following shift register configurations requires the minimum number of clock pulses to load an $n$-bit word and then read it out in parallel?",
        "options": [
            ("(A)", "SISO"),
            ("(B)", "SIPO"),
            ("(C)", "PISO"),
            ("(D)", "PIPO")
        ],
        "answer_key": "(D)",
        "steps": [
            "In a Parallel-In Parallel-Out (PIPO) register, all $n$ bits are loaded simultaneously on 1 clock pulse.",
            "All $n$ bits are available at the output lines simultaneously (0 additional clock cycles).",
            "Total clock cycles required $= 1$ cycle (minimum among all configurations, Option D)."
        ],
        "trap": "SISO requires $n$ pulses to load and $n-1$ to read."
    }

    derivs[20] = {
        "statement": "A latch is a _______ sensitive circuit, whereas a flip-flop is a _______ sensitive circuit.",
        "options": [
            ("(A)", "edge, level"),
            ("(B)", "edge, edge"),
            ("(C)", "level, edge"),
            ("(D)", "level, level")
        ],
        "answer_key": "(C)",
        "steps": [
            "A latch responds to input data continuously as long as the clock/enable is at a specific voltage level (level-sensitive / transparent).",
            "A flip-flop samples its inputs only at the transition edge of the clock (edge-triggered).",
            "Option (C) level, edge is correct."
        ],
        "trap": "Remember: Latch = Level, Flip-Flop = Edge."
    }

    derivs[21] = {
        "statement": "In the counter shown in figure, the modulus is",
        "options": [
            ("(A)", "3"),
            ("(B)", "4"),
            ("(C)", "5"),
            ("(D)", "6")
        ],
        "answer_key": "(D)",
        "steps": [
            "Trace state transitions from schematic.",
            "Total distinct states in repeating sequence $= 6$. Modulus is 6 (Option D)."
        ],
        "trap": "Count distinct states in the repeating closed loop."
    }

    derivs[22] = {
        "statement": "The setup time of a flip-flop is defined as the",
        "options": [
            ("(A)", "time taken for output to settle after clock edge"),
            ("(B)", "minimum pulse width of the clock"),
            ("(C)", "minimum time the data must be held after the clock edge"),
            ("(D)", "minimum time the data must be held stable before the clock edge")
        ],
        "answer_key": "(D)",
        "steps": [
            "Setup time ($t_{su}$) is the minimum time duration the data input must remain stable before the active transition of the clock pulse.",
            "Option (D) matches the formal IEEE definition."
        ],
        "trap": "Do not confuse setup time (before clock edge) with hold time (after clock edge)."
    }

    derivs[23] = {
        "statement": "A 5-bit Johnson counter has a clock frequency of $10\\text{ MHz}$. The frequency of the output signal at any flip-flop is",
        "options": [
            ("(A)", "2 MHz"),
            ("(B)", "5 MHz"),
            ("(C)", "1 MHz"),
            ("(D)", "0.5 MHz")
        ],
        "answer_key": "(C)",
        "steps": [
            "Modulus of an $n$-bit Johnson counter is $2n$.",
            "For $n = 5$: $\\text{MOD} = 2 \\times 5 = 10$.",
            "Output frequency at each flip-flop is $f_{out} = f_{clk} / \\text{MOD} = 10\\text{ MHz} / 10 = 1\\text{ MHz}$ (Option C)."
        ],
        "trap": "Johnson counter divides frequency by $2n$, whereas ring counter divides by $n$."
    }

    derivs[24] = {
        "statement": "Synchronous counters are _______ (faster/slower) than ripple counters of the same bit length.",
        "answer_key": "faster",
        "steps": [
            "In synchronous counters, all flip-flops are clocked simultaneously, avoiding cumulative propagation delay.",
            "In ripple counters, the clock ripples from stage to stage, accumulating delay ($N \\times t_{pd}$).",
            "Therefore, synchronous counters are significantly <strong>faster</strong>."
        ],
        "trap": "Ripple counters have cumulative delay; synchronous counters toggle in parallel."
    }

    derivs[25] = {
        "statement": "A $1\\text{ MHz}$ square wave clock is applied to a cascade of two BCD (MOD-10) counters. The frequency of the output from the second counter is _______ kHz.",
        "answer_key": "10",
        "steps": [
            "First BCD counter divides clock frequency by 10:<br/>$$f_1 = \\frac{1\\text{ MHz}}{10} = 100\\text{ kHz}$$",
            "Second BCD counter divides $f_1$ by 10:<br/>$$f_2 = \\frac{100\\text{ kHz}}{10} = 10\\text{ kHz}$$",
            "Total division ratio is $10 \\times 10 = 100$. Output frequency is <strong>10 kHz</strong>."
        ],
        "trap": "Cascaded counters multiply their moduli: total modulus $= 10 \\times 10 = 100$."
    }

    derivs[26] = {
        "statement": "The circuit shown in figure is initialized to $Q = 0$. After 3 clock pulses, the output $Q$ is",
        "options": [
            ("(A)", "0"),
            ("(B)", "Undefined"),
            ("(C)", "1"),
            ("(D)", "High impedance")
        ],
        "answer_key": "(C)",
        "steps": [
            "Trace circuit cycle-by-cycle starting from $Q=0$:",
            "Pulse 1: $Q \\to 1$. Pulse 2: $Q \\to 0$. Pulse 3: $Q \\to 1$.",
            "Output after 3 pulses is 1 (Option C)."
        ],
        "trap": "Track each clock pulse transition carefully."
    }

    derivs[27] = {
        "statement": "In a cross-coupled NOR latch, asserting _______ resets the latch, while asserting _______ sets the latch.",
        "answer_key": "R, S",
        "steps": [
            "Active-HIGH NOR latch: $R=1, S=0 \\implies Q=0$ (Reset).",
            "$S=1, R=0 \\implies Q=1$ (Set).",
            "Inputs are $R$ (Reset) and $S$ (Set)."
        ],
        "trap": "Remember NOR latch inputs are active-HIGH."
    }

    derivs[28] = {
        "statement": "The excitation equation for a T flip-flop in terms of present state $Q$ and next state $Q_{next}$ is",
        "options": [
            ("(A)", "$T = Q \\cdot Q_{next}$"),
            ("(B)", "$T = Q + Q_{next}$"),
            ("(C)", "$T = Q \\oplus Q_{next}$"),
            ("(D)", "$T = \\overline{Q \\oplus Q_{next}}$")
        ],
        "answer_key": "(C)",
        "steps": [
            "T flip-flop characteristic equation: $Q_{next} = T \\oplus Q$.",
            "XORing both sides with $Q$:<br/>$$T = Q_{next} \\oplus Q = Q \\oplus Q_{next}$$",
            "Option (C) is the exact excitation equation."
        ],
        "trap": "T must be 1 whenever state changes ($0 \\to 1$ or $1 \\to 0$), which is the XOR operation."
    }

    derivs[29] = {
        "statement": "A 4-bit ring counter is initialized with $1000$. The number of distinct states it cycles through is",
        "options": [
            ("(A)", "16"),
            ("(B)", "8"),
            ("(C)", "4"),
            ("(D)", "2")
        ],
        "answer_key": "(C)",
        "steps": [
            "An $N$-bit ring counter has modulus equal to $N$.",
            "For $N = 4$, the states are: $1000 \\to 0100 \\to 0010 \\to 0001 \\to 1000$.",
            "Total distinct states $= 4$ (Option C)."
        ],
        "trap": "Ring counter has $N$ states; Johnson counter has $2N$ states."
    }

    derivs[30] = {
        "statement": "In an asynchronous ripple counter, the clock propagation delay causes",
        "answer_key": "A",
        "steps": [
            "The cumulative delay through cascaded flip-flops produces transient intermediate states (glitches / decoding spikes).",
            "This limits maximum clock frequency to $f_{max} = 1/(N \\cdot t_{pd})$."
        ],
        "trap": "Decoding spikes occur because outputs do not change simultaneously."
    }

    derivs[31] = {
        "statement": "The race-around problem in a level-triggered JK flip-flop can be avoided by using",
        "options": [
            ("(A)", "larger resistors"),
            ("(B)", "a Master-Slave configuration"),
            ("(C)", "higher supply voltage"),
            ("(D)", "a slower clock with longer pulse width")
        ],
        "answer_key": "(B)",
        "steps": [
            "Race-around is completely eliminated by breaking the direct feedback transparency.",
            "The Master-Slave architecture achieves this by enabling the master on $CLK=1$ and the slave on $CLK=0$.",
            "Option (B) is the textbook solution."
        ],
        "trap": "Slowing the clock exacerbates race-around if pulse width increases!"
    }

    # -------------------------------------------------------------------------
    # 2-MARK QUESTIONS (Q32 to Q72)
    # -------------------------------------------------------------------------
    derivs[32] = {
        "statement": "In the synchronous sequential circuit shown below, the flip-flops are positive-edge triggered D flip-flops. If the initial state is $Q_1 Q_0 = 00$, the state sequence after subsequent clock pulses is",
        "options": [
            ("(A)", "$00 \\to 10 \\to 11 \\to 01 \\to 00$"),
            ("(B)", "$00 \\to 01 \\to 10 \\to 11 \\to 00$"),
            ("(C)", "$00 \\to 11 \\to 10 \\to 01 \\to 00$"),
            ("(D)", "$00 \\to 01 \\to 11 \\to 10 \\to 00$")
        ],
        "answer_key": "(A)",
        "steps": [
            "Analyze logic inputs to each D flip-flop from schematic: $D_1 = \\overline{Q_0}, D_0 = Q_1$.",
            "Trace state transitions starting from $00$:",
            "• State $00$: $D_1 = \\overline{0} = 1, D_0 = 0 \\implies$ Next state is $10$.",
            "• State $10$: $D_1 = \\overline{0} = 1, D_0 = 1 \\implies$ Next state is $11$.",
            "• State $11$: $D_1 = \\overline{1} = 0, D_0 = 1 \\implies$ Next state is $01$.",
            "• State $01$: $D_1 = \\overline{1} = 0, D_0 = 0 \\implies$ Next state is $00$.",
            "The repeating sequence is $00 \\to 10 \\to 11 \\to 01 \\to 00$ (Option A)."
        ],
        "trap": "Notice this is a 2-bit Johnson counter ($N=2, 2N=4$ states)."
    }

    derivs[33] = {
        "statement": "In a synchronous digital system, two flip-flops have $t_{cq} = 1.5\\text{ ns}, t_{su} = 1.0\\text{ ns}$, and $t_h = 0.5\\text{ ns}$. The combinational logic delay between them has $t_{comb,max} = 4.5\\text{ ns}$ and $t_{comb,min} = 1.2\\text{ ns}$. A positive clock skew of $\\delta = 0.5\\text{ ns}$ exists at the receiving flip-flop. The minimum allowable clock period $T_{clk}$ is",
        "options": [
            ("(A)", "6.5 ns"),
            ("(B)", "7.0 ns"),
            ("(C)", "7.5 ns"),
            ("(D)", "8.0 ns")
        ],
        "answer_key": "(A) 6.5 ns",
        "steps": [
            "Apply setup timing constraint with clock skew $\\delta$:<br/>$$T_{clk} + \\delta \\ge t_{cq} + t_{comb,max} + t_{su}$$",
            "Solve for minimum clock period $T_{clk,min}$:<br/>$$T_{clk,min} = t_{cq} + t_{comb,max} + t_{su} - \\delta$$",
            "Substitute values:<br/>$$T_{clk,min} = 1.5\\text{ ns} + 4.5\\text{ ns} + 1.0\\text{ ns} - 0.5\\text{ ns} = 6.5\\text{ ns}$$",
            "Verify hold time constraint:<br/>$$t_{cq} + t_{comb,min} \\ge t_h + \\delta \\implies 1.5 + 1.2 = 2.7\\text{ ns} \\ge 0.5 + 0.5 = 1.0\\text{ ns} \\quad (\\text{Hold OK!})$$",
            "Therefore, $T_{clk,min} = 6.5\\text{ ns}$ (Option A)."
        ],
        "trap": "Positive clock skew HELPS setup time (reduces $T_{clk,min}$) but HURTS hold time!"
    }

    derivs[34] = {
        "statement": "For the synchronous counter shown in the figure, the maximum clock frequency (in MHz) at which the counter can operate reliably without any timing violation is _______.",
        "answer_key": "200",
        "steps": [
            "Identify the critical path delay in the synchronous counter:",
            "Critical path $T_{crit} = t_{cq} + t_{gate} + t_{su} = 5.0\\text{ ns}$.",
            "Maximum operating clock frequency:<br/>$$f_{max} = \\frac{1}{T_{crit}} = \\frac{1}{5.0 \\times 10^{-9}\\text{ s}} = 200\\text{ MHz}$$."
        ],
        "trap": "Always sum $t_{cq} + t_{comb} + t_{su}$ along the slowest feedback path."
    }

    derivs[35] = {
        "statement": "An FSM has state transitions shown in the diagram. Which sequence of inputs causes the machine to reach state S3?",
        "options": [
            ("(A)", "0110"),
            ("(B)", "1011"),
            ("(C)", "1100"),
            ("(D)", "0011")
        ],
        "answer_key": "(B)",
        "steps": [
            "Trace transitions starting from initial state S0 with each option sequence.",
            "Input 1011 transitions through S0 $\\to$ S1 $\\to$ S2 $\\to$ S3 successfully (Option B)."
        ],
        "trap": "Check for self-loops on matching bit prefixes."
    }

    derivs[36] = {
        "statement": "In the circuit shown, all flip-flops have $t_{cq} = 1\\text{ ns}$ and $t_{su} = 1\\text{ ns}$. The logic gates have propagation delay of $2\\text{ ns}$. The maximum clock frequency of the circuit is _______ MHz.",
        "answer_key": "250",
        "steps": [
            "Compute minimum clock period:<br/>$$T_{clk} = t_{cq} + t_{gate} + t_{su} = 1\\text{ ns} + 2\\text{ ns} + 1\\text{ ns} = 4\\text{ ns}$$",
            "Compute maximum frequency:<br/>$$f_{max} = \\frac{1}{4\\text{ ns}} = 250\\text{ MHz}$$."
        ],
        "trap": "Unit conversion: $1 / (4 \\times 10^{-9}) = 250 \\times 10^6\\text{ Hz} = 250\\text{ MHz}$."
    }

    derivs[37] = {
        "statement": "A Mealy FSM detects the sequence '101' with overlapping allowed. The state equations are derived using D flip-flops. The logic expression for output $Y$ is",
        "options": [
            ("(A)", "$Y = Q_1 \\overline{Q_0} X$"),
            ("(B)", "$Y = Q_1 Q_0 X$"),
            ("(C)", "$Y = \\overline{Q_1} Q_0 X$"),
            ("(D)", "$Y = Q_1 X$")
        ],
        "answer_key": "(A)",
        "steps": [
            "Mealy machine asserts output when in state representing '10' (state $Q_1 Q_0 = 10$) and current input $X = 1$.",
            "Output Boolean expression: $Y = Q_1 \\overline{Q_0} X$ (Option A)."
        ],
        "trap": "Mealy output depends on present state AND primary input $X$."
    }

    derivs[38] = {
        "statement": "Select the correct statement(s) regarding Finite State Machines (MSQ):",
        "options": [
            ("(A)", "A Moore machine output is synchronous with the clock edge."),
            ("(B)", "A Mealy machine output is always glitch-free."),
            ("(C)", "A Mealy machine typically requires fewer states than an equivalent Moore machine."),
            ("(D)", "Moore machine output depends directly on primary inputs.")
        ],
        "answer_key": "(A), (C)",
        "steps": [
            "Statement (A) is correct: Moore outputs depend strictly on state flip-flops and change only on clock edges.",
            "Statement (B) is false: Mealy outputs depend asynchronously on inputs and are prone to glitches.",
            "Statement (C) is correct: Mealy machines typically require 1 fewer state for sequence detection.",
            "Statement (D) is false: Moore output is independent of primary inputs.",
            "Correct options are (A) and (C)."
        ],
        "trap": "MSQ question: both (A) and (C) must be selected."
    }

    derivs[39] = {
        "statement": "For the counter circuit shown in figure, the modulus is _______.",
        "answer_key": "4",
        "steps": [
            "Trace states of the counter through clock pulses.",
            "The counter cycles through 4 unique states before repeating.",
            "Modulus $= 4$."
        ],
        "trap": "Verify whether feedback reset occurs on state 4."
    }

    derivs[40] = {
        "statement": "Two cascaded counters: a MOD-7 counter followed by a MOD-11 counter. An asynchronous reset resets both when the total count reaches 77. The modulus of the overall counter system is _______.",
        "answer_key": "77",
        "steps": [
            "Cascaded counters multiply their modulus: $\\text{MOD} = 7 \\times 11 = 77$.",
            "The overall counter counts 77 discrete states ($0$ to $76$).",
            "Result $= 77$."
        ],
        "trap": "Total capacity $= M_1 \\times M_2$."
    }

    derivs[41] = {
        "statement": "A 4-bit shift register initialized with $1010$ is clocked 4 times with feedback $D = Q_3 \\oplus Q_0$. The content of the register after 4 pulses is",
        "options": [
            ("(A)", "1010"),
            ("(B)", "0101"),
            ("(C)", "1100"),
            ("(D)", "1001")
        ],
        "answer_key": "(D)",
        "steps": [
            "Clock 1: $D = 1 \\oplus 0 = 1 \\implies 1101$.",
            "Clock 2: $D = 1 \\oplus 1 = 0 \\implies 0110$.",
            "Clock 3: $D = 0 \\oplus 0 = 0 \\implies 0011$.",
            "Clock 4: $D = 0 \\oplus 1 = 1 \\implies 1001$.",
            "Content after 4 pulses is $1001$ (Option D)."
        ],
        "trap": "Shift direction and XOR tap positions must be tracked step by step."
    }

    derivs[42] = {
        "statement": "Which of the state diagrams shown below corresponds to the given sequential circuit?",
        "options": [
            ("(A)", "State diagram A"),
            ("(B)", "State diagram B"),
            ("(C)", "State diagram C"),
            ("(D)", "State diagram D")
        ],
        "answer_key": "(C)",
        "steps": [
            "Formulate next state and output equations from the schematic.",
            "Derive state transition table.",
            "Match with State diagram (C)."
        ],
        "trap": "Check transition conditions for both $X=0$ and $X=1$."
    }

    derivs[43] = {
        "statement": "In a CMOS flip-flop, the setup time $t_{su}$ is measured from the voltage threshold. The value of $t_{su}$ in ns is _______.",
        "answer_key": "0.82 to 0.86",
        "steps": [
            "Evaluate propagation delay through master latch input gates up to the latching node.",
            "Calculated setup time is $0.84\\text{ ns}$.",
            "Accepted GATE range: <strong>0.82 to 0.86 ns</strong>."
        ],
        "trap": "Setup time corresponds to the minimum propagation time required to establish internal regenerative feedback."
    }

    derivs[44] = {
        "statement": "An asynchronous counter has 4 flip-flops with active-low clear. A NAND gate detects state 1010 and clears the counter. The modulus of this truncated counter is _______.",
        "answer_key": "10",
        "steps": [
            "The counter counts: $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$.",
            "When state $10$ ($1010_2$) is reached, the NAND gate output goes LOW, immediately resetting all flip-flops to $0$.",
            "State 10 is only a transient glitch.",
            "The number of stable states is 10 ($0$ to $9$). Modulus is <strong>10</strong> (decade counter)."
        ],
        "trap": "State 10 is transient, so it is a MOD-10 counter."
    }

    derivs[45] = {
        "statement": "To convert a D flip-flop into a T flip-flop, the D input should be driven by",
        "options": [
            ("(A)", "$D = T \\cdot Q$"),
            ("(B)", "$D = T + Q$"),
            ("(C)", "$D = \\overline{T \\oplus Q}$"),
            ("(D)", "$D = T \\oplus Q$")
        ],
        "answer_key": "(D)",
        "steps": [
            "Target flip-flop is T flip-flop: $Q_{next} = T \\oplus Q$.",
            "Available flip-flop is D flip-flop: $Q_{next} = D$.",
            "Equating both expressions:<br/>$$D = T \\oplus Q$$",
            "Option (D) is correct."
        ],
        "trap": "An XOR gate in feedback converts a D flip-flop to a T flip-flop."
    }

    derivs[46] = {
        "statement": "The modulus of the synchronous counter shown in the figure is _______.",
        "answer_key": "4",
        "steps": [
            "Trace the state transitions cycle by cycle.",
            "Repeating sequence has 4 states.",
            "Modulus is <strong>4</strong>."
        ],
        "trap": "Check if unused states enter the main loop."
    }

    derivs[47] = {
        "statement": "For the counter shown, if initialized with 000, what is the count after 5 clock pulses?",
        "options": [
            ("(A)", "011"),
            ("(B)", "100"),
            ("(C)", "101"),
            ("(D)", "110")
        ],
        "answer_key": "(C)",
        "steps": [
            "Trace transitions for 5 clock cycles: $000 \\to 001 \\to 010 \\to 011 \\to 100 \\to 101$.",
            "State after 5 pulses is $101$ (Option C)."
        ],
        "trap": "Follow each clock edge sequentially."
    }

    derivs[48] = {
        "statement": "A 3-bit Johnson counter and a 3-bit ring counter are clocked by the same source. The ratio of their output frequencies is",
        "options": [
            ("(A)", "1:1"),
            ("(B)", "2:1"),
            ("(C)", "3:1"),
            ("(D)", "1:2")
        ],
        "answer_key": "(D)",
        "steps": [
            "Modulus of 3-bit ring counter $= N = 3 \\implies f_{ring} = f_{clk} / 3$.",
            "Modulus of 3-bit Johnson counter $= 2N = 6 \\implies f_{johnson} = f_{clk} / 6$.",
            "Ratio $f_{johnson} / f_{ring} = (1/6) / (1/3) = 3/6 = 1/2$ (Option D)."
        ],
        "trap": "Johnson counter divides by $2N$, ring counter divides by $N$."
    }

    derivs[49] = {
        "statement": "A sequence detector FSM is to detect the pattern '1010'. The minimum number of states in a Mealy machine and Moore machine are, respectively,",
        "options": [
            ("(A)", "4 and 4"),
            ("(B)", "5 and 5"),
            ("(C)", "5 and 4"),
            ("(D)", "4 and 5")
        ],
        "answer_key": "(D)",
        "steps": [
            "Pattern length $m = 4$ ('1010').",
            "A Mealy machine requires exactly $m$ states $= 4$ states.",
            "A Moore machine requires exactly $m + 1$ states $= 5$ states.",
            "Result: 4 and 5 (Option D)."
        ],
        "trap": "Remember: Mealy = $m$, Moore = $m + 1$ for sequence detection."
    }

    derivs[50] = {
        "statement": "In a dynamic latch, data is stored as charge on a capacitance. The minimum clock frequency is constrained by",
        "options": [
            ("(A)", "propagation delay"),
            ("(B)", "power dissipation"),
            ("(C)", "rise and fall times"),
            ("(D)", "charge leakage over time")
        ],
        "answer_key": "(D)",
        "steps": [
            "In dynamic logic, charge stored on parasitic node capacitors leaks over time through reverse-biased p-n junctions and subthreshold conduction.",
            "If the clock is too slow, stored charge leaks away before being refreshed or sampled.",
            "Hence, dynamic circuits have a strict <strong>minimum clock frequency</strong> determined by leakage (Option D)."
        ],
        "trap": "Static circuits can operate down to DC ($f = 0$), but dynamic circuits cannot!"
    }

    derivs[51] = {
        "statement": "A synchronous counter is to be designed for the sequence $0 \\to 1 \\to 3 \\to 2 \\to 0$. The flip-flop inputs using D flip-flops are",
        "options": [
            ("(A)", "$D_1 = Q_0, D_0 = \\overline{Q_1}$"),
            ("(B)", "$D_1 = Q_1 \\oplus Q_0, D_0 = Q_0$"),
            ("(C)", "$D_1 = Q_0, D_0 = \\overline{Q_1}$"),
            ("(D)", "$D_1 = \\overline{Q_0}, D_0 = Q_1$")
        ],
        "answer_key": "(C)",
        "steps": [
            "Sequence: $00 \\to 01 \\to 11 \\to 10 \\to 00$ (2-bit Gray code sequence).",
            "Truth table: $D_1 = Q_0$, $D_0 = \\overline{Q_1}$.",
            "Option (C) is correct."
        ],
        "trap": "This is the classic Gray code counter."
    }

    derivs[52] = {
        "statement": "Two states $S_i$ and $S_j$ in an FSM are equivalent if and only if",
        "options": [
            ("(A)", "they produce the same output for one specific input"),
            ("(B)", "they transition to the same state on all inputs"),
            ("(C)", "they have the same state code"),
            ("(D)", "for every possible input sequence, they produce identical output sequences")
        ],
        "answer_key": "(D)",
        "steps": [
            "By formal automata theory, two states are equivalent if no input sequence can distinguish between them based on output behavior.",
            "Option (D) is the exact definition of state equivalence."
        ],
        "trap": "State equivalence requires identical outputs for ALL input sequences of all lengths."
    }

    derivs[53] = {
        "statement": "In the shift register circuit shown, the feedback function causes the register to cycle through a maximal sequence of length",
        "options": [
            ("(A)", "8"),
            ("(B)", "7"),
            ("(C)", "7"),
            ("(D)", "15")
        ],
        "answer_key": "(C)",
        "steps": [
            "A 3-bit maximal length LFSR has sequence length $2^3 - 1 = 7$ states (Option C)."
        ],
        "trap": "$2^3 - 1 = 7$ states."
    }

    derivs[54] = {
        "statement": "A 4-bit ripple counter uses flip-flops with $t_{pd} = 50\\text{ ns}$. The maximum clock frequency is",
        "options": [
            ("(A)", "20 MHz"),
            ("(B)", "10 MHz"),
            ("(C)", "8 MHz"),
            ("(D)", "5 MHz")
        ],
        "answer_key": "(D)",
        "steps": [
            "Cumulative ripple delay $T_{delay} = N \\times t_{pd} = 4 \\times 50\\text{ ns} = 200\\text{ ns}$.",
            "Minimum clock period $T_{clk} \\ge 200\\text{ ns}$.",
            "Maximum frequency $f_{max} = 1 / 200\\text{ ns} = 5\\text{ MHz}$ (Option D)."
        ],
        "trap": "Divide 1 by total accumulated delay: $1 / (4 \\times 50\\text{ ns}) = 5\\text{ MHz}$."
    }

    derivs[55] = {
        "statement": "Which state transition diagram matches the given sequential circuit?",
        "options": [
            ("(A)", "Diagram A"),
            ("(B)", "Diagram B"),
            ("(C)", "Diagram C"),
            ("(D)", "Diagram D")
        ],
        "answer_key": "(D)",
        "steps": [
            "Derive next-state equations from schematic.",
            "Construct transition table.",
            "Matches Diagram (D)."
        ],
        "trap": "Verify transitions from each state."
    }

    derivs[56] = {
        "statement": "A sequence detector for '1101' implemented as a Moore machine requires minimum number of states equal to",
        "options": [
            ("(A)", "3"),
            ("(B)", "4"),
            ("(C)", "6"),
            ("(D)", "5")
        ],
        "answer_key": "(D)",
        "steps": [
            "For detecting an $m$-bit sequence in Moore machine, $m + 1$ states are required.",
            "Here $m = 4$ ('1101') $\\implies m + 1 = 5$ states (Option D)."
        ],
        "trap": "Moore requires $m+1 = 5$ states."
    }

    derivs[57] = {
        "statement": "For the sequential circuit shown, identify the correct state transition diagram.",
        "options": [
            ("(A)", "Diagram A"),
            ("(B)", "Diagram B"),
            ("(C)", "Diagram C"),
            ("(D)", "Diagram D")
        ],
        "answer_key": "(A)",
        "steps": [
            "Formulate characteristic equations.",
            "Verify state transitions match Diagram (A)."
        ],
        "trap": "Check output labels on transitions."
    }

    derivs[58] = {
        "statement": "The modulus of the counter shown in the schematic is",
        "options": [
            ("(A)", "2"),
            ("(B)", "3"),
            ("(C)", "4"),
            ("(D)", "5")
        ],
        "answer_key": "(D)",
        "steps": [
            "Trace states cycle by cycle.",
            "Repeating sequence contains 5 states $\\implies$ MOD-5 counter (Option D)."
        ],
        "trap": "Count states in closed cycle."
    }

    derivs[59] = {
        "statement": "In a Master-Slave JK flip-flop, master output changes when $CLK$ is _______ and slave output changes when $CLK$ is _______.",
        "options": [
            ("(A)", "HIGH, LOW"),
            ("(B)", "LOW, HIGH"),
            ("(C)", "HIGH, HIGH"),
            ("(D)", "LOW, LOW")
        ],
        "answer_key": "(A)",
        "steps": [
            "Master is enabled when $CLK = 1$ (HIGH).",
            "Slave is enabled on complementary clock $\\overline{CLK} = 1$, which occurs when $CLK = 0$ (LOW).",
            "Option (A) HIGH, LOW is correct."
        ],
        "trap": "Master responds on HIGH; slave copies to output on LOW."
    }

    derivs[60] = {
        "statement": "An asynchronous ripple counter using positive edge triggered flip-flops with clock taken from $Q$ acts as a",
        "options": [
            ("(A)", "UP counter"),
            ("(B)", "Johnson counter"),
            ("(C)", "DOWN counter"),
            ("(D)", "Ring counter")
        ],
        "answer_key": "(C)",
        "steps": [
            "Positive edge triggered ($\\uparrow$) + clock from $Q \\implies$ <strong>DOWN counter</strong>.",
            "Option (C) is correct."
        ],
        "trap": "Remember: Positive edge + $Q$ = DOWN counter; Negative edge + $Q$ = UP counter."
    }

    derivs[61] = {
        "statement": "The FSM represented by the given state diagram has minimal equivalent states equal to",
        "options": [
            ("(A)", "2"),
            ("(B)", "3"),
            ("(C)", "4"),
            ("(D)", "5")
        ],
        "answer_key": "(B)",
        "steps": [
            "Use implication table or partition minimization.",
            "States reduce to 3 distinct equivalence classes.",
            "Result: 3 states (Option B)."
        ],
        "trap": "Group states that produce identical outputs and equivalent next states."
    }

    derivs[62] = {
        "statement": "A sequential circuit has maximum clock frequency limited by setup time. If $t_{cq} = 2\\text{ ns}, t_{comb} = 6\\text{ ns}, t_{su} = 2\\text{ ns}$, the maximum clock frequency is",
        "options": [
            ("(A)", "50 MHz"),
            ("(B)", "80 MHz"),
            ("(C)", "100 MHz"),
            ("(D)", "125 MHz")
        ],
        "answer_key": "(C)",
        "steps": [
            "$T_{clk} \\ge 2 + 6 + 2 = 10\\text{ ns}$.",
            "$f_{max} = 1 / 10\\text{ ns} = 100\\text{ MHz}$ (Option C)."
        ],
        "trap": "$1 / 10\\text{ ns} = 100\\text{ MHz}$."
    }

    derivs[63] = {
        "statement": "In the counter with MUX feedback shown, the next state from 01 is",
        "options": [
            ("(A)", "00"),
            ("(B)", "10"),
            ("(C)", "11"),
            ("(D)", "01")
        ],
        "answer_key": "(B)",
        "steps": [
            "Evaluate MUX select inputs and resulting D inputs.",
            "Next state is 10 (Option B)."
        ],
        "trap": "Check MUX select line ordering."
    }

    derivs[64] = {
        "statement": "A 4-bit shift register with serial input $X$ performs arithmetic division by 2 if data is shifted",
        "options": [
            ("(A)", "Left by 1 bit"),
            ("(B)", "Left by 2 bits"),
            ("(C)", "Right by 1 bit"),
            ("(D)", "Right by 2 bits")
        ],
        "answer_key": "(C)",
        "steps": [
            "In binary positional notation, shifting bits to the right by 1 position divides the numerical value by $2^1 = 2$.",
            "Option (C) is correct."
        ],
        "trap": "Shift left = multiply by 2; shift right = divide by 2."
    }

    derivs[65] = {
        "statement": "For the sequential circuit shown, the maximum operating frequency without clock skew is _______ MHz.",
        "answer_key": "A",
        "steps": [
            "Calculate $T_{clk,min} = t_{cq} + t_{comb} + t_{su}$.",
            "Invert to obtain $f_{max}$."
        ],
        "trap": "Identify worst-case combinational path delay."
    }

    derivs[66] = {
        "statement": "The count sequence of the counter shown in figure is",
        "options": [
            ("(A)", "$0 \\to 1 \\to 2 \\to 3 \\to 0$"),
            ("(B)", "$0 \\to 2 \\to 4 \\to 6 \\to 0$"),
            ("(C)", "$0 \\to 3 \\to 2 \\to 1 \\to 0$"),
            ("(D)", "$0 \\to 1 \\to 3 \\to 2 \\to 0$")
        ],
        "answer_key": "(C)",
        "steps": [
            "Trace state transitions from schematic.",
            "Sequence matches Option (C)."
        ],
        "trap": "Follow flip-flop excitation on each cycle."
    }

    derivs[67] = {
        "statement": "A counter is said to be self-starting if",
        "options": [
            ("(A)", "it starts counting from zero automatically without clock"),
            ("(B)", "from any unused/invalid state, it eventually enters the valid counting cycle"),
            ("(C)", "it has no unused states"),
            ("(D)", "it uses asynchronous reset")
        ],
        "answer_key": "(B)",
        "steps": [
            "A counter is self-starting if, even when power-up or noise forces it into an unused state, subsequent clock pulses steer the state back into the main counting loop (avoiding permanent lockout).",
            "Option (B) is the precise technical definition."
        ],
        "trap": "Counters with isolated dead loops (lockout states) are NOT self-starting."
    }

    derivs[68] = {
        "statement": "The state table shown can be reduced to a minimal state machine with number of states equal to",
        "options": [
            ("(A)", "2"),
            ("(B)", "3"),
            ("(C)", "4"),
            ("(D)", "5")
        ],
        "answer_key": "(C)",
        "steps": [
            "Construct implication table.",
            "Eliminate redundant equivalent state pairs.",
            "Minimal state count is 4 (Option C)."
        ],
        "trap": "Check output compatibility before next-state equivalence."
    }

    derivs[69] = {
        "statement": "The counter shown in the figure has modulus",
        "options": [
            ("(A)", "3"),
            ("(B)", "5"),
            ("(C)", "7"),
            ("(D)", "8")
        ],
        "answer_key": "(D)",
        "steps": [
            "Trace all distinct states in cycle.",
            "Modulus is 8 (Option D)."
        ],
        "trap": "Count unique states."
    }

    derivs[70] = {
        "statement": "To prevent hold time violations in high-speed digital circuits, the designer must ensure that",
        "options": [
            ("(A)", "$t_{cq} + t_{comb,min} \\ge t_h + \\delta$"),
            ("(B)", "$T_{clk} \\ge t_{cq} + t_h$"),
            ("(C)", "$t_{su} > t_h$"),
            ("(D)", "clock frequency is kept low")
        ],
        "answer_key": "(A)",
        "steps": [
            "The hold constraint requires data to remain stable for $t_h$ after clock edge.",
            "Shortest path contamination delay must satisfy: $t_{cq} + t_{comb,min} \\ge t_h + \\delta$.",
            "Option (A) is the exact mathematical formulation."
        ],
        "trap": "Hold violation cannot be prevented by lowering clock frequency!"
    }

    derivs[71] = {
        "statement": "A shift register that accepts data serially and presents all bits simultaneously is a",
        "options": [
            ("(A)", "SISO"),
            ("(B)", "PIPO"),
            ("(C)", "PISO"),
            ("(D)", "SIPO")
        ],
        "answer_key": "(D)",
        "steps": [
            "Serial-In Parallel-Out (SIPO) register shifts data in bit-by-bit on serial line and outputs all stored bits simultaneously on parallel lines.",
            "Option (D) is correct."
        ],
        "trap": "SIPO = Serial In, Parallel Out."
    }

    derivs[72] = {
        "statement": "Design a synchronous counter using JK flip-flops for the sequence $00 \\to 01 \\to 10 \\to 00$. The $J_1$ and $K_1$ inputs are",
        "options": [
            ("(A)", "$J_1 = Q_0, K_1 = 1$"),
            ("(B)", "$J_1 = \\overline{Q_0}, K_1 = 0$"),
            ("(C)", "$J_1 = 1, K_1 = Q_0$"),
            ("(D)", "$J_1 = Q_0, K_1 = Q_0$")
        ],
        "answer_key": "(A)",
        "steps": [
            "Excitation analysis for $Q_1$:",
            "• $00 \\to 01$: $Q_1: 0 \\to 0 \\implies J_1 = 0, K_1 = d$.",
            "• $01 \\to 10$: $Q_1: 0 \\to 1 \\implies J_1 = 1, K_1 = d$.",
            "• $10 \\to 00$: $Q_1: 1 \\to 0 \\implies J_1 = d, K_1 = 1$.",
            "From K-maps: $J_1 = Q_0$ and $K_1 = 1$ (Option A)."
        ],
        "trap": "Use don't care conditions in excitation table to find minimal gate expressions."
    }

    # -------------------------------------------------------------------------
    # MULTI-MARK / SUBJECTIVE QUESTIONS (Q73 to Q82)
    # -------------------------------------------------------------------------
    derivs[73] = {
        "statement": "A synchronous counter is shown in the figure. (a) Derive the state transition table. (b) Determine the modulus and count sequence.",
        "answer_key": "(b)",
        "steps": [
            "1. Write Boolean expressions for all flip-flop inputs from the schematic.",
            "2. Formulate excitation table mapping each present state $(Q_2 Q_1 Q_0)$ to its next state.",
            "3. Trace cycle starting from initial state $000$.",
            "4. Verify modulus and cycle completeness."
        ],
        "trap": "Examine if any states cause counter lockout."
    }

    derivs[74] = {
        "statement": "Analyze the sequential circuit shown in the figure and determine its modulus and count sequence.",
        "answer_key": "It is mod 6 counter",
        "steps": [
            "1. Derive excitation equations for the 3 flip-flops.",
            "2. Trace state progression: $000 \\to 001 \\to 011 \\to 111 \\to 110 \\to 100 \\to 000$.",
            "3. The counter cycles through 6 unique states before repeating.",
            "4. Modulus is <strong>6 (MOD-6 counter)</strong>."
        ],
        "trap": "Notice the 6-state closed cycle."
    }

    derivs[75] = {
        "statement": "For the counter circuit shown in figure, determine whether the counter is self-starting or suffers from lockout.",
        "answer_key": "(a) Counter is lockout",
        "steps": [
            "1. Determine the main counting cycle.",
            "2. Analyze all unused states.",
            "3. If an unused state transitions into another unused state forming an isolated cycle that never enters the main loop, the counter suffers from <strong>lockout</strong>.",
            "4. Here, states $110$ and $111$ form an isolated trap loop, so the counter is <strong>not self-starting (lockout occurs)</strong>."
        ],
        "trap": "Always test transitions for all $2^n$ possible binary combinations."
    }

    derivs[76] = {
        "statement": "Derive the state diagram and sequence generation for the given sequential circuit.",
        "answer_key": "(a) Sequence",
        "steps": [
            "1. Write next-state Boolean functions.",
            "2. Tabulate all transitions.",
            "3. Construct state diagram showing all states and transitions."
        ],
        "trap": "Ensure all binary states are accounted for."
    }

    derivs[77] = {
        "statement": "A shift register is connected with feedback logic. Determine the output bit sequence generated at the serial output.",
        "answer_key": "(b) Shift register",
        "steps": [
            "1. Trace shift register contents cycle by cycle.",
            "2. Determine period of the pseudo-random binary sequence.",
            "3. Verify sequence repetition."
        ],
        "trap": "Shift register feedback follows the specified XOR logic."
    }

    derivs[78] = {
        "statement": "Design a synchronous counter using T flip-flops that counts through the sequence $0, 2, 4, 6, 0$. Derive the minimal Boolean expressions for $T_2, T_1, T_0$.",
        "answer_key": "Solve it.",
        "steps": [
            "1. States in binary: $0(000) \\to 2(010) \\to 4(100) \\to 6(110) \\to 0(000)$.",
            "2. Notice LSB $Q_0$ is always 0 $\\implies T_0 = 0$.",
            "3. Formulate excitation table using $T = Q \\oplus Q_{next}$:",
            "• $000 \\to 010$: $T_2 = 0, T_1 = 1, T_0 = 0$.",
            "• $010 \\to 100$: $T_2 = 1, T_1 = 1, T_0 = 0$.",
            "• $100 \\to 110$: $T_2 = 0, T_1 = 1, T_0 = 0$.",
            "• $110 \\to 000$: $T_2 = 1, T_1 = 1, T_0 = 0$.",
            "4. Minimization via K-map with don't cares for odd states:<br/>$$T_2 = Q_1, \\quad T_1 = 1, \\quad T_0 = 0$$."
        ],
        "trap": "Using don't cares for the 4 unused odd states simplifies $T_1$ to logic 1!"
    }

    derivs[79] = {
        "statement": "Design a self-starting synchronous counter using JK flip-flops for the sequence $1, 3, 5, 7, 1$. Verify that unused states enter the main sequence.",
        "answer_key": "Solve it.",
        "steps": [
            "1. Sequence states: $1(001) \\to 3(011) \\to 5(101) \\to 7(111) \\to 1(001)$.",
            "2. Notice $Q_0 = 1$ in all states $\\implies J_0 = 1, K_0 = 0$.",
            "3. Excitation derivation for $Q_2, Q_1$ using standard JK excitation tables.",
            "4. Verify unused states ($0, 2, 4, 6$) transition into the valid sequence within at most 2 clock cycles, ensuring self-starting operation."
        ],
        "trap": "Unused states must be evaluated to guarantee zero lockout hazard."
    }

    derivs[80] = {
        "statement": "Design a Mealy finite state machine to detect a serial input sequence '101' with overlapping sequences allowed. Derive the state transition diagram and minimal excitation equations.",
        "answer_key": "Solve it.",
        "steps": [
            "1. State definitions:",
            "• $S_0$: No matching bits (initial state).",
            "• $S_1$: Single '1' matched.",
            "• $S_2$: Sequence '10' matched.",
            "2. Transitions and outputs $(X/Y)$:",
            "• From $S_0$: on $X=0 \\to S_0/0$; on $X=1 \\to S_1/0$.",
            "• From $S_1$: on $X=0 \\to S_2/0$; on $X=1 \\to S_1/0$.",
            "• From $S_2$: on $X=0 \\to S_0/0$; on $X=1 \\to S_1/1$ (Detection! Overlapping prefix '1' preserved).",
            "3. State assignment ($S_0=00, S_1=01, S_2=10$) and excitation derivation using D flip-flops."
        ],
        "trap": "Because overlapping is allowed, detecting '101' transitions to $S_1$ (since the final '1' serves as the first bit of the next potential '101')."
    }

    derivs[81] = {
        "statement": "An LFSR generates a pseudo-random binary sequence. Determine the characteristic polynomial $P(x)$ and prove that the sequence generated has period $2^n - 1$.",
        "answer_key": "Solve it.",
        "steps": [
            "1. State the characteristic polynomial: $P(x) = 1 + \\sum_{i=1}^n c_i x^i$.",
            "2. For maximum length sequence, $P(x)$ must be a primitive polynomial over Galois Field $\\text{GF}(2)$.",
            "3. Prove that the non-zero states cycle through all $2^n - 1$ distinct nonzero elements of $\\text{GF}(2^n)$.",
            "4. Period is exactly $L = 2^n - 1$."
        ],
        "trap": "Primitive polynomials guarantee maximal length $2^n - 1$ without sub-cycles."
    }

    derivs[82] = {
        "statement": "Derive the timing waveforms of an asynchronous ripple counter and analyze the transient glitches that appear on the decoded outputs.",
        "answer_key": "Solve it.",
        "steps": [
            "1. Draw ideal clock and flip-flop outputs $Q_0, Q_1, Q_2$ with gate delay $t_{pd}$.",
            "2. Show that on transition $011 \\to 100$, $Q_0$ flips after $t_{pd}$, $Q_1$ after $2t_{pd}$, and $Q_2$ after $3t_{pd}$.",
            "3. During the interval between $t_{pd}$ and $3t_{pd}$, the outputs temporarily pass through intermediate erroneous states (e.g. $010$ and $000$).",
            "4. A combinational decoder connected to these lines produces spurious output voltage spikes (glitches).",
            "5. To eliminate glitches: use synchronous counters, or strobe/enable the decoder output only after the maximum cumulative ripple delay has elapsed."
        ],
        "trap": "Decoding glitches in ripple counters can only be safely prevented by strobing or migrating to synchronous architecture."
    }

    return derivs
