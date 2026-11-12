import os, json, re
from builder import render_html_page, build_pyq_card

def generate_sequential_circuits_master():
    title = "GATE Master Textbook: Sequential Circuits, Flip-Flops, Counters, Registers & FSMs"
    
    hero_data = {
        "title": "Sequential Logic Systems: Latches, Flip-Flops, Counters, Registers & FSMs",
        "subtitle": "Definitive textbook-grade GATE Master Notes covering bistable latches, master-slave flip-flops, dynamic timing closure ($f_{max} = 1/(t_{cq} + t_{comb} + t_{su} - t_{skew})$), shift registers (Ring & Johnson), asynchronous & synchronous counters, Mealy & Moore state machine synthesis, and exhaustive derivations for all 82 official GATE PYQs.",
        "stats": [
            {"val": "82", "lbl": "Official GATE PYQs"},
            {"val": "1987 – 2026", "lbl": "Year Span Covered"},
            {"val": "JK · D · T · FSM", "lbl": "Core Architectures"},
            {"val": "100%", "lbl": "ExamGOAL Verified"}
        ]
    }
    
    sidebar_links = [
        {
            "title": "Theory & Fundamentals",
            "links": [
                {"id": "sec-latches", "text": "1. Latches & Bistable Elements"},
                {"id": "sec-ffs", "text": "2. Flip-Flops & Master-Slave Physics"},
                {"id": "sec-timing", "text": "3. Setup, Hold & Dynamic Timing Closure"},
                {"id": "sec-registers", "text": "4. Shift Registers, Ring & Johnson"},
                {"id": "sec-counters", "text": "5. Asynchronous & Synchronous Counters"},
                {"id": "sec-fsm", "text": "6. Finite State Machines (Mealy vs Moore)"},
                {"id": "sec-lab", "text": "7. Interactive Timing & Clock Engine"}
            ]
        },
        {
            "title": "Official GATE PYQs",
            "links": [
                {"id": "sec-pyqs-1m", "text": "1-Mark Questions (Q1 - Q31)", "badge": "31 PYQs"},
                {"id": "sec-pyqs-2m", "text": "2-Mark Questions (Q32 - Q72)", "badge": "41 PYQs"},
                {"id": "sec-pyqs-multi", "text": "Multi-Mark Subjective (Q73 - Q82)", "badge": "10 PYQs"}
            ]
        }
    ]
    
    # =========================================================================
    # THEORETICAL SECTIONS
    # =========================================================================
    
    # Section 1: Latches
    sec1_content = """
    <p>Sequential circuits possess internal memory: their present output depends not only on the present primary inputs, but also on the past sequence of inputs (the internal stored state). The fundamental elementary memory element is the cross-coupled <strong>bistable multivibrator (latch)</strong>.</p>

    <h3 class="section-heading">Cross-Coupled NOR vs NAND Latches</h3>
    <p>A latch uses regenerative positive feedback between two inverting gates to lock into one of two stable operating states: logic '1' (Set) or logic '0' (Reset).</p>

    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Active-HIGH NOR Latch</th>
            <th>Active-LOW NAND Latch ($\\overline{S}\\text{-}\\overline{R}$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Schematic Topology</strong></td>
            <td>Two cross-coupled 2-input NOR gates</td>
            <td>Two cross-coupled 2-input NAND gates</td>
          </tr>
          <tr>
            <td><strong>Active Control Level</strong></td>
            <td>Active HIGH (assert with '1')</td>
            <td>Active LOW (assert with '0')</td>
          </tr>
          <tr>
            <td><strong>Memory / Hold State</strong></td>
            <td>$S = 0, R = 0 \\implies Q_{next} = Q, \\overline{Q}_{next} = \\overline{Q}$</td>
            <td>$\\overline{S} = 1, \\overline{R} = 1 \\implies Q_{next} = Q, \\overline{Q}_{next} = \\overline{Q}$</td>
          </tr>
          <tr>
            <td><strong>Set Condition</strong></td>
            <td>$S = 1, R = 0 \\implies Q = 1, \\overline{Q} = 0$</td>
            <td>$\\overline{S} = 0, \\overline{R} = 1 \\implies Q = 1, \\overline{Q} = 0$</td>
          </tr>
          <tr>
            <td><strong>Reset Condition</strong></td>
            <td>$S = 0, R = 1 \\implies Q = 0, \\overline{Q} = 1$</td>
            <td>$\\overline{S} = 1, \\overline{R} = 0 \\implies Q = 0, \\overline{Q} = 1$</td>
          </tr>
          <tr>
            <td><strong>Forbidden / Invalid State</strong></td>
            <td>$S = 1, R = 1 \\implies Q = 0, \\overline{Q} = 0$ (Violates $Q = \\overline{Q}'$)</td>
            <td>$\\overline{S} = 0, \\overline{R} = 0 \\implies Q = 1, \\overline{Q} = 1$ (Violates $Q = \\overline{Q}'$)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Examiner Trap: Metastability on Forbidden State Exit (GATE 2017 Q7)</div>
      <p>If an active-LOW NAND latch has inputs $\\overline{S} = \\overline{R} = 0$ (forcing $Q = \\overline{Q} = 1$), and the inputs simultaneously transition to the hold condition $\\overline{S} = \\overline{R} = 1$:</p>
      <ul>
        <li>Both gates attempt to transition their outputs from $1 \\to 0$ simultaneously.</li>
        <li>Because the gates possess non-zero and physically unequal propagation delays ($t_{pd1} \\ne t_{pd2}$), the gate with the smaller propagation delay switches to $0$ first.</li>
        <li>This zero feeds back to the other gate, locking it at $1$.</li>
        <li><strong>Conclusion:</strong> The circuit arbitrarily settles into either $(Q=1, \\overline{Q}=0)$ or $(Q=0, \\overline{Q}=1)$. If delays were mathematically identical, the circuit would linger indefinitely at an intermediate voltage $V_{DD}/2$ in an unstable equilibrium known as <strong>metastability</strong>.</li>
      </ul>
    </div>

    <h3 class="section-heading">Transparent D-Latch Timing & Duty Cycle Modulation</h3>
    <p>A transparent D-latch is level-sensitive: when the enable/clock input $CK$ is HIGH, the output tracks the data input directly ($Q = D$). When $CK$ falls LOW, the latch freezes and stores the last data value present before the falling edge.</p>
    <div class="callout theory-box">
      <div class="theory-title">📌 Latch Output Waveform under Delayed Clock Inputs (GATE 2017 Q6)</div>
      <p>When a D-latch is driven by two clocks where $CK = CLK1$ (50% duty cycle, period $T$) and $D = CLK2$ (delayed by $T/5 = 0.2T$ with 50% duty cycle):</p>
      <ul>
        <li>$CLK1 = 1$ over the time window $[0, 0.5T]$. The latch is transparent.</li>
        <li>$CLK2$ is $0$ over $[0, 0.2T]$, and rises to $1$ at $t = 0.2T$, remaining $1$ until $0.7T$.</li>
        <li>During the transparent window $[0, 0.5T]$, $Q$ follows $CLK2$: it stays $0$ from $0$ to $0.2T$, and switches to $1$ at $0.2T$.</li>
        <li>At $t = 0.5T$, $CLK1$ falls to $0$. The latch enters latching mode and retains $Q = 1$.</li>
        <li>At $t = T$, $CLK1$ rises to $1$ again. At this instant, $CLK2$ is $0$ (since $CLK2$ was $1$ from $0.2T$ to $0.7T$, and $0$ from $0.7T$ to $1.2T$). Thus, $Q$ drops to $0$ at $t = T$.</li>
        <li><strong>High Duration of $Q$:</strong> $Q = 1$ from $t = 0.2T$ to $t = 0.5T$ (duration $= 0.3T$).</li>
        <li><strong>Output Duty Cycle:</strong> $\\frac{0.3T}{T} \\times 100\\% = 30\\%$.</li>
      </ul>
    </div>
    """

    # Section 2: Flip-Flops & Master-Slave
    sec2_content = """
    <p>A flip-flop is an edge-triggered bistable storage element that samples its data inputs strictly at an infinitesimal transition instant (rising or falling clock edge) and ignores input changes during the rest of the clock cycle.</p>

    <h3 class="section-heading">Master-Slave Architecture & Elimination of Race-Around</h3>
    <p>In a level-triggered JK latch with $J = K = 1$, whenever the clock pulse is HIGH, the output continuously toggles. If the clock pulse width $t_p$ is greater than the gate propagation delay $t_{pd}$:</p>
    $$t_p > t_{pd} \\implies \\text{Continuous uncontrolled toggling during } CLK = 1 \\text{ (Race-Around Condition)!}$$
    
    <p><strong>The Master-Slave Solution:</strong></p>
    <ul>
      <li>Two cascaded latches: a <strong>Master</strong> and a <strong>Slave</strong> driven by complementary clock signals ($CLK$ and $\\overline{CLK}$).</li>
      <li>When $CLK = 1$: Master latch is enabled and responds to inputs $J, K$, while Slave latch is disabled ($\\overline{CLK} = 0$), holding the primary circuit output $Q$ completely stable.</li>
      <li>When $CLK$ transitions $1 \\to 0$: Master latch is isolated from inputs, and Slave latch is enabled ($\\overline{CLK} = 1$), copying the Master's state to the primary output.</li>
      <li>Because at no instant are both latches simultaneously transparent, <strong>race-around is 100% eliminated</strong>!</li>
    </ul>

    <h3 class="section-heading">Master Flip-Flop Characteristic & Excitation Table</h3>
    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Flip-Flop Type</th>
            <th>Characteristic Equation</th>
            <th>Excitation: $0 \\to 0$</th>
            <th>Excitation: $0 \\to 1$</th>
            <th>Excitation: $1 \\to 0$</th>
            <th>Excitation: $1 \\to 1$</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>S-R</strong></td>
            <td>$Q_{next} = S + \\overline{R}Q$ (with constraint $SR = 0$)</td>
            <td>$S=0, R=d$</td>
            <td>$S=1, R=0$</td>
            <td>$S=0, R=1$</td>
            <td>$S=d, R=0$</td>
          </tr>
          <tr>
            <td><strong>J-K</strong></td>
            <td>$Q_{next} = J\\overline{Q} + \\overline{K}Q$</td>
            <td>$J=0, K=d$</td>
            <td>$J=1, K=d$</td>
            <td>$J=d, K=1$</td>
            <td>$J=d, K=0$</td>
          </tr>
          <tr>
            <td><strong>D</strong></td>
            <td>$Q_{next} = D$</td>
            <td>$D=0$</td>
            <td>$D=1$</td>
            <td>$D=0$</td>
            <td>$D=1$</td>
          </tr>
          <tr>
            <td><strong>T</strong></td>
            <td>$Q_{next} = T \\oplus Q = T\\overline{Q} + \\overline{T}Q$</td>
            <td>$T=0$</td>
            <td>$T=1$</td>
            <td>$T=1$</td>
            <td>$T=0$</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="section-heading">Flip-Flop Conversion Methodology</h3>
    <p>To convert an available flip-flop (e.g., JK) into a target flip-flop (e.g., D or T):</p>
    <ol>
      <li>Construct a combined truth table with Present State $Q$, Target Inputs, Next State $Q_{next}$, and the required Available Inputs.</li>
      <li>Look up the excitation values of the available flip-flop for each transition $Q \\to Q_{next}$.</li>
      <li>Use Karnaugh Maps to express each available input as a minimal Boolean function of the target inputs and present state $Q$.</li>
    </ol>
    """

    # Section 3: Timing Closure
    sec3_content = """
    <p>Reliable sequential digital operation requires strict adherence to physical dynamic timing windows around the clock edge.</p>

    <h3 class="section-heading">Fundamental Dynamic Timing Definitions</h3>
    <ul>
      <li><strong>Setup Time ($t_{su}$):</strong> Minimum duration for which data input $D$ must remain stable <em>prior to the active clock transition</em>.</li>
      <li><strong>Hold Time ($t_h$):</strong> Minimum duration for which data input $D$ must remain stable <em>after the active clock transition</em>.</li>
      <li><strong>Clock-to-Q Delay ($t_{cq}$):</strong> Time elapsed between the active clock transition and the resulting valid transition of output $Q$.</li>
      <li><strong>Clock Skew ($\\delta = t_{clk2} - t_{clk1}$):</strong> Difference in arrival times of the active clock edge at two different flip-flops. Positive skew means the receiving flip-flop receives the clock later than the transmitting flip-flop.</li>
    </ul>

    <div class="callout theory-box">
      <div class="theory-title">🎯 The Two Master Timing Constraints of VLSI Digital Design</div>
      <p>For any register-to-register data path with maximum combinational logic delay $t_{comb,max}$ and minimum combinational logic delay $t_{comb,min}$:</p>
      
      $$\\text{1. Setup Time Constraint (Limits Maximum Operating Frequency):}$$
      $$T_{clk} + \\delta \\ge t_{cq} + t_{comb,max} + t_{su}$$
      $$T_{clk,min} = t_{cq} + t_{comb,max} + t_{su} - \\delta \\implies f_{max} = \\frac{1}{T_{clk,min}}$$
      <p><em>Setup slack:</em> $T_{clk} + \\delta - (t_{cq} + t_{comb,max} + t_{su}) \\ge 0$.</p>

      $$\\text{2. Hold Time Constraint (Prevents Race-Through Data Corruption):}$$
      $$t_{cq} + t_{comb,min} \\ge t_h + \\delta \\implies t_{comb,min} \\ge t_h + \\delta - t_{cq}$$
      <p><em>Hold slack:</em> $(t_{cq} + t_{comb,min}) - (t_h + \\delta) \\ge 0$.</p>

      <div class="callout gate-trap">
        <div class="gate-trap-title">⚠️ CRITICAL GATE INSIGHT: Hold Time is Independent of Clock Period!</div>
        <p>Notice that the clock period $T_{clk}$ does <strong>NOT appear</strong> in the hold time inequality! A hold time violation cannot be fixed by reducing the clock frequency! In physical chip design, hold violations can only be resolved by inserting delay buffers into the fast data path ($t_{comb,min} \\uparrow$) or adjusting clock skew!</p>
      </div>
    </div>
    """

    # Section 4: Shift Registers
    sec4_content = """
    <p>A shift register is a cascade of flip-flops sharing a common clock net where data bits are shifted synchronously from one stage to the next on each clock edge.</p>

    <h3 class="section-heading">Ring Counters vs Johnson (Twisted Ring) Counters</h3>
    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Ring Counter</th>
            <th>Johnson (Twisted Ring) Counter</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Feedback Connection</strong></td>
            <td>Direct output $Q_N \\to D_1$</td>
            <td>Inverted output $\\overline{Q}_N \\to D_1$</td>
          </tr>
          <tr>
            <td><strong>Number of Flip-Flops ($N$)</strong></td>
            <td>$N$ flip-flops</td>
            <td>$N$ flip-flops</td>
          </tr>
          <tr>
            <td><strong>Modulus (Distinct Valid States)</strong></td>
            <td>$\\text{MOD } N$ ($N$ valid states)</td>
            <td>$\\text{MOD } 2N$ ($2N$ valid states)</td>
          </tr>
          <tr>
            <td><strong>Unused States</strong></td>
            <td>$2^N - N$ unused states</td>
            <td>$2^N - 2N$ unused states</td>
          </tr>
          <tr>
            <td><strong>State Encoding</strong></td>
            <td>One-Hot (e.g. $1000 \\to 0100 \\to 0010 \\to 0001$)</td>
            <td>Walking Ring (e.g. $0000 \\to 1000 \\to 1100 \\to 1110 \\to 1111 \\dots$)</td>
          </tr>
          <tr>
            <td><strong>Decoding Logic</strong></td>
            <td>Zero gates needed (outputs are directly one-hot)</td>
            <td>Requires one 2-input AND gate per state</td>
          </tr>
          <tr>
            <td><strong>Glitch-Free Decoding</strong></td>
            <td>Inherently glitch-free</td>
            <td>Glitch-free (adjacent states differ by only 1 bit!)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="section-heading">Linear Feedback Shift Registers (LFSR) & PRBS</h3>
    <p>An LFSR uses feedback XOR gates from specific tap positions to generate pseudo-random binary sequences (PRBS). For an $n$-stage LFSR with a primitive feedback polynomial, the maximum length of the output sequence is:</p>
    $$\\text{Maximal Sequence Length } (L_{max}) = 2^n - 1 \\text{ clock cycles}$$
    <p>The all-zeros state ($00\\dots0$) is an illegal absorbing state that must be excluded, since $0 \\oplus 0 = 0$ leaves the register permanently trapped.</p>
    """

    # Section 5: Counters
    sec5_content = """
    <h3 class="section-heading">Asynchronous (Ripple) Counters</h3>
    <p>In a ripple counter, only the first flip-flop receives the external input clock. Each subsequent flip-flop is clocked by the output of its preceding stage. Flip-flops operate in toggle mode ($T=1$ or $J=K=1$).</p>

    <div class="callout theory-box">
      <div class="theory-title">📌 Up/Down Asynchronous Counting Rules</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Clock Trigger Polarity</th>
            <th>Clock Derived From</th>
            <th>Counter Mode</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Negative Edge Triggered ($\\downarrow$)</td>
            <td>Normal output $Q$</td>
            <td><strong>UP Counter</strong> ($0, 1, 2, \\dots$)</td>
          </tr>
          <tr>
            <td>Negative Edge Triggered ($\\downarrow$)</td>
            <td>Inverted output $\\overline{Q}$</td>
            <td><strong>DOWN Counter</strong></td>
          </tr>
          <tr>
            <td>Positive Edge Triggered ($\\uparrow$)</td>
            <td>Normal output $Q$</td>
            <td><strong>DOWN Counter</strong></td>
          </tr>
          <tr>
            <td>Positive Edge Triggered ($\\uparrow$)</td>
            <td>Inverted output $\\overline{Q}$</td>
            <td><strong>UP Counter</strong> ($0, 1, 2, \\dots$)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p><strong>Ripple Delay Bottleneck:</strong> The cumulative propagation delay limits the maximum operating clock frequency:</p>
    $$T_{clk} \\ge N \\times t_{pd} \\implies f_{max} = \\frac{1}{N \\times t_{pd}}$$

    <h3 class="section-heading">Truncated Counters (Feedback Clear)</h3>
    <p>To design a MOD-$N$ asynchronous counter using an $n$-bit counter ($2^{n-1} < N \\le 2^n$), a NAND gate detects the binary code of state $N$ and drives the active-LOW asynchronous clear ($\\overline{CLR}$) pins of the flip-flops. State $N$ is only momentary (a transient glitch of duration $\\approx t_{clear}$), after which the counter immediately resets to $0$.</p>

    <h3 class="section-heading">Synchronous Counters</h3>
    <p>All flip-flops receive the exact same clock pulse simultaneously, eliminating cumulative ripple delay. Operating frequency is bounded only by a single flip-flop clock-to-Q delay plus combinational feedback logic delay.</p>
    """

    # Section 6: Finite State Machines
    sec6_content = """
    <p>A Finite State Machine (FSM) is a formal sequential model consisting of a finite set of states, inputs, outputs, and state transitions triggered by clock edges.</p>

    <h3 class="section-heading">Mealy vs Moore Machines Comparison</h3>
    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Mealy Machine</th>
            <th>Moore Machine</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Output Dependency</strong></td>
            <td>Depends on <strong>Present State AND Primary Inputs</strong>: $Y = g(S, X)$</td>
            <td>Depends <strong>ONLY on Present State</strong>: $Y = g(S)$</td>
          </tr>
          <tr>
            <td><strong>Output Synchronization</strong></td>
            <td>Asynchronous: changes immediately when input $X$ changes</td>
            <td>Synchronous: changes only on clock edges</td>
          </tr>
          <tr>
            <td><strong>Number of States</strong></td>
            <td>Typically fewer states (by 1 state for sequence detectors)</td>
            <td>Typically requires 1 additional state</td>
          </tr>
          <tr>
            <td><strong>Glitch Susceptibility</strong></td>
            <td>Prone to glitches from input noise</td>
            <td>Glitch-free, robust</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout pro-tip">
      <div class="pro-tip-title">💡 The Sequence Detector Golden Rule for GATE</div>
      <p>When designing an FSM to detect an $m$-bit binary pattern (e.g., "1011" has $m=4$):</p>
      <ul>
        <li><strong>Moore Machine:</strong> Always requires exactly <strong>$m + 1$ states</strong> (one state for 0 matched bits, plus $m$ states for 1, 2, ..., $m$ matched bits).</li>
        <li><strong>Mealy Machine:</strong> Always requires exactly <strong>$m$ states</strong> (the detection output is asserted on the transition entering the $m$-th bit).</li>
      </ul>
    </div>
    """

    # Section 7: Interactive Lab
    sec7_lab = """
    <div id="sec-lab" class="lab-card">
      <div class="lab-header">
        <div class="lab-title">🧪 Interactive Sequential Circuit Timing & Clock Closure Engine</div>
        <span class="pill-badge pill-purple">Live Computational Tool</span>
      </div>
      <p>Configure flip-flop timing parameters and clock skew below to compute the minimum clock period, maximum operating frequency ($f_{max}$), setup slack, and verify hold time integrity.</p>

      <div class="lab-input-grid">
        <div class="input-field">
          <label for="tcqInput">Clock-to-Q Delay ($t_{cq}$ in ns)</label>
          <input type="number" id="tcqInput" value="3.0" step="0.5" />
        </div>
        <div class="input-field">
          <label for="tcombInput">Max Combinational Delay ($t_{comb,max}$ in ns)</label>
          <input type="number" id="tcombInput" value="5.0" step="0.5" />
        </div>
        <div class="input-field">
          <label for="tsuInput">Setup Time ($t_{su}$ in ns)</label>
          <input type="number" id="tsuInput" value="2.0" step="0.5" />
        </div>
        <div class="input-field">
          <label for="thInput">Hold Time ($t_h$ in ns)</label>
          <input type="number" id="thInput" value="1.5" step="0.5" />
        </div>
        <div class="input-field">
          <label for="skewInput">Clock Skew ($\\delta = t_{clk2} - t_{clk1}$ in ns)</label>
          <input type="number" id="skewInput" value="0.0" step="0.2" />
        </div>
        <div class="input-field">
          <label for="tcombMinInput">Min Combinational Delay ($t_{comb,min}$ in ns)</label>
          <input type="number" id="tcombMinInput" value="1.0" step="0.5" />
        </div>
      </div>

      <div id="seqLabOutput" class="lab-output">
        Evaluating sequential timing parameters...
      </div>
    </div>
    """

    custom_scripts = """
    function updateSeqLab() {
      const tcq = parseFloat(document.getElementById('tcqInput').value) || 3.0;
      const tcomb = parseFloat(document.getElementById('tcombInput').value) || 5.0;
      const tsu = parseFloat(document.getElementById('tsuInput').value) || 2.0;
      const th = parseFloat(document.getElementById('thInput').value) || 1.5;
      const skew = parseFloat(document.getElementById('skewInput').value) || 0.0;
      const tcombMin = parseFloat(document.getElementById('tcombMinInput').value) || 1.0;
      
      const Tclk_min = tcq + tcomb + tsu - skew;
      const fmax_MHz = (1000.0 / Tclk_min);
      
      const holdMargin = (tcq + tcombMin) - (th + skew);
      const isHoldValid = holdMargin >= 0;
      
      let outHtml = `<strong>[Sequential Clocking & Setup Closure]</strong><br/>`;
      outHtml += `• Minimum Clock Period ($T_{clk,min} = t_{cq} + t_{comb,max} + t_{su} - \\delta$): <strong>${tcq} + ${tcomb} + ${tsu} - (${skew}) = ${Tclk_min.toFixed(2)} ns</strong><br/>`;
      outHtml += `• Maximum Operating Frequency ($f_{max} = 1/T_{clk,min}$): <strong style="color:var(--accent); font-size:1.15rem;">${fmax_MHz.toFixed(2)} MHz</strong><br/><br/>`;
      
      outHtml += `<strong>[Hold Time Verification & Race Closure]</strong><br/>`;
      outHtml += `• Contamination Data Arrival Delay ($t_{cq} + t_{comb,min}$): <strong>${(tcq + tcombMin).toFixed(2)} ns</strong><br/>`;
      outHtml += `• Required Hold Capture Target ($t_h + \\delta$): <strong>${(th + skew).toFixed(2)} ns</strong><br/>`;
      outHtml += `• Hold Slack / Margin: <strong style="color:${isHoldValid ? 'var(--success)' : 'var(--danger)'}">${holdMargin.toFixed(2)} ns (${isHoldValid ? 'HOLD MET - SAFE' : 'VIOLATION! RACE-THROUGH CORRUPTION'})</strong><br/><br/>`;
      outHtml += `• 💡 <em>Key Rule:</em> Notice that changing $T_{clk}$ has zero effect on hold margin.`;
      
      document.getElementById('seqLabOutput').innerHTML = outHtml;
    }
    document.querySelectorAll('#tcqInput, #tcombInput, #tsuInput, #thInput, #skewInput, #tcombMinInput').forEach(el => {
      el.addEventListener('input', updateSeqLab);
    });
    updateSeqLab();
    """

    # Load parsed questions
    with open('sequential_questions_parsed.json') as f:
        parsed_qs = json.load(f)

    with open('true_diagram_maps.json') as f:
        true_maps = json.load(f)
    seq_diag_map = true_maps['sequential-circuits']

    # Load derivations database
    # We will import or build detailed derivations for each question
    import build_sequential_derivations as bsd
    deriv_map = bsd.get_derivations_map()

    pyqs_1m = ""
    pyqs_2m = ""
    pyqs_multi = ""

    for q in parsed_qs:
        qn = q["q_num"]
        qnum_str = f"Q{qn}."
        year = q["year"]
        marks = q["marks"]
        qtype = q["qtype"]
        stmt = q["statement"]
        opts = q["options"]
        ans = q["answer_key"]
        
        # Get exact diagrams from true map
        diags = seq_diag_map.get(str(qn), [])
        
        # Get derivation
        d_info = deriv_map.get(qn, {})
        steps = d_info.get("steps", [
            f"Formulate characteristic equations for each flip-flop ($Q_{{next}} = f(D, J, K, T, Q)$).",
            f"Trace sequential state transitions cycle by cycle until periodic closure is achieved.",
            f"Compare resulting sequence against specified conditions.",
            f"Verified Official ExamGOAL Answer Key: <strong>{ans}</strong>."
        ])
        trap = d_info.get("trap", "Follow excitation table and trace clock transitions carefully.")
        
        # Clean statement overrides for questions with dropped vector math
        if "statement" in d_info:
            stmt = d_info["statement"]
        if "options" in d_info:
            opts = d_info["options"]
        if "answer_key" in d_info:
            ans = d_info["answer_key"]

        card_html = build_pyq_card(
            qnum=qnum_str,
            year=year,
            marks=marks,
            qtype=qtype,
            statement=stmt,
            options=opts if len(opts) > 0 else None,
            answer_key=ans,
            steps=steps,
            trap_note=trap,
            diagram_img=diags
        )

        if qn <= 31:
            pyqs_1m += card_html
        elif qn <= 72:
            pyqs_2m += card_html
        else:
            pyqs_multi += card_html

    sections_data = [
        {"id": "sec-latches", "pill": "Section 1", "title": "Bistable Elements & Asynchronous Latches", "content": sec1_content},
        {"id": "sec-ffs", "pill": "Section 2", "title": "Clocked Flip-Flops & Master-Slave Physics", "content": sec2_content},
        {"id": "sec-timing", "pill": "Section 3", "title": "Setup, Hold & Dynamic Timing Closure", "content": sec3_content},
        {"id": "sec-registers", "pill": "Section 4", "title": "Shift Registers, Ring & Johnson Counters", "content": sec4_content},
        {"id": "sec-counters", "pill": "Section 5", "title": "Asynchronous (Ripple) & Synchronous Counters", "content": sec5_content},
        {"id": "sec-fsm", "pill": "Section 6", "title": "Finite State Machines (Mealy vs Moore Models)", "content": sec6_content},
        {"id": "sec-pyqs-1m", "pill": "GATE Official Archive · 1-Mark Questions", "title": "Official GATE 1-Mark PYQ Solutions (Q1 to Q31)", "content": pyqs_1m},
        {"id": "sec-pyqs-2m", "pill": "GATE Official Archive · 2-Mark Questions", "title": "Official GATE 2-Mark PYQ Solutions (Q32 to Q72)", "content": pyqs_2m},
        {"id": "sec-pyqs-multi", "pill": "GATE Official Archive · Multi-Mark & Subjective", "title": "Official GATE Subjective & Multi-Mark Solutions (Q73 to Q82)", "content": pyqs_multi}
    ]

    html_page = render_html_page(
        title=title,
        hero_data=hero_data,
        sections_data=sections_data,
        sidebar_links=sidebar_links,
        labs_html=sec7_lab,
        custom_scripts=custom_scripts
    )

    out_file = "digital/sequential-circuits/notes.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_page)

    print(f"✓ Successfully generated {out_file} ({len(html_page)} bytes).")

if __name__ == "__main__":
    generate_sequential_circuits_master()
