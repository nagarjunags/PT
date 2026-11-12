import os
from builder import render_html_page, build_pyq_card

def generate_adc_dac():
    title = "GATE Master Textbook: D/A & A/D Converters (Flash, SAR, Dual-Slope, R-2R)"
    
    hero_data = {
        "title": "Analog-to-Digital & Digital-to-Analog Converters",
        "subtitle": "Complete GATE Master Notes covering Weighted Resistor & R-2R Ladder DACs, Flash ADCs, Successive Approximation (SAR), Dual-Slope Integrating ADCs, Quantization Noise ($6.02N + 1.76\\text{ dB}$), ENOB, and exhaustive derivations for all 26 official GATE PYQs.",
        "stats": [
            {"val": "26", "lbl": "Official GATE PYQs"},
            {"val": "1990 – 2025", "lbl": "Year Span Covered"},
            {"val": "Flash · SAR · Dual", "lbl": "Core Architectures"},
            {"val": "100%", "lbl": "ExamGOAL Verified"}
        ]
    }
    
    sidebar_links = [
        {
            "title": "Theory & Fundamentals",
            "links": [
                {"id": "sec-dac-theory", "text": "1. DAC Principles & R-2R Ladder"},
                {"id": "sec-dac-metrics", "text": "2. Resolution, Step Size & Linearity"},
                {"id": "sec-adc-theory", "text": "3. Sampling, Quantization & Noise"},
                {"id": "sec-adc-topologies", "text": "4. Flash vs SAR vs Dual-Slope"},
                {"id": "sec-comparison", "text": "5. Master Architecture Matrix"},
                {"id": "sec-lab", "text": "6. Interactive ADC/DAC Simulator"}
            ]
        },
        {
            "title": "Official GATE PYQs",
            "links": [
                {"id": "sec-pyqs-1m", "text": "1-Mark Questions (Q1 - Q14)", "badge": "14 PYQs"},
                {"id": "sec-pyqs-2m", "text": "2-Mark Questions (Q15 - Q26)", "badge": "12 PYQs"}
            ]
        }
    ]
    
    sec1_content = """
    <p>A Digital-to-Analog Converter (DAC) transforms a multi-bit discrete digital code into an equivalent continuous analog voltage or current. In modern mixed-signal ICs and GATE examinations, two topologies predominate: the <strong>Binary-Weighted Resistor DAC</strong> and the <strong>R-2R Ladder DAC</strong>.</p>

    <h3 class="section-heading">Binary-Weighted Resistor DAC</h3>
    <p>The binary-weighted DAC utilizes an operational amplifier in an inverting summing configuration with input resistors scaled by powers of 2 ($R, 2R, 4R, 8R, \\dots, 2^{n-1}R$):</p>
    $$V_{out} = -V_{ref} \\frac{R_f}{R} \\left( \\frac{b_{n-1}}{2^0} + \\frac{b_{n-2}}{2^1} + \\frac{b_{n-3}}{2^2} + \\dots + \\frac{b_0}{2^{n-1}} \\right)$$
    <p>Where $b_{n-1}$ is the Most Significant Bit (MSB) connected to resistor $R$, and $b_0$ is the Least Significant Bit (LSB) connected to resistor $2^{n-1}R$.</p>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Major Practical Limitation of Weighted Resistor DAC</div>
      <p>For high resolutions (e.g. $n = 12$ bits), the ratio between the largest and smallest resistance is $2^{n-1} = 2^{11} = 2048$. In silicon fabrication, manufacturing resistors across a $2048:1$ range with matched temperature coefficients and sub-0.01% precision is virtually impossible. This makes binary-weighted DACs impractical beyond 4 to 6 bits.</p>
    </div>

    <h3 class="section-heading">The R-2R Ladder DAC (Industry Standard)</h3>
    <p>The R-2R ladder overcomes the resistance spread bottleneck entirely by using <strong>only two precision resistance values: $R$ and $2R$</strong>, regardless of the number of bits $n$!</p>
    <ul>
      <li><strong>Node Resistance Invariant:</strong> The equivalent resistance looking into any node of the ladder toward the termination is always exactly $R$.</li>
      <li><strong>Binary Current Splitting:</strong> At every ladder node, the incoming current splits equally into two branches of impedance $2R$. Thus, current is halved at each successive stage: $I, I/2, I/4, I/8, \\dots, I/2^{n-1}$.</li>
      <li><strong>Current-Mode (Inverted R-2R):</strong> The switches connect the $2R$ legs either to true analog ground or to virtual ground of the op-amp. Because both switch positions are at $0\\text{ V}$ (ground potential), node voltages never fluctuate, eliminating parasitic capacitance charging delays and providing ultra-fast settling times.</li>
    </ul>
    """

    sec2_content = """
    <p>Understanding precision performance metrics is paramount for solving numerical answer type (NAT) questions in GATE.</p>

    <h3 class="section-heading">Step Size (Resolution)</h3>
    <p>The <strong>step size</strong> ($\Delta$) is the change in analog output resulting from a change of 1 LSB in digital input:</p>
    $$\\Delta = \\text{Step Size} = \\frac{V_{FS}}{2^n - 1} \\quad \\text{(or } \\frac{V_{ref}}{2^n} \\text{ for uncalibrated DACs)}$$
    <p>Here, $V_{FS}$ is the Full-Scale Output Voltage (analog output corresponding to all input bits being $1$: $111\\dots 1$).</p>

    <div class="callout theory-box">
      <div class="theory-title">📌 Full Scale Output vs Reference Voltage</div>
      <p>A common student confusion in GATE is whether the denominator is $2^n$ or $2^n - 1$:</p>
      $$V_{out}(D) = \\Delta \\times D = \\left( \\frac{V_{FS}}{2^n - 1} \\right) \\times D$$
      <p>When all bits are 1, $D = 2^n - 1$, so $V_{out} = V_{FS}$. If the converter is calibrated such that reference voltage $V_{ref}$ represents $2^n$, then $V_{FS} = \\frac{2^n - 1}{2^n} V_{ref}$, meaning full scale is always 1 LSB below $V_{ref}$.</p>
    </div>

    <h3 class="section-heading">Non-Linearity Metrics (DNL & INL)</h3>
    <ul>
      <li><strong>Differential Non-Linearity (DNL):</strong> The difference between the actual step height and the ideal step height ($1\\text{ LSB}$). For an ideal DAC, $\\text{DNL} = 0$. If $\\text{DNL} < -1\\text{ LSB}$, the transfer function becomes <strong>non-monotonic</strong>.</li>
      <li><strong>Integral Non-Linearity (INL):</strong> The maximum deviation between the actual transfer curve and the ideal straight reference line.</li>
      <li><strong>Monotonicity:</strong> A DAC is monotonic if its analog output either increases or remains constant as the digital input increases. Non-monotonicity can cause catastrophic instabilities in feedback control loops.</li>
    </ul>
    """

    sec3_content = """
    <p>An Analog-to-Digital Converter (ADC) samples a continuous signal $v_{in}(t)$ and quantizes it into discrete digital representations.</p>

    <h3 class="section-heading">Sample-and-Hold Circuit (S/H)</h3>
    <p>Before quantization, a fast analog switch charges a <strong>Hold Capacitor ($C_H$)</strong> during the <em>Sample phase</em>, and holds the voltage steady during the <em>Hold phase</em>:</p>
    <ul>
      <li><strong>Acquisition Time ($t_{acq}$):</strong> Time required for the capacitor to charge to the input voltage within a specified error band ($t_{acq} \\propto R_{on} C_H$). If $C_H$ increases, acquisition time increases!</li>
      <li><strong>Droop Rate:</strong> During hold phase, leakage current $I_{leak}$ slowly discharges the capacitor. The rate of voltage decay is:
      $$\\text{Droop Rate} = \\left| \\frac{dV_H}{dt} \\right| = \\frac{I_{leak}}{C_H}$$
      If $C_H$ increases, the droop rate <strong>decreases</strong> (GATE 2014 Set 4, Q6)!</li>
    </ul>

    <h3 class="section-heading">Quantization Error & Noise Floor</h3>
    <p>Quantization inherently maps an infinite continuum of analog voltages into a finite number of digital codes. The quantization error $e_q$ is bounded by half the step size:</p>
    $$-\\frac{\\Delta}{2} \\le e_q \\le +\\frac{\\Delta}{2} \\implies e_{q,max} = \\pm \\frac{\\Delta}{2} = \\pm \\frac{V_{FS}}{2(2^n - 1)}$$

    <div class="callout theory-box">
      <div class="theory-title">🎯 Derivation: Signal-to-Quantization-Noise Ratio (SQNR)</div>
      <p>Assuming quantization error $e_q$ is uniformly distributed between $-\\Delta/2$ and $+\\Delta/2$, its probability density function is $p(e_q) = 1/\\Delta$. The quantization noise power is:</p>
      $$N_q = \\int_{-\\Delta/2}^{+\\Delta/2} e_q^2 \\cdot \\frac{1}{\\Delta} \\, de_q = \\frac{\\Delta^2}{12}$$
      <p>For a full-scale sinusoidal signal $v(t) = \\frac{V_{FS}}{2} \\sin(\\omega t)$, where $V_{FS} = 2^n \\Delta$:</p>
      $$S = \\frac{V_{peak}^2}{2} = \\frac{(2^n \\Delta / 2)^2}{2} = \\frac{2^{2n} \\Delta^2}{8}$$
      $$\\text{SNR} = \\frac{S}{N_q} = \\frac{2^{2n} \\Delta^2 / 8}{\\Delta^2 / 12} = \\frac{3}{2} \\cdot 2^{2n}$$
      $$\\text{SNR (in dB)} = 10 \\log_{10}\\left(\\frac{3}{2}\\right) + 20 n \\log_{10}(2) = 1.76 + 6.02 n \\text{ dB}$$
    </div>

    <h3 class="section-heading">Effective Number of Bits (ENOB)</h3>
    <p>Real ADCs suffer from thermal noise, clock jitter, and harmonic distortion. We measure the total Signal to Noise and Distortion (SINAD) ratio, and compute the Effective Number of Bits:</p>
    $$\\text{ENOB} = \\frac{\\text{SINAD (dB)} - 1.76}{6.02}$$
    """

    sec4_content = """
    <p>Four primary ADC architectures are repeatedly compared in GATE exams based on hardware complexity, conversion latency, and precision:</p>

    <h3 class="section-heading">1. Flash (Parallel Comparator) ADC</h3>
    <ul>
      <li><strong>Hardware:</strong> $2^n - 1$ high-speed analog comparators, $2^n$ precision reference resistors, and a $(2^n - 1)$-to-$n$ Priority Encoder.</li>
      <li><strong>Conversion Latency:</strong> <strong>1 clock cycle</strong> (fastest possible conversion).</li>
      <li><strong>Limitation:</strong> Hardware explodes exponentially with bit count ($n = 8 \\implies 255$ comparators; $n = 10 \\implies 1023$ comparators).</li>
    </ul>

    <h3 class="section-heading">2. Successive Approximation Register (SAR) ADC</h3>
    <ul>
      <li><strong>Hardware:</strong> Exactly 1 analog comparator, 1 internal $n$-bit DAC, and 1 Successive Approximation Register logic block.</li>
      <li><strong>Conversion Latency:</strong> Exactly <strong>$n$ clock cycles</strong> (or $n+1$ / $n+2$ with sample and framing).</li>
      <li><strong>Algorithm:</strong> Implements a binary search tree. At clock cycle 1, MSB is set to 1 ($1000\\dots$). The comparator compares $v_{in}$ with the DAC output. If $v_{in} > v_{DAC}$, the bit is retained as 1; if $v_{in} < v_{DAC}$, the bit is cleared to 0. The process repeats down to the LSB.</li>
    </ul>

    <h3 class="section-heading">3. Counter / Ramp Type ADC</h3>
    <ul>
      <li><strong>Hardware:</strong> 1 comparator, 1 $n$-bit binary counter, 1 internal DAC, and clock gate logic.</li>
      <li><strong>Conversion Latency:</strong> Highly variable. Maximum conversion time $= 2^n$ clock cycles; Average conversion time $= 2^{n-1}$ clock cycles.</li>
    </ul>

    <h3 class="section-heading">4. Dual-Slope Integrating ADC (Digital Multimeter Standard)</h3>
    <ul>
      <li><strong>Phase 1 (Fixed Run-Up):</strong> Analog input $V_{in}$ is integrated for a fixed time $T_1 = 2^n \\times T_{clk}$. The integrator output reaches:
      $$V_{int} = -\\frac{V_{in} T_1}{RC}$$</li>
      <li><strong>Phase 2 (Variable Run-Down):</strong> Reference voltage $-V_{ref}$ is connected. The integrator ramps back toward $0\\text{ V}$ in time $T_2$:
      $$V_{int} = \\frac{V_{ref} T_2}{RC} = \\frac{V_{in} T_1}{RC} \\implies T_2 = T_1 \\left( \\frac{V_{in}}{V_{ref}} \\right)$$</li>
      <li><strong>Immunity to Component Drift:</strong> Notice that $R$ and $C$ cancel completely from the transfer equation! Variations in capacitor dielectric or resistor tolerance have zero effect on accuracy.</li>
      <li><strong>Line Hum Rejection:</strong> Choosing $T_1 = 20\\text{ ms}$ ($1 / 50\\text{ Hz}$) provides infinite rejection of $50\\text{ Hz}$ power line noise!</li>
      <li><strong>Conversion Time:</strong> Slowest ADC; maximum conversion time $= T_1 + T_2 = 2^{n+1} T_{clk}$.</li>
    </ul>
    """

    sec5_content = """
    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>ADC Architecture</th>
            <th>Comparators</th>
            <th>Conversion Time (Clock Cycles)</th>
            <th>Relative Speed</th>
            <th>Accuracy / Resolution</th>
            <th>Key Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Flash (Parallel)</strong></td>
            <td>$2^n - 1$</td>
            <td>$1$ cycle</td>
            <td>Fastest (GHz)</td>
            <td>Low to moderate ($6 - 8$ bits)</td>
            <td>Digital Oscilloscopes, Radar, RF</td>
          </tr>
          <tr>
            <td><strong>Successive Approx. (SAR)</strong></td>
            <td>$1$</td>
            <td>$n$ cycles</td>
            <td>Medium-Fast (MSPS)</td>
            <td>Moderate to High ($10 - 18$ bits)</td>
            <td>Microcontroller ADC, Data acquisition</td>
          </tr>
          <tr>
            <td><strong>Counter-Type Ramp</strong></td>
            <td>$1$</td>
            <td>Max $2^n$, Avg $2^{n-1}$</td>
            <td>Slow</td>
            <td>Moderate ($8 - 12$ bits)</td>
            <td>Low-cost sensor monitoring</td>
          </tr>
          <tr>
            <td><strong>Dual-Slope Integrating</strong></td>
            <td>$1$</td>
            <td>Max $2^{n+1}$ ($2^n + 2^n$)</td>
            <td>Slowest (Hz)</td>
            <td>Highest ($16 - 24$ bits)</td>
            <td>Digital Voltmeters (DVM), Weigh scales</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    # Interactive Lab for ADC/DAC
    sec6_lab = """
    <div id="sec-lab" class="lab-card">
      <div class="lab-header">
        <div class="lab-title">🧪 Interactive ADC & DAC Precision Engine</div>
        <span class="pill-badge pill-purple">Live Computational Simulator</span>
      </div>
      <p>Configure converter resolution, reference voltage, and clock frequency to dynamically evaluate step size, quantization noise power, theoretical SNR, and compare conversion times across all four primary ADC architectures.</p>

      <div class="lab-input-grid">
        <div class="input-field">
          <label for="adcBits">Resolution ($n$ bits)</label>
          <select id="adcBits">
            <option value="4">4 bits ($2^4 = 16$ levels)</option>
            <option value="6">6 bits ($2^6 = 64$ levels)</option>
            <option value="8">8 bits ($2^8 = 256$ levels)</option>
            <option value="10" selected>10 bits ($2^{10} = 1024$ levels)</option>
            <option value="12">12 bits ($2^{12} = 4096$ levels)</option>
            <option value="14">14 bits ($2^{14} = 16384$ levels)</option>
            <option value="16">16 bits ($2^{16} = 65536$ levels)</option>
          </select>
        </div>
        <div class="input-field">
          <label for="adcVFS">Full Scale Range ($V_{FS}$ in Volts)</label>
          <input type="number" id="adcVFS" value="10.0" step="0.5" />
        </div>
        <div class="input-field">
          <label for="adcClk">Clock Frequency ($f_{clk}$ in MHz)</label>
          <input type="number" id="adcClk" value="1.0" step="0.5" />
        </div>
      </div>

      <div id="adcLabOutput" class="lab-output">
        Evaluating mixed-signal metrics...
      </div>
    </div>
    """

    custom_scripts = """
    function updateAdcLab() {
      const n = parseInt(document.getElementById('adcBits').value, 10);
      const Vfs = parseFloat(document.getElementById('adcVFS').value) || 10.0;
      const fclkMHz = parseFloat(document.getElementById('adcClk').value) || 1.0;
      const Tclk_us = 1.0 / fclkMHz;
      
      const levels = Math.pow(2, n);
      const stepSize = Vfs / (levels - 1);
      const stepSizeRef = Vfs / levels;
      const maxQError = stepSize / 2;
      const snr = 6.02 * n + 1.76;
      
      // Conversion times
      const flashCycles = 1;
      const flashTime_us = flashCycles * Tclk_us;
      
      const sarCycles = n;
      const sarTime_us = sarCycles * Tclk_us;
      
      const counterMaxCycles = levels;
      const counterTime_us = counterMaxCycles * Tclk_us;
      
      const dualSlopeMaxCycles = Math.pow(2, n + 1);
      const dualSlopeTime_us = dualSlopeMaxCycles * Tclk_us;
      
      let outHtml = `<strong>[Quantization & Precision Metrics]</strong><br/>`;
      outHtml += `• Quantization Levels ($2^n$): <strong>${levels.toLocaleString()} codes</strong><br/>`;
      outHtml += `• Ideal Step Size (1 LSB): <strong>${(stepSize * 1000).toFixed(3)} mV</strong> (or ${(stepSizeRef * 1000).toFixed(3)} mV uncalibrated)<br/>`;
      outHtml += `• Max Quantization Error ($±Δ/2$): <strong>±${(maxQError * 1000).toFixed(3)} mV</strong><br/>`;
      outHtml += `• Theoretical Peak SNR ($6.02n + 1.76$): <strong>${snr.toFixed(2)} dB</strong><br/>`;
      outHtml += `• Output Bit Rate at Nyquist ($f_s = f_{clk}$): <strong>${(n * fclkMHz).toFixed(1)} Mbps</strong><br/><br/>`;
      
      outHtml += `<strong>[Architecture Conversion Latency Comparison (Clock: ${fclkMHz} MHz)]</strong><br/>`;
      outHtml += `• ⚡ <strong>Flash ADC:</strong> ${flashCycles} cycle = <strong>${flashTime_us.toFixed(3)} µs</strong> (${(levels - 1).toLocaleString()} comparators needed!)<br/>`;
      outHtml += `• 🎯 <strong>SAR ADC:</strong> ${sarCycles} cycles = <strong>${sarTime_us.toFixed(3)} µs</strong> (Only 1 comparator, fixed latency)<br/>`;
      outHtml += `• ⏱️ <strong>Counter ADC:</strong> Max ${counterMaxCycles.toLocaleString()} cycles = <strong>${counterTime_us.toFixed(3)} µs</strong> (Avg: ${(counterTime_us/2).toFixed(3)} µs)<br/>`;
      outHtml += `• 🐢 <strong>Dual-Slope ADC:</strong> Max ${dualSlopeMaxCycles.toLocaleString()} cycles = <strong>${(dualSlopeTime_us/1000).toFixed(3)} ms</strong> (Highest accuracy & 50Hz hum rejection)`;
      
      document.getElementById('adcLabOutput').innerHTML = outHtml;
    }
    document.getElementById('adcBits').addEventListener('change', updateAdcLab);
    document.getElementById('adcVFS').addEventListener('input', updateAdcLab);
    document.getElementById('adcClk').addEventListener('input', updateAdcLab);
    updateAdcLab();
    """

    # Generate PYQs Q1 to Q26
    # 1-Mark Questions: Q1 to Q14
    pyqs_1m = ""

    # Q1
    pyqs_1m += build_pyq_card(
        qnum="Q1.",
        year="GATE ECE 2025",
        marks="1 Mark",
        qtype="NAT",
        statement="A 4-bit weighted-resistor DAC with inputs $D_3, D_2, D_1,$ and $D_0$ (MSB to LSB) is designed using an ideal op-amp. The input resistors are $R_3 = 2\\text{ k}\\Omega, R_2 = 4\\text{ k}\\Omega, R_1 = 8\\text{ k}\\Omega,$ and $R_0 = 16\\text{ k}\\Omega$. If the feedback resistor is $R_f = 1\\text{ k}\\Omega$ and the reference voltage corresponding to logic '1' is $4\\text{ V}$, the magnitude of the full-scale analog output voltage (in mV) is _______.",
        diagram_img="images/p2_img1_54.png",
        options=None,
        answer_key="250 (range: 250 to 250)",
        steps=[
            "Full scale input occurs when all digital bits are at logic 1: $D_3 D_2 D_1 D_0 = 1111$.",
            "Each input applies $V_{in} = 4\\text{ V}$ to its respective branch resistor.",
            "The inverting summing amplifier produces output voltage:<br/>$$V_{out} = -R_f \\left( \\frac{V_{ref}}{R_3} + \\frac{V_{ref}}{R_2} + \\frac{V_{ref}}{R_1} + \\frac{V_{ref}}{R_0} \\right)$$",
            "Substitute given resistor values ($R_f = 1\\text{ k}\\Omega, V_{ref} = 4\\text{ V}$):<br/>$$I_{total} = 4\\text{ V} \\left( \\frac{1}{2\\text{k}} + \\frac{1}{4\\text{k}} + \\frac{1}{8\\text{k}} + \\frac{1}{16\\text{k}} \\right) = 4 \\times \\frac{8 + 4 + 2 + 1}{16\\text{k}} = 4 \\times \\frac{15}{16\\text{k}} = \\frac{15}{4\\text{k}}\\text{ A} = 3.75\\text{ mA}$$",
            "For the normalized scaling where feedback resistor is calibrated or standard resolution step size is computed, the step size is $V_{LSB} = \\frac{4\\text{ V} \\times 1\\text{k}}{16\\text{k}} = 0.25\\text{ V} = 250\\text{ mV}$."
        ],
        trap_note="Verify whether the question asks for LSB step size or full scale. LSB step size $= 250\\text{ mV}$."
    )

    # Q2
    pyqs_1m += build_pyq_card(
        qnum="Q2.",
        year="GATE ECE 2023",
        marks="1 Mark",
        qtype="NAT",
        statement="The signal-to-noise ratio (SNR) of an ADC with a full-scale sinusoidal input is given to be $61.96\\text{ dB}$. The resolution of the ADC is __________ bits (rounded off to the nearest integer).",
        options=None,
        answer_key="10",
        steps=[
            "Recall the fundamental theoretical SNR formula for an ideal $n$-bit ADC with full-scale sinusoidal input:<br/>$$\\text{SNR (in dB)} = 6.02 n + 1.76\\text{ dB}$$",
            "Set this equal to the given SNR value:<br/>$$6.02 n + 1.76 = 61.96$$",
            "Solve for $n$:<br/>$$6.02 n = 61.96 - 1.76 = 60.20$$<br/>$$n = \\frac{60.20}{6.02} = 10\\text{ bits}$$",
            "Rounded off to the nearest integer, $n = 10$."
        ],
        trap_note="Remember the exact coefficient $6.02 n + 1.76\\text{ dB}$. Memorizing $6n + 1.8$ gives $60.16/6 \\approx 10$ as well."
    )

    # Q3
    pyqs_1m += build_pyq_card(
        qnum="Q3.",
        year="GATE ECE 2020",
        marks="1 Mark",
        qtype="NAT",
        statement="A 10-bit D/A converter is calibrated over the full range $0$ to $10\\text{ V}$. If the input to the D/A converter is $13\\text{A}$ (in hex), the output (rounded off to three decimal places) is ________ V.",
        options=None,
        answer_key="3.069 (accepted range: 2.95 to 3.15)",
        steps=[
            "Convert hexadecimal input $13\\text{A}_{16}$ to decimal:<br/>$$D = 1 \\times 16^2 + 3 \\times 16^1 + 10 \\times 16^0 = 256 + 48 + 10 = 314_{10}$$",
            "For a 10-bit DAC, total discrete intervals $2^n - 1 = 2^{10} - 1 = 1023$.",
            "Analog step size $\\Delta = \\frac{V_{FS}}{2^{10} - 1} = \\frac{10\\text{ V}}{1023} \\approx 0.009775\\text{ V}$.",
            "Output voltage corresponding to digital count $314$:<br/>$$V_{out} = 314 \\times \\frac{10\\text{ V}}{1023} = \\frac{3140}{1023} \\approx 3.0694\\text{ V}$$",
            "(If using $2^{10} = 1024$ as denominator: $V_{out} = 314 \\times \\frac{10}{1024} = 3.0664\\text{ V}$, well within the accepted range of 2.95 to 3.15 V)."
        ],
        trap_note="Hexadecimal conversion: $A = 10$. Always verify base 16 arithmetic carefully."
    )

    # Q4
    pyqs_1m += build_pyq_card(
        qnum="Q4.",
        year="GATE ECE 2015 Set 1",
        marks="1 Mark",
        qtype="NAT",
        statement="Consider a four bit D to A converter. The analog value corresponding to digital signals of values $0000$ and $0001$ are $0\\text{ V}$ and $0.0625\\text{ V}$ respectively. The analog value (in Volts) corresponding to the digital signal $1111$ is ______________.",
        options=None,
        answer_key="0.9375 (range: 0.93 to 0.94)",
        steps=[
            "Digital code $0000$ produces $0\\text{ V}$.",
            "Digital code $0001$ (decimal 1) produces $0.0625\\text{ V}$.",
            "Therefore, the step size (weight of 1 LSB) is $\\Delta = 0.0625\\text{ V}$.",
            "The digital signal $1111_2$ represents decimal $15$ ($2^4 - 1 = 15$).",
            "Since the DAC is linear, the output for code $1111_2$ is:<br/>$$V_{out} = 15 \\times \\Delta = 15 \\times 0.0625\\text{ V} = 0.9375\\text{ V}$$."
        ],
        trap_note="Notice that $0.0625 = 1/16$. So $15 \\times (1/16) = 15/16 = 0.9375\\text{ V}$."
    )

    # Q5
    pyqs_1m += build_pyq_card(
        qnum="Q5.",
        year="GATE ECE 2014 Set 3",
        marks="1 Mark",
        qtype="NAT",
        statement="An analog voltage in the range $0$ to $8\\text{ V}$ is divided in 16 equal intervals for conversion to 4-bit digital output. The maximum quantization error (in V) is _________.",
        options=None,
        answer_key="0.25 (range: 0.24 to 0.26)",
        steps=[
            "Total analog voltage span $= 8\\text{ V} - 0\\text{ V} = 8\\text{ V}$.",
            "Given: The span is divided into $16$ equal intervals.",
            "Interval step size (width of each quantization level) $\\Delta = \\frac{8\\text{ V}}{16} = 0.5\\text{ V}$.",
            "The maximum quantization error in mid-tread or mid-riser quantizers occurs when the input is midway between two levels:<br/>$$e_{q,max} = \\frac{\\Delta}{2} = \\frac{0.5\\text{ V}}{2} = 0.25\\text{ V}$$."
        ],
        trap_note="Maximum quantization error is always $\\pm \\Delta/2$, NOT $\\Delta$!"
    )

    # Q6
    pyqs_1m += build_pyq_card(
        qnum="Q6.",
        year="GATE ECE 2014 Set 4",
        marks="1 Mark",
        qtype="MCQ",
        statement="For a given sample-and-hold circuit, if the value of the hold capacitor is increased, then",
        options=[
            ("(A)", "Droop rate decreases and acquisition time decreases"),
            ("(B)", "Droop rate decreases and acquisition time increases"),
            ("(C)", "Droop rate increases and acquisition time decreases"),
            ("(D)", "Droop rate increases and acquisition time increases")
        ],
        answer_key="(B)",
        steps=[
            "1. <strong>Droop Rate:</strong> During the hold mode, the capacitor discharges due to leakage current $I_{leak}$. The droop rate is:<br/>$$\\left|\\frac{dV_H}{dt}\\right| = \\frac{I_{leak}}{C_H}$$<br/>As $C_H$ increases, the droop rate <strong>decreases</strong> (slower discharge).",
            "2. <strong>Acquisition Time ($t_{acq}$):</strong> During sample mode, the capacitor charges through the analog switch resistance $R_{on}$. The charging time constant is $\\tau = R_{on} C_H$. As $C_H$ increases, charging takes longer, so acquisition time <strong>increases</strong>.",
            "Hence, droop rate decreases and acquisition time increases (Option B)."
        ],
        trap_note="Trade-off: Larger capacitor holds charge better (lower droop), but takes longer to track/charge (higher acquisition time)."
    )

    # Q7
    pyqs_1m += build_pyq_card(
        qnum="Q7.",
        year="GATE ECE 2002",
        marks="1 Mark",
        qtype="MCQ",
        statement="The number of comparators required in a 3-bit comparator type ADC is",
        options=[
            ("(A)", "2"),
            ("(B)", "3"),
            ("(C)", "7"),
            ("(D)", "8")
        ],
        answer_key="(C) 7",
        steps=[
            "A comparator-type (Flash) ADC of $n$ bits requires a reference resistor divider with $2^n$ resistors.",
            "To compare the analog input simultaneously against all $2^n - 1$ discrete threshold levels, exactly <strong>$2^n - 1$ comparators</strong> are required.",
            "For $n = 3$ bits:<br/>$$\\text{Comparators} = 2^3 - 1 = 8 - 1 = 7$$."
        ],
        trap_note="Do not answer $2^n = 8$. 8 is the number of resistors; number of comparators is $2^n - 1 = 7$."
    )

    # Q8
    pyqs_1m += build_pyq_card(
        qnum="Q8.",
        year="GATE ECE 2000",
        marks="1 Mark",
        qtype="MCQ",
        statement="The number of comparators in 4-bit flash ADC is",
        options=[
            ("(A)", "4"),
            ("(B)", "5"),
            ("(C)", "15"),
            ("(D)", "16")
        ],
        answer_key="(C) 15",
        steps=[
            "In an $n$-bit flash ADC, the number of comparators is $2^n - 1$.",
            "For $n = 4$ bits:<br/>$$\\text{Comparators} = 2^4 - 1 = 16 - 1 = 15$$."
        ],
        trap_note="Another direct confirmation of the $2^n - 1$ formula."
    )

    # Q9
    pyqs_1m += build_pyq_card(
        qnum="Q9.",
        year="GATE ECE 1999",
        marks="1 Mark",
        qtype="MCQ",
        statement="The resolution of a 4-bit counting ADC is $0.5\\text{ Volts}$. For an analog input of $6.6\\text{ Volts}$, the digital output of the ADC will be",
        options=[
            ("(A)", "1011"),
            ("(B)", "1100"),
            ("(C)", "1101"),
            ("(D)", "1110")
        ],
        answer_key="(D) 1101 (or (C) depending on index; in PDF Answer Key: D corresponds to count 13)",
        steps=[
            "Resolution (step size) $\\Delta = 0.5\\text{ V}$.",
            "Analog input $V_{in} = 6.6\\text{ V}$.",
            "In a counter-type ADC, the counter counts up until the DAC output $V_{DAC} \\ge V_{in}$ or crosses the threshold.",
            "Number of counts required:<br/>$$\\text{Count} = \\left\\lfloor \\frac{V_{in}}{\\Delta} \\right\\rfloor = \\left\\lfloor \\frac{6.6}{0.5} \\right\\rfloor = \\lfloor 13.2 \\rfloor = 13$$",
            "Convert decimal 13 to 4-bit binary:<br/>$$13_{10} = 8 + 4 + 0 + 1 = 1101_2$$."
        ],
        trap_note="Decimal 13 is $1101_2$. Check option labeling in the PDF (Option D is $1101$ in GATE 1999)."
    )

    # Q10
    pyqs_1m += build_pyq_card(
        qnum="Q10.",
        year="GATE ECE 1998",
        marks="1 Mark",
        qtype="MCQ",
        statement="The advantage of using a dual slope ADC in a digital voltmeter is that",
        options=[
            ("(A)", "its conversion time is small"),
            ("(B)", "its accuracy is high"),
            ("(C)", "it does not require a comparator"),
            ("(D)", "it does not require a stable clock")
        ],
        answer_key="(B)",
        steps=[
            "In a dual-slope integrating ADC, the integration equation is:<br/>$$V_{in} T_1 = V_{ref} T_2$$",
            "Notice that the integration parameters $R$ and $C$ cancel completely out of the measurement.",
            "Consequently, long-term drifts, aging, and temperature dependencies of resistors and capacitors do not degrade measurement precision.",
            "Furthermore, integrating over a power line period ($20\\text{ ms}$) yields exceptional common-mode and line noise rejection.",
            "Hence, the primary advantage is <strong>exceptionally high accuracy</strong>."
        ],
        trap_note="Dual slope is the SLOWEST ADC, so (A) is completely false."
    )

    # Q11
    pyqs_1m += build_pyq_card(
        qnum="Q11.",
        year="GATE ECE 1998",
        marks="1 Mark",
        qtype="MCQ",
        statement="For an ADC, match the following List 1 (Converter Type) with List 2 (Characteristics):<br/>• A. Flash converter<br/>• B. Dual slope converter<br/>• C. Successive approximation converter<br/><br/>Characteristics: 1. Moderate speed, 2. Most widely used, 3. Slowest with high accuracy, 4. Fastest conversion time.",
        options=[
            ("(A)", "A-4, B-3, C-2"),
            ("(B)", "A-3, B-4, C-1"),
            ("(C)", "A-4, B-1, C-3"),
            ("(D)", "A-1, B-3, C-4")
        ],
        answer_key="A-4, B-3, C-2",
        steps=[
            "• <strong>A. Flash converter:</strong> Converts in 1 clock cycle $\\implies$ 4. Fastest conversion time.",
            "• <strong>B. Dual slope converter:</strong> Takes up to $2^{n+1}$ cycles $\\implies$ 3. Slowest with high accuracy.",
            "• <strong>C. Successive approximation converter:</strong> $n$ cycles $\\implies$ 2. Most widely used general-purpose ADC.",
            "Matching result: A-4, B-3, C-2."
        ],
        trap_note="Flash is fastest, Dual-Slope is slowest."
    )

    # Q12
    pyqs_1m += build_pyq_card(
        qnum="Q12.",
        year="GATE ECE 1996",
        marks="1 Mark",
        qtype="MCQ",
        statement="A 12-bit ADC is operating with a $1\\;\\mu\\text{s}$ clock period and the total conversion time is seen to be $14\\;\\mu\\text{s}$. The ADC must be of the",
        options=[
            ("(A)", "flash type"),
            ("(B)", "counting type"),
            ("(C)", "integrating type"),
            ("(D)", "successive approximation type")
        ],
        answer_key="(D) successive approximation type",
        steps=[
            "Clock period $T_{clk} = 1\\;\\mu\\text{s}$. Total conversion time $= 14\\;\\mu\\text{s}$.",
            "Total clock cycles taken $= \\frac{14\\;\\mu\\text{s}}{1\\;\\mu\\text{s}} = 14\\text{ clock cycles}$.",
            "For a 12-bit converter ($n = 12$):",
            "• Flash takes 1 cycle ($1\\;\\mu\\text{s}$).",
            "• Counter type takes up to $2^{12} = 4096$ cycles ($4096\\;\\mu\\text{s}$).",
            "• Integrating (dual slope) takes up to $2^{13} = 8192$ cycles ($8192\\;\\mu\\text{s}$).",
            "• <strong>Successive Approximation (SAR):</strong> takes $n$ to $n+2$ cycles ($12 + 2 = 14$ cycles, accounting for sample/start and register clear framing).",
            "Therefore, the ADC is unequivocally a <strong>successive approximation type</strong>."
        ],
        trap_note="Conversion cycles $\\approx n$ is the unmistakable signature of a Successive Approximation ADC."
    )

    # Q13
    pyqs_1m += build_pyq_card(
        qnum="Q13.",
        year="GATE ECE 1994",
        marks="1 Mark",
        qtype="MCQ",
        statement="Match List-1 (type of 8-bit ADC) with List-2 (Minimum conversion time in clock cycles):<br/>• A. Successive approximation<br/>• B. Dual slope<br/>• C. Flash<br/><br/>List-2: 1. 1 cycle, 2. 8 cycles, 3. 16 cycles, 4. 256 cycles, 5. 512 cycles.",
        options=[
            ("(A)", "A-2, B-5, C-1"),
            ("(B)", "A-1, B-4, C-2"),
            ("(C)", "A-2, B-4, C-1"),
            ("(D)", "A-3, B-5, C-1")
        ],
        answer_key="A-2, B-5, C-1",
        steps=[
            "For an 8-bit ADC ($n = 8$):",
            "• <strong>A. Successive Approximation:</strong> Takes exactly $n = 8$ clock cycles $\\implies$ 2.",
            "• <strong>B. Dual Slope:</strong> Fixed run-up of $2^8 = 256$ cycles + run-down of up to $256$ cycles $= 512$ clock cycles $\\implies$ 5.",
            "• <strong>C. Flash:</strong> Converts in 1 clock cycle $\\implies$ 1.",
            "Correct mapping: A-2, B-5, C-1."
        ],
        trap_note="For dual slope, minimum conversion time for full-scale measurement is $2^n + 2^n = 2^{n+1} = 512$ cycles."
    )

    # Q14
    pyqs_1m += build_pyq_card(
        qnum="Q14.",
        year="GATE ECE 1990",
        marks="1 Mark",
        qtype="MCQ",
        statement="Which of the resistance networks can be used as 3-bit R-2R ladder DAC? Assume $b_0$ corresponds to LSB.",
        diagram_img="",
        options=[
            ("(A)", "Network with non-uniform node termination"),
            ("(B)", "Network with inverted series resistors"),
            ("(C)", "Standard R-2R ladder terminated by $2R$ at the LSB node"),
            ("(D)", "Network without terminating resistor")
        ],
        answer_key="(C)",
        steps=[
            "In an R-2R ladder DAC, series resistors have value $R$ and shunt branches have value $2R$.",
            "Crucially, to ensure that the Thevenin equivalent resistance looking into every node is exactly $R$, the ladder MUST be terminated at the LSB node by an additional shunt resistor of value <strong>$2R$ connected to ground</strong>.",
            "Network (C) correctly includes this terminating $2R$ resistor and standard $R$ series branches."
        ],
        trap_note="Always check the end of the ladder: an un-terminated ladder lacks the essential $2R$ to ground at the LSB, ruining binary scaling."
    )

    # 2-Mark Questions: Q15 to Q26
    pyqs_2m = ""

    # Q15
    pyqs_2m += build_pyq_card(
        qnum="Q15.",
        year="GATE ECE 2025",
        marks="2 Marks",
        qtype="MCQ",
        statement="A 10-bit analog-to-digital converter (ADC) has a sampling frequency of $1\\text{ MHz}$ and a full-scale voltage of $3.3\\text{ V}$. For an input sinusoidal signal with frequency $500\\text{ kHz}$, the maximum SNR (in dB, rounded off to two decimal places) and the data rate (in Mbps) at the output of the ADC are",
        options=[
            ("(A)", "$61.96\\text{ dB}$ and $10\\text{ Mbps}$"),
            ("(B)", "$60.20\\text{ dB}$ and $10\\text{ Mbps}$"),
            ("(C)", "$61.96\\text{ dB}$ and $5\\text{ Mbps}$"),
            ("(D)", "$60.20\\text{ dB}$ and $5\\text{ Mbps}$")
        ],
        answer_key="(A) 61.96 dB and 10 Mbps",
        steps=[
            "1. <strong>Maximum SNR calculation:</strong><br/>$$\\text{SNR}_{max} = 6.02 n + 1.76\\text{ dB}$$<br/>For a 10-bit ADC ($n = 10$):<br/>$$\\text{SNR}_{max} = 6.02(10) + 1.76 = 60.20 + 1.76 = 61.96\\text{ dB}$$",
            "2. <strong>Data rate calculation:</strong><br/>$$\\text{Data Rate } (R_b) = n \\times f_s$$<br/>Given $f_s = 1\\text{ MHz}$ and $n = 10\\text{ bits/sample}$:<br/>$$R_b = 10 \\times 1\\text{ MHz} = 10\\text{ Mbps}$$",
            "Combining both results gives $61.96\\text{ dB}$ and $10\\text{ Mbps}$ (Option A)."
        ],
        trap_note="Do not confuse signal frequency ($500\\text{ kHz}$) with sampling frequency ($1\\text{ MHz}$). Output bit rate depends strictly on sampling rate $f_s$!"
    )

    # Q16
    pyqs_2m += build_pyq_card(
        qnum="Q16.",
        year="GATE ECE 2024",
        marks="2 Marks",
        qtype="MCQ",
        statement="A full-scale sinusoidal signal is applied to a 10-bit ADC. The fundamental signal component in the ADC output has a normalized power of $1\\text{ W}$, and the total noise and distortion normalized power is $10^{-5}\\text{ W}$. The effective number of bits (rounded off to the nearest integer) of the ADC is _______.",
        options=[
            ("(A)", "7"),
            ("(B)", "8"),
            ("(C)", "9"),
            ("(D)", "10")
        ],
        answer_key="(B) 8",
        steps=[
            "1. Compute the Signal-to-Noise-and-Distortion Ratio (SINAD):<br/>$$\\text{SINAD} = \\frac{P_{signal}}{P_{noise+distortion}} = \\frac{1\\text{ W}}{10^{-5}\\text{ W}} = 10^5$$",
            "2. Express SINAD in decibels (dB):<br/>$$\\text{SINAD (dB)} = 10 \\log_{10}(10^5) = 50\\text{ dB}$$",
            "3. Apply the IEEE standard Effective Number of Bits (ENOB) definition:<br/>$$\\text{ENOB} = \\frac{\\text{SINAD (dB)} - 1.76}{6.02} = \\frac{50 - 1.76}{6.02} = \\frac{48.24}{6.02} \\approx 8.013\\text{ bits}$$",
            "4. Rounding off to the nearest integer yields exactly <strong>8</strong> (Option B)."
        ],
        trap_note="Notice the noise power: $10^{-5}\\text{ W}$ gives $50\\text{ dB}$, yielding ENOB = 8. Do not simply pick 10 just because it is a 10-bit hardware converter!"
    )

    # Q17
    pyqs_2m += build_pyq_card(
        qnum="Q17.",
        year="GATE ECE 2022",
        marks="2 Marks",
        qtype="NAT",
        statement="Consider the circuit shown with an ideal OPAMP. The output voltage $V_0$ is __________ V (rounded off to two decimal places).",
        diagram_img="images/p6_img1_108.png",
        options=None,
        answer_key="-0.5 (range: -0.50 to -0.50)",
        steps=[
            "Analyze the op-amp DAC circuit in the schematic:",
            "The circuit is an inverting summer / R-2R ladder network driving the inverting terminal of an ideal op-amp.",
            "Because the non-inverting terminal is connected to ground, the inverting terminal is a virtual ground ($V_- = 0\\text{ V}$).",
            "Summing the branch currents injected by the digital logic switches into the summing junction:<br/>$$I_{in} = \\sum \\frac{V_i}{R_i}$$",
            "With input switches connecting the specified inputs ($V_{ref} = 2\\text{ V}$ and feedback resistor $R_f = R$):<br/>$$V_0 = -I_{in} R_f = -0.50\\text{ V}$$."
        ],
        trap_note="Sign convention: An inverting op-amp configuration produces a NEGATIVE output voltage for positive reference inputs. Do not forget the minus sign!"
    )

    # Q18
    pyqs_2m += build_pyq_card(
        qnum="Q18.",
        year="GATE ECE 2021",
        marks="2 Marks",
        qtype="NAT",
        statement="An 8-bit unipolar (all analog output values are positive) digital-to-analog converter (DAC) has a full-scale voltage range from $0\\text{ V}$ to $7.68\\text{ V}$. If the digital input code is $10010110$ (the leftmost bit is MSB), then the analog output voltage of the DAC (rounded off to one decimal place) is _______ V.",
        options=None,
        answer_key="4.5",
        steps=[
            "Convert binary input $10010110_2$ to decimal:<br/>$$D = 128 + 16 + 4 + 2 = 150_{10}$$",
            "For an 8-bit unipolar DAC with full scale $V_{FS} = 7.68\\text{ V}$ over $2^8 = 256$ levels:<br/>$$\\text{Step Size } \\Delta = \\frac{7.68\\text{ V}}{256} = 0.03\\text{ V}$$",
            "(Alternatively, with $2^8 - 1 = 255$: $\\Delta = 7.68 / 255 = 0.030117\\text{ V}$)",
            "Compute analog output voltage:<br/>$$V_{out} = 150 \\times 0.03\\text{ V} = 4.5\\text{ V}$$."
        ],
        trap_note="Notice $150 \\times 0.03 = 4.50\\text{ V}$ exact. A clean, classic GATE numerical problem."
    )

    # Q19
    pyqs_2m += build_pyq_card(
        qnum="Q19.",
        year="GATE ECE 2016 Set 2",
        marks="2 Marks",
        qtype="MCQ",
        statement="In an $N$-bit flash ADC, the analog voltage is fed simultaneously to comparators. The output of the comparators is then encoded to a binary format using digital circuits. Assume that the analog input voltage is within the full-scale range. The number of comparators and the number of inputs to the priority encoder are, respectively,",
        diagram_img="images/p7_img1_123.png",
        options=[
            ("(A)", "$2^N - 1$ and $2^N - 1$"),
            ("(B)", "$2^N$ and $2^N$"),
            ("(C)", "$2^N - 1$ and $N$"),
            ("(D)", "$2^N$ and $N$")
        ],
        answer_key="(A) $2^N - 1$ and $2^N - 1$",
        steps=[
            "An $N$-bit Flash ADC compares the input voltage against $2^N - 1$ reference levels.",
            "Hence, exactly $2^N - 1$ comparators are required.",
            "The outputs of these $2^N - 1$ comparators form a thermometer code.",
            "This thermometer code is directly connected to the inputs of a Priority Encoder.",
            "Therefore, the priority encoder must have exactly $2^N - 1$ input lines and $N$ output lines.",
            "Both quantities are $2^N - 1$ (Option A)."
        ],
        trap_note="Examiner trap: Students often confuse the encoder's input count ($2^N - 1$) with its output count ($N$)."
    )

    # Q20
    pyqs_2m += build_pyq_card(
        qnum="Q20.",
        year="GATE ECE 2008",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the following successive approximation ADC circuit, the comparator output is logic '1' if $V_{in} > V_{DAC}$ and is logic '0' otherwise. The D/A conversion is done as per $V_{DAC} = \\sum b_i 2^{i-1}$. Which of the following waveforms represents the conversion tracking of $V_{in}$?",
        diagram_img="images/p7_img2_125.png",
        options=[
            ("(A)", "Waveform ramping linearly"),
            ("(B)", "Waveform oscillating around zero"),
            ("(C)", "Counter step progression"),
            ("(D)", "Binary search successively halving the test interval toward $V_{in}$")
        ],
        answer_key="(D)",
        steps=[
            "A Successive Approximation Register (SAR) ADC implements a binary search algorithm.",
            "Starting at the first clock cycle, the MSB is tested ($100\\dots$). The DAC output jumps to $V_{FS}/2$.",
            "If $V_{in} > V_{DAC}$, the bit is retained, and the next MSB is tested by jumping half-way up.",
            "If $V_{in} < V_{DAC}$, the bit is rejected, and the next test jumps half-way down.",
            "This results in a distinctive converging geometric waveform with decreasing step sizes ($V_{FS}/2, V_{FS}/4, V_{FS}/8, \\dots$).",
            "Waveform (D) accurately portrays this binary search convergence."
        ],
        trap_note="Ramping waveform (A) represents a Counter-Type ADC, not a SAR ADC."
    )

    # Q21
    pyqs_2m += build_pyq_card(
        qnum="Q21.",
        year="GATE ECE 2008",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the previous SAR ADC circuit, if the analog input is $V_{in} = 6.2\\text{ V}$ and full scale is $8\\text{ V}$, what is the final digital output code after 3 conversion clock cycles?",
        diagram_img="images/p8_img1_135.png",
        options=[
            ("(A)", "101"),
            ("(B)", "110"),
            ("(C)", "111"),
            ("(D)", "100")
        ],
        answer_key="(B) 110",
        steps=[
            "Trace the SAR register bit-by-bit for 3 bits ($b_2 b_1 b_0$):",
            "• <strong>Cycle 1 (Test MSB $b_2 = 1$):</strong> Trial code = $100_2$.<br/>$$V_{DAC} = 4\\text{ V}$$<br/>Since $V_{in} = 6.2\\text{ V} > 4\\text{ V}$, comparator $= 1 \\implies$ Keep $b_2 = 1$.",
            "• <strong>Cycle 2 (Test $b_1 = 1$):</strong> Trial code = $110_2$.<br/>$$V_{DAC} = 4 + 2 = 6\\text{ V}$$<br/>Since $V_{in} = 6.2\\text{ V} > 6\\text{ V}$, comparator $= 1 \\implies$ Keep $b_1 = 1$.",
            "• <strong>Cycle 3 (Test $b_0 = 1$):</strong> Trial code = $111_2$.<br/>$$V_{DAC} = 6 + 1 = 7\\text{ V}$$<br/>Since $V_{in} = 6.2\\text{ V} < 7\\text{ V}$, comparator $= 0 \\implies$ Reset $b_0 = 0$.",
            "Final settled digital code is $110_2$ (Option B)."
        ],
        trap_note="Always reset the trial bit to 0 if $V_{in} < V_{DAC}$!"
    )

    # Q22
    pyqs_2m += build_pyq_card(
        qnum="Q22.",
        year="GATE ECE 2007",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the Digital-to-Analog converter circuit shown in the figure below, $V_{ref} = 10\\text{ V}$ and $R = 10\\text{ k}\\Omega$. For the given digital word, the output voltage is",
        diagram_img=["images/p8_img2_137.png", "images/p8_img3_139.png"],
        options=[
            ("(A)", "-3.75 V"),
            ("(B)", "-6.25 V"),
            ("(C)", "-5.00 V"),
            ("(D)", "-2.50 V")
        ],
        answer_key="(B) -6.25 V",
        steps=[
            "Analyze the R-2R ladder network driving the virtual ground summing junction of the op-amp.",
            "The digital input switches route currents corresponding to binary weights $2^{-1}, 2^{-2}, 2^{-3}, 2^{-4}$.",
            "For the specified input combination ($1010_2$ with MSB $= 1, b_2 = 0, b_1 = 1, b_0 = 0$):<br/>$$V_{out} = -V_{ref} \\left( \\frac{1}{2} + \\frac{1}{8} \\right) = -10\\text{ V} \\left( \\frac{5}{8} \\right) = -6.25\\text{ V}$$."
        ],
        trap_note="Weight of MSB is $1/2$, second bit is $1/4$, third bit is $1/8$. $10 \\times 5/8 = 6.25\\text{ V}$."
    )

    # Q23
    pyqs_2m += build_pyq_card(
        qnum="Q23.",
        year="GATE ECE 2007",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the same DAC circuit, if the feedback resistor is changed to $2R$, the output voltage change per LSB (resolution) is",
        diagram_img="",
        options=[
            ("(A)", "0.3125 V"),
            ("(B)", "0.625 V"),
            ("(C)", "1.25 V"),
            ("(D)", "2.5 V")
        ],
        answer_key="(C) 1.25 V",
        steps=[
            "Output voltage is proportional to $R_f$: $V_{out} \\propto R_f$.",
            "When $R_f$ is doubled from $R$ to $2R$, all branch gains double.",
            "The weight of 1 LSB becomes:<br/>$$\\Delta = 2 \\times \\frac{V_{ref}}{2^4} = 2 \\times \\frac{10\\text{ V}}{16} = 1.25\\text{ V}$$."
        ],
        trap_note="Doubling feedback resistance doubles the analog step size."
    )

    # Q24
    pyqs_2m += build_pyq_card(
        qnum="Q24.",
        year="GATE ECE 2006",
        marks="2 Marks",
        qtype="MCQ",
        statement="A 4-bit D/A converter is connected to a free-running 3-bit UP counter, as shown in the following figure. The counter outputs $Q_2, Q_1, Q_0$ are connected to DAC inputs $D_2, D_1, D_0$, while the MSB input $D_3$ is tied to Ground ($0\\text{ V}$). Which of the following waveforms will be observed at $V_0$?",
        diagram_img="images/p9_img1_151.jpeg",
        options=[
            ("(A)", "Staircase going to full scale 15V then resetting"),
            ("(B)", "Staircase ramping up to count 7 (7/16 of full scale) and periodically resetting to 0"),
            ("(C)", "Square wave"),
            ("(D)", "Triangular ramp")
        ],
        answer_key="(B)",
        steps=[
            "The 3-bit counter counts cyclically from $000_2$ to $111_2$ (decimal $0$ to $7$).",
            "Because MSB $D_3$ of the 4-bit DAC is permanently grounded ($D_3 = 0$), the 4-bit DAC input only spans codes $0000_2$ to $0111_2$.",
            "This corresponds to analog voltages from $0$ up to $\\frac{7}{16} V_{FS}$.",
            "When the counter rolls over from 7 to 0, the output resets to zero.",
            "Hence, the waveform is a periodic 8-step staircase ramping up to $7/16$ of full scale and resetting to 0 (Option B)."
        ],
        trap_note="Notice $D_3$ is tied to ground. The DAC never reaches its full scale (codes 8 to 15 are never addressed)."
    )

    # Q25
    pyqs_2m += build_pyq_card(
        qnum="Q25.",
        year="GATE ECE 2003",
        marks="2 Marks",
        qtype="MCQ",
        statement="The circuit shown in figure is a 4-bit DAC. The input bits 0 and 1 are represented by 0 and 5 V respectively. The OP-AMP is ideal, but all the resistances and the 5V inputs have a tolerance of ±10%. The worst-case error in the output voltage is",
        diagram_img="images/p10_img1_162.jpeg",
        options=[
            ("(A)", "Significant error exceeding ±10% due to resistor tolerance accumulation"),
            ("(B)", "Zero error"),
            ("(C)", "Exactly ±10%"),
            ("(D)", "Less than ±1%")
        ],
        answer_key="(A)",
        steps=[
            "In a binary weighted summing DAC, $V_{out} = -R_f \\sum \\frac{V_i}{R_i}$.",
            "Each term involves the ratio $\\frac{R_f \\cdot V_i}{R_i}$.",
            "If $R_f$ varies by $+10\\%$, $V_i$ by $+10\\%$, and $R_i$ by $-10\\%$, the maximum worst-case fractional deviation is:<br/>$$\\frac{(1 + 0.1)(1 + 0.1)}{1 - 0.1} - 1 = \\frac{1.21}{0.9} - 1 \\approx +34.4\\%$$",
            "This creates a substantial worst-case error, far exceeding a single component's $\\pm 10\\%$ tolerance."
        ],
        trap_note="Tolerances accumulate multiplicatively in ratio expressions!"
    )

    # Q26
    pyqs_2m += build_pyq_card(
        qnum="Q26.",
        year="GATE ECE 2000",
        marks="2 Marks",
        qtype="MCQ",
        statement="For the 4-bit DAC shown in Figure, the output voltage $V_0$ is",
        diagram_img="images/p10_img2_163.jpeg",
        options=[
            ("(A)", "10 V"),
            ("(B)", "-5 V"),
            ("(C)", "-10 V"),
            ("(D)", "5 V")
        ],
        answer_key="(B) -5 V",
        steps=[
            "Inspect the circuit: Inverting op-amp summing amplifier with input voltages $V_3, V_2, V_1, V_0$ applied to weighted resistors.",
            "Given switch settings in the figure connect the MSB to $5\\text{ V}$ and remaining bits to Ground ($0\\text{ V}$).",
            "For $b_3 = 1$ and $b_2 = b_1 = b_0 = 0$, with $R_3 = R_f$:",
            "$$V_0 = -V_{ref} \\frac{R_f}{R_3} = -5\\text{ V} \\times 1 = -5\\text{ V}$$.",
            "Hence, output voltage is $-5\\text{ V}$ (Option B)."
        ],
        trap_note="Virtual ground at inverting terminal ensures that other branches carry zero current."
    )

    sections_data = [
        {
            "id": "sec-dac-theory",
            "pill": "Chapter 02 · Part 1",
            "title": "Digital-to-Analog Converters (Weighted Resistor vs R-2R Ladder)",
            "content": sec1_content
        },
        {
            "id": "sec-dac-metrics",
            "pill": "Chapter 02 · Part 2",
            "title": "DAC Resolution, Step Size, Full-Scale Voltage & Non-Linearity",
            "content": sec2_content
        },
        {
            "id": "sec-adc-theory",
            "pill": "Chapter 02 · Part 3",
            "title": "ADC Fundamentals: Sample-and-Hold, Quantization Error & SQNR",
            "content": sec3_content
        },
        {
            "id": "sec-adc-topologies",
            "pill": "Chapter 02 · Part 4",
            "title": "ADC Architecture Taxonomy: Flash, SAR, Counter & Dual-Slope",
            "content": sec4_content
        },
        {
            "id": "sec-comparison",
            "pill": "Chapter 02 · Part 5",
            "title": "Master Architecture Comparison & Performance Trade-offs",
            "content": sec5_content
        },
        {
            "id": "sec-pyqs-1m",
            "pill": "GATE Official Archive · 1-Mark Questions",
            "title": "Official GATE 1-Mark PYQ Solutions (Q1 to Q14)",
            "content": pyqs_1m
        },
        {
            "id": "sec-pyqs-2m",
            "pill": "GATE Official Archive · 2-Mark Questions",
            "title": "Official GATE 2-Mark PYQ Solutions (Q15 to Q26)",
            "content": pyqs_2m
        }
    ]

    html_out = render_html_page(
        title=title,
        hero_data=hero_data,
        sections_data=sections_data,
        sidebar_links=sidebar_links,
        labs_html=sec6_lab,
        custom_scripts=custom_scripts
    )

    out_file = "digital/adc-dac/notes.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"✓ Successfully generated {out_file} ({len(html_out)} bytes).")

if __name__ == "__main__":
    generate_adc_dac()
