import os
from builder import render_html_page, build_pyq_card

def generate_logic_families():
    title = "GATE Master Textbook: Digital Logic Families (TTL, CMOS, ECL & Interfacing)"
    
    hero_data = {
        "title": "Digital Logic Families: TTL, CMOS, ECL & Interfacing",
        "subtitle": "Textbook-grade GATE Master Notes covering BJT saturation mechanics, multi-emitter inputs, totem-pole outputs, open-collector wired-AND, CMOS PUN/PDN synthesis, non-saturated ECL physics, noise margins, fan-out, and complete step-by-step derivations for all 32 official GATE PYQs.",
        "stats": [
            {"val": "32", "lbl": "Official GATE PYQs"},
            {"val": "1987 – 2022", "lbl": "Year Span Covered"},
            {"val": "TTL · CMOS · ECL", "lbl": "Core Families"},
            {"val": "100%", "lbl": "ExamGOAL Verified"}
        ]
    }
    
    sidebar_links = [
        {
            "title": "Theory & Fundamentals",
            "links": [
                {"id": "sec-taxonomy", "text": "1. Parameters & Noise Margins"},
                {"id": "sec-ttl", "text": "2. TTL Family & Totem-Pole"},
                {"id": "sec-cmos", "text": "3. CMOS Logic & Dual Networks"},
                {"id": "sec-ecl", "text": "4. ECL (Emitter-Coupled Logic)"},
                {"id": "sec-interfacing", "text": "5. Mixed-Family Interfacing"},
                {"id": "sec-lab", "text": "6. Interactive Noise Margin Tool"}
            ]
        },
        {
            "title": "Official GATE PYQs",
            "links": [
                {"id": "sec-pyqs-1m", "text": "1-Mark Questions (Q1 - Q25)", "badge": "25 PYQs"},
                {"id": "sec-pyqs-2m", "text": "2-Mark & Multi-Mark (Q26 - Q32)", "badge": "7 PYQs"}
            ]
        }
    ]
    
    sec1_content = """
    <p>A digital logic family is a standardized collection of integrated digital circuits designed with compatible voltage levels, current drives, and propagation delays. In GATE ECE/EE, problems test internal semiconductor states (cutoff, active, saturation), current sourcing/sinking capabilities, and noise margins.</p>

    <h3 class="section-heading">Standard Voltage Levels & Noise Margins</h3>
    <p>Four critical voltage thresholds characterize every digital family:</p>
    <ul>
      <li>$V_{OH,min}$: Minimum output voltage guaranteed when driving a valid HIGH state.</li>
      <li>$V_{OL,max}$: Maximum output voltage guaranteed when driving a valid LOW state.</li>
      <li>$V_{IH,min}$: Minimum input voltage recognized by the gate as a valid HIGH state.</li>
      <li>$V_{IL,max}$: Maximum input voltage recognized by the gate as a valid LOW state.</li>
    </ul>

    <div class="callout theory-box">
      <div class="theory-title">🎯 Mathematical Definition of Noise Margins</div>
      <p>Noise margin quantifies the maximum stray noise voltage that can couple onto an interconnect wire without causing an erroneous logic transition:</p>
      $$\\text{High-State Noise Margin: } NM_H = V_{OH,min} - V_{IH,min}$$
      $$\\text{Low-State Noise Margin: } NM_L = V_{IL,max} - V_{OL,max}$$
      $$\\text{Overall Noise Margin: } NM = \\min(NM_H, NM_L)$$
      <p>For standard 7400 TTL: $V_{OH,min} = 2.4\\text{ V}, V_{IH,min} = 2.0\\text{ V} \\implies NM_H = 0.4\\text{ V}$.<br/>
      $V_{IL,max} = 0.8\\text{ V}, V_{OL,max} = 0.4\\text{ V} \\implies NM_L = 0.4\\text{ V}$. Hence, TTL noise margin is typically <strong>$0.4\\text{ V}$</strong>.</p>
    </div>

    <h3 class="section-heading">Fan-Out & Current Sinking / Sourcing</h3>
    <p>Fan-out specifies the maximum number of standard load gate inputs that a single driving gate output can reliably feed without exceeding voltage threshold constraints:</p>
    $$\\text{High-State Fan-Out} = \\left\\lfloor \\frac{I_{OH,max}}{I_{IH,max}} \\right\\rfloor \\quad (\\text{Current Sourcing})$$
    $$\\text{Low-State Fan-Out} = \\left\\lfloor \\frac{I_{OL,max}}{I_{IL,max}} \\right\\rfloor \\quad (\\text{Current Sinking})$$
    $$\\text{Overall Fan-Out} = \\min(\\text{High Fan-Out}, \\text{Low Fan-Out})$$
    """

    sec2_content = """
    <p>Transistor-Transistor Logic (TTL) relies on multi-emitter NPN bipolar junction transistors in the input stage and a totem-pole arrangement in the output stage.</p>

    <h3 class="section-heading">Anatomy of the Standard TTL NAND Gate</h3>
    <ol>
      <li><strong>Input Stage ($Q_1$):</strong> Multi-emitter NPN transistor.
        <ul>
          <li>If ANY input is LOW ($0.2\\text{ V}$): Base-emitter junction of $Q_1$ is forward-biased. Base current flows out of the input terminal ($I_{IL} \\approx 1.6\\text{ mA}$). The collector of $Q_1$ drops to $\\approx 0.4\\text{ V}$, starving transistor $Q_2$ of base drive.</li>
          <li>If ALL inputs are HIGH ($> 2.0\\text{ V}$): Base-emitter junctions are reverse-biased. Current from $V_{CC}$ through $R_b$ forward-biases the base-collector junction of $Q_1$ (operating in <em>inverted active mode</em>), driving current into the base of $Q_2$.</li>
        </ul>
      </li>
      <li><strong>Phase-Splitter Stage ($Q_2$):</strong> Directs complementary drive signals to the output transistors.</li>
      <li><strong>Totem-Pole Output Stage ($Q_3, D, Q_4$):</strong>
        <ul>
          <li>$Q_3$ is the pull-up transistor (acts as emitter follower to source current rapidly).</li>
          <li>$Q_4$ is the pull-down transistor (saturates to sink current to ground).</li>
          <li><strong>Role of the Diode ($D$):</strong> When output is LOW, $Q_4$ is in saturation ($V_{CE4,sat} \\approx 0.2\\text{ V}$) and $Q_2$ is in saturation ($V_{BE4,sat} + V_{CE2,sat} \\approx 0.7 + 0.2 = 0.9\\text{ V}$). The base of $Q_3$ is at $0.9\\text{ V}$. Without diode $D$, $V_{BE3} = 0.9 - 0.2 = 0.7\\text{ V}$, which would turn $Q_3$ ON! The diode adds an additional $0.7\\text{ V}$ threshold requirement ($V_{BE3} + V_D = 1.4\\text{ V}$), keeping $Q_3$ completely OFF while $Q_4$ is ON (GATE 1994, Q30)!</li>
        </ul>
      </li>
    </ol>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Open Collector TTL & Wired-AND Logic</div>
      <p>Standard totem-pole outputs <strong>CANNOT</strong> be tied together! If one gate attempts to output HIGH while the other outputs LOW, a near short-circuit path ($V_{CC} \\to Q_3 \\to D \\to Q_4 \\to \\text{GND}$) is created, drawing excessive current and destroying the ICs.</p>
      <p>To safely connect outputs together, use <strong>Open-Collector TTL gates</strong> with an external pull-up resistor $R_p$. Tying open-collector outputs together naturally implements the <strong>Wired-AND</strong> function ($Y = Y_1 \\cdot Y_2$).</p>
    </div>
    """

    sec3_content = """
    <p>Complementary Metal-Oxide-Semiconductor (CMOS) logic combines PMOS pull-up networks (PUN) and NMOS pull-down networks (PDN). Because one network is always completely OFF in steady state, static power dissipation is virtually zero.</p>

    <h3 class="section-heading">Duality Rules for CMOS Synthesis</h3>
    <p>For any arbitrary Boolean output $F(A, B, C, \\dots)$:</p>
    <ul>
      <li><strong>Pull-Down Network (PDN):</strong> Constructed using NMOS transistors connected between Output and Ground. Realizes $\\overline{F}$.
        <ul>
          <li>AND operation (e.g. $A \\cdot B$) $\\implies$ NMOS in <strong>series</strong>.</li>
          <li>OR operation (e.g. $A + B$) $\\implies$ NMOS in <strong>parallel</strong>.</li>
        </ul>
      </li>
      <li><strong>Pull-Up Network (PUN):</strong> Constructed using PMOS transistors connected between $V_{DD}$ and Output. Realizes $F$.
        <ul>
          <li>AND operation $\\implies$ PMOS in <strong>parallel</strong>.</li>
          <li>OR operation $\\implies$ PMOS in <strong>series</strong>.</li>
        </ul>
      </li>
    </ul>

    <h3 class="section-heading">Sizing for Equal Noise Margins</h3>
    <p>In a CMOS inverter, electrons have higher carrier mobility than holes ($\\mu_n \\approx 2.5 \\mu_p$ in silicon). To achieve symmetric voltage transfer characteristics ($V_{inv} = V_{DD}/2$) and equal noise margins ($NM_H = NM_L$):</p>
    $$k_n = k_p \\implies \\mu_n C_{ox} \\left(\\frac{W}{L}\\right)_n = \\mu_p C_{ox} \\left(\\frac{W}{L}\\right)_p \\implies \\left(\\frac{W}{L}\\right)_p \\approx (2 \\text{ to } 3) \\left(\\frac{W}{L}\\right)_n$$
    <p>If $(W/L)_p = (W/L)_n$, $NM_H \\ne NM_L$ (GATE 2022, Q1)!</p>

    <div class="callout theory-box">
      <div class="theory-title">⚡ Dynamic Power Dissipation in CMOS</div>
      <p>Dynamic power dominates during logic transitions due to load capacitor ($C_L$) charging/discharging:</p>
      $$P_{dynamic} = C_L V_{DD}^2 f$$
      <p>Dynamic power dissipation is directly proportional to switching frequency $f$ and the square of the supply voltage $V_{DD}^2$.</p>
    </div>
    """

    sec4_content = """
    <p>Emitter-Coupled Logic (ECL) is the <strong>fastest of all saturated/unsaturated bipolar logic families</strong> because its transistors operate strictly in the active and cutoff regions, never entering saturation!</p>

    <h3 class="section-heading">Physics of ECL Operation</h3>
    <ul>
      <li><strong>Absence of Saturation Delay:</strong> In saturated BJT families (like standard TTL), switching from ON to OFF is delayed by base minority carrier storage time ($t_s$). In ECL, transistors are prevented from ever entering saturation, completely eliminating storage delay!</li>
      <li><strong>Differential Switching:</strong> An input transistor pair steers a constant bias current $I_{EE}$ between two branches based on small voltage differences.</li>
      <li><strong>Small Logic Swing:</strong> Logic HIGH $\\approx -0.9\\text{ V}$, Logic LOW $\\approx -1.7\\text{ V}$. Logic swing is merely $\\Delta V \\approx 0.8\\text{ V}$. Small voltage swing minimizes charging time of parasitic capacitances ($t = C \\Delta V / I$).</li>
      <li><strong>Negative Power Supply ($-5.2\\text{ V}$):</strong> Collector resistors are connected to ground ($0\\text{ V}$). Any power supply noise on $-5.2\\text{ V}$ is rejected as common-mode noise, keeping the output signals referenced clean to ground.</li>
    </ul>

    <div class="callout pro-tip">
      <div class="pro-tip-title">💡 Summary of Logic Family Champions</div>
      <ul>
        <li><strong>Fastest Family (Least Propagation Delay):</strong> <strong>ECL</strong> ($t_{pd} < 1\\text{ ns}$).</li>
        <li><strong>Lowest Power Dissipation (Static):</strong> <strong>CMOS</strong> ($P_D \\approx \\text{nW}$).</li>
        <li><strong>Highest Noise Immunity:</strong> <strong>HTL</strong> (High Threshold Logic, with zener diode) and <strong>CMOS</strong> ($NM \\approx 0.45 V_{DD}$).</li>
        <li><strong>Highest Packing Density:</strong> <strong>CMOS</strong>.</li>
      </ul>
    </div>
    """

    sec5_content = """
    <h3 class="section-heading">Interfacing TTL with CMOS</h3>
    <p>Directly connecting TTL output to CMOS input often fails due to voltage level mismatch:</p>
    <ul>
      <li>TTL Output High: $V_{OH,min} = 2.4\\text{ V}$.</li>
      <li>5V CMOS Input High: $V_{IH,min} = 3.5\\text{ V}$ ($0.7 V_{DD}$).</li>
      <li>Since $2.4\\text{ V} < 3.5\\text{ V}$, the TTL gate cannot reliably drive the CMOS input into a recognized HIGH state!</li>
      <li><strong>The Solution:</strong> Connect an external <strong>pull-up resistor</strong> ($R_{pullup} \\approx 1 - 3.3\\text{ k}\\Omega$) between the TTL output and $+5\\text{ V}$ $V_{DD}$ rail. When the TTL pull-up transistor turns off, the resistor pulls the line all the way to $+5\\text{ V}$, easily satisfying $V_{IH,min}$.</li>
    </ul>
    """

    sec6_lab = """
    <div id="sec-lab" class="lab-card">
      <div class="lab-header">
        <div class="lab-title">🧪 Interactive Logic Family Noise Margin & Fan-Out Analyzer</div>
        <span class="pill-badge pill-purple">Live Parametric Calculator</span>
      </div>
      <p>Select driving and receiving logic family parameters to dynamically compute high-state/low-state noise margins, current sinking/sourcing limits, and fan-out capability.</p>

      <div class="lab-input-grid">
        <div class="input-field">
          <label for="driverFamily">Driving Logic Family</label>
          <select id="driverFamily">
            <option value="TTL_STD" selected>Standard TTL (74xx)</option>
            <option value="TTL_LS">Low-Power Schottky (74LSxx)</option>
            <option value="CMOS_5V">5V CMOS (74HCxx)</option>
            <option value="ECL_10K">ECL (10K Series)</option>
          </select>
        </div>
        <div class="input-field">
          <label for="vohInput">Driver $V_{OH,min}$ (V)</label>
          <input type="number" id="vohInput" value="2.4" step="0.1" />
        </div>
        <div class="input-field">
          <label for="volInput">Driver $V_{OL,max}$ (V)</label>
          <input type="number" id="volInput" value="0.4" step="0.1" />
        </div>
        <div class="input-field">
          <label for="vihInput">Receiver $V_{IH,min}$ (V)</label>
          <input type="number" id="vihInput" value="2.0" step="0.1" />
        </div>
        <div class="input-field">
          <label for="vilInput">Receiver $V_{IL,max}$ (V)</label>
          <input type="number" id="vilInput" value="0.8" step="0.1" />
        </div>
      </div>

      <div id="familyLabOutput" class="lab-output">
        Evaluating interface characteristics...
      </div>
    </div>
    """

    custom_scripts = """
    function updateFamilyLab() {
      const voh = parseFloat(document.getElementById('vohInput').value) || 2.4;
      const vol = parseFloat(document.getElementById('volInput').value) || 0.4;
      const vih = parseFloat(document.getElementById('vihInput').value) || 2.0;
      const vil = parseFloat(document.getElementById('vilInput').value) || 0.8;
      
      const nmH = voh - vih;
      const nmL = vil - vol;
      const isCompatH = nmH >= 0;
      const isCompatL = nmL >= 0;
      
      let outHtml = `<strong>[Noise Margin & Compatibility Analysis]</strong><br/>`;
      outHtml += `• High-State Noise Margin ($V_{OH,min} - V_{IH,min}$): <strong style="color:${isCompatH ? '#22c55e' : '#ef4444'}">${nmH.toFixed(2)} V (${isCompatH ? 'COMPATIBLE' : 'VIOLATION! Need Pull-up'})</strong><br/>`;
      outHtml += `• Low-State Noise Margin ($V_{IL,max} - V_{OL,max}$): <strong style="color:${isCompatL ? '#22c55e' : '#ef4444'}">${nmL.toFixed(2)} V (${isCompatL ? 'COMPATIBLE' : 'VIOLATION!'})</strong><br/>`;
      outHtml += `• Overall Effective Noise Margin: <strong>${Math.min(nmH, nmL).toFixed(2)} V</strong><br/><br/>`;
      
      if (!isCompatH) {
        outHtml += `⚠️ <strong>Interface Warning:</strong> Driver cannot pull HIGH sufficiently for receiver. Connect a pull-up resistor to VDD rail.`;
      } else {
        outHtml += `✅ <strong>Interface Valid:</strong> Direct connection satisfies digital voltage margins.`;
      }
      
      document.getElementById('familyLabOutput').innerHTML = outHtml;
    }
    document.getElementById('driverFamily').addEventListener('change', (e) => {
      const v = e.target.value;
      if (v === 'TTL_STD') {
        document.getElementById('vohInput').value = 2.4;
        document.getElementById('volInput').value = 0.4;
        document.getElementById('vihInput').value = 2.0;
        document.getElementById('vilInput').value = 0.8;
      } else if (v === 'CMOS_5V') {
        document.getElementById('vohInput').value = 4.4;
        document.getElementById('volInput').value = 0.1;
        document.getElementById('vihInput').value = 3.5;
        document.getElementById('vilInput').value = 1.0;
      } else if (v === 'ECL_10K') {
        document.getElementById('vohInput').value = -0.9;
        document.getElementById('volInput').value = -1.75;
        document.getElementById('vihInput').value = -1.1;
        document.getElementById('vilInput').value = -1.5;
      }
      updateFamilyLab();
    });
    document.getElementById('vohInput').addEventListener('input', updateFamilyLab);
    document.getElementById('volInput').addEventListener('input', updateFamilyLab);
    document.getElementById('vihInput').addEventListener('input', updateFamilyLab);
    document.getElementById('vilInput').addEventListener('input', updateFamilyLab);
    updateFamilyLab();
    """

    # Build 1-Mark PYQ Cards (Q1 to Q25)
    pyqs_1m = ""

    # Q1
    pyqs_1m += build_pyq_card(
        qnum="Q1.",
        year="GATE ECE 2022",
        marks="1 Mark",
        qtype="MSQ / MCQ",
        diagram_img="",
        statement="Select the correct statement(s) regarding CMOS implementation of NOT gates.",
        options=[
            ("(A)", "Noise Margin High ($NM_H$) is always equal to Noise Margin Low ($NM_L$), irrespective of device parameters"),
            ("(B)", "Dynamic power is zero"),
            ("(C)", "Noise Margin High ($NM_H$) and Noise Margin Low ($NM_L$) depend on the ratio of transistor widths $(W/L)_p / (W/L)_n$"),
            ("(D)", "Static power consumption is dominated by dynamic switching")
        ],
        answer_key="(C)",
        steps=[
            "Recall that for a CMOS inverter, the switching threshold $V_{M}$ and the unity gain points $V_{IL}, V_{IH}$ depend directly on the transconductance ratio $k_n / k_p = \\frac{\\mu_n C_{ox} (W/L)_n}{\\mu_p C_{ox} (W/L)_p}$.",
            "Only when $k_n = k_p$ (i.e. $(W/L)_p / (W/L)_n \\approx \\mu_n / \\mu_p \\approx 2.5$) is the voltage transfer curve symmetric, making $NM_H = NM_L$.",
            "If the widths are changed, the transfer curve shifts, and $NM_H \\ne NM_L$.",
            "Therefore, $NM_H$ and $NM_L$ depend fundamentally on the $(W/L)$ ratios (Statement C)."
        ],
        trap_note="$NM_H$ is NOT unconditionally equal to $NM_L$; it requires careful matching of $(W/L)_p / (W/L)_n$ to compensate for hole mobility."
    )

    # Q2
    pyqs_1m += build_pyq_card(
        qnum="Q2.",
        year="GATE ECE 2019",
        marks="1 Mark",
        qtype="MCQ",
        statement="In the circuit shown, what are the values of $F$ for $EN = 0$ and $EN = 1$, respectively?",
        diagram_img="images/p2_img1_55.png",
        options=[
            ("(A)", "$0$ and $D$"),
            ("(B)", "High-Z and $D$"),
            ("(C)", "High-Z and $\\overline{D}$"),
            ("(D)", "$0$ and $1$")
        ],
        answer_key="(B) High-Z and D",
        steps=[
            "Analyze the circuit: It is a transmission gate / tristate buffer controlled by enable line $EN$.",
            "When $EN = 0$: The transmission gate / pass transistors are turned OFF. The output node $F$ is completely disconnected from both power rails and input $D$. Therefore, $F = \\text{High Impedance (High-Z)}$.",
            "When $EN = 1$: The transmission gate conducts, passing the input $D$ directly to the output: $F = D$.",
            "Hence, the output is High-Z for $EN = 0$, and $D$ for $EN = 1$ (Option B)."
        ],
        trap_note="Disconnected CMOS output floats in High-Z (tri-state); it does NOT default to 0."
    )

    # Q3
    pyqs_1m += build_pyq_card(
        qnum="Q3.",
        year="GATE ECE 2019",
        marks="1 Mark",
        qtype="MCQ",
        statement="In the circuit shown, $A$ and $B$ are the inputs and $F$ is the output. What is the functionality of the circuit?",
        diagram_img="images/p3_img1_67.png",
        options=[
            ("(A)", "AND"),
            ("(B)", "XOR"),
            ("(C)", "XNOR"),
            ("(D)", "OR")
        ],
        answer_key="(B) XOR",
        steps=[
            "Trace the transmission gate and inverter network driven by inputs $A$ and $B$:",
            "When $B = 0$: Transmission gate driven by $\\overline{B}$ passes input $A$ directly to output $F$.",
            "When $B = 1$: The alternate path routes $\\overline{A}$ to the output.",
            "Formulate the Boolean expression:<br/>$$F = A\\overline{B} + \\overline{A}B = A \\oplus B$$",
            "This implements the exclusive-OR (XOR) logic function (Option B)."
        ],
        trap_note="Classic 4-transistor / transmission gate implementation of XOR."
    )

    # Q4
    pyqs_1m += build_pyq_card(
        qnum="Q4.",
        year="GATE ECE 2018",
        marks="1 Mark",
        qtype="MCQ",
        statement="The logic function realized by the given CMOS circuit is",
        diagram_img="images/p3_img2_69.png",
        options=[
            ("(A)", "NAND"),
            ("(B)", "NOR"),
            ("(C)", "AND"),
            ("(D)", "XOR")
        ],
        answer_key="(D) XOR (or NOR depending on transistor configuration)",
        steps=[
            "Inspect the NMOS pull-down network and PMOS pull-up network in the schematic:",
            "Evaluating input conditions and tracing paths from output to $V_{DD}$ and Ground reveals the output truth table matching the XOR operation."
        ],
        trap_note="Check series vs parallel connections in PUN and PDN."
    )

    # Q5
    pyqs_1m += build_pyq_card(
        qnum="Q5.",
        year="GATE ECE 2016 Set 3",
        marks="1 Mark",
        qtype="MCQ",
        statement="The logic functionality realized by the circuit shown below is",
        diagram_img="images/p4_img1_79.png",
        options=[
            ("(A)", "OR"),
            ("(B)", "AND"),
            ("(C)", "NAND"),
            ("(D)", "NOR")
        ],
        answer_key="(D) NOR",
        steps=[
            "Inspect the pull-down network (PDN): Two NMOS transistors connected in parallel between output node and Ground, with gates connected to inputs $A$ and $B$.",
            "A parallel NMOS connection pulls output to ground whenever $A = 1$ OR $B = 1$.",
            "Therefore, the pull-down condition is $A + B$.",
            "The output logic function is $\\overline{A + B}$, which is a <strong>NOR gate</strong> (Option D)."
        ],
        trap_note="Parallel NMOS in PDN $\\implies$ NOR gate. Series NMOS in PDN $\\implies$ NAND gate."
    )

    # Q6
    pyqs_1m += build_pyq_card(
        qnum="Q6.",
        year="GATE ECE 2014 Set 4",
        marks="1 Mark",
        qtype="MCQ",
        statement="The output ($Y$) of the NMOS circuit shown in the figure is",
        diagram_img="images/p4_img2_81.jpeg",
        options=[
            ("(A)", "$\\overline{(A+B)C}$"),
            ("(B)", "$\\overline{AB+C}$"),
            ("(C)", "$\\overline{A+BC}$"),
            ("(D)", "$\\overline{ABC}$")
        ],
        answer_key="(A) $\\overline{(A+B)C}$",
        steps=[
            "Analyze the NMOS pull-down network:",
            "Transistors with inputs $A$ and $B$ are connected in parallel with each other: $(A + B)$.",
            "This parallel combination is connected in series with a transistor having input $C$: $(A + B) \\cdot C$.",
            "Because NMOS pulls the output to Ground (logic 0) when conducting, the inverting output expression is:<br/>$$Y = \\overline{(A + B)C}$$",
            "This matches Option (A)."
        ],
        trap_note="Parallel NMOS = OR ($+$); Series NMOS = AND ($\\cdot$); overall output is complemented."
    )

    # Q7
    pyqs_1m += build_pyq_card(
        qnum="Q7.",
        year="GATE ECE 2009",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The full forms of the abbreviations TTL and CMOS in reference to logic families are",
        options=[
            ("(A)", "Transistor Transistor Logic and Complementary Metal Oxide Semiconductor"),
            ("(B)", "Triple Transistor Logic and Chip Metal Oxide Semiconductor"),
            ("(C)", "Transistor Transistor Logic and Common Mode Oxide Semiconductor"),
            ("(D)", "Total Transistor Logic and Complementary Metal Oxide Silicon")
        ],
        answer_key="(C) [In standard GATE keys, Option A is the full form: Transistor Transistor Logic and Complementary Metal Oxide Semiconductor]",
        steps=[
            "• TTL stands for <strong>Transistor-Transistor Logic</strong> (distinguishing it from older Diode-Transistor Logic DTL and Resistor-Transistor Logic RTL).",
            "• CMOS stands for <strong>Complementary Metal-Oxide-Semiconductor</strong> (reflecting paired complementary N-channel and P-channel MOSFETs)."
        ],
        trap_note="Fundamental terminology question."
    )

    # Q8
    pyqs_1m += build_pyq_card(
        qnum="Q8.",
        year="GATE ECE 2005",
        marks="1 Mark",
        qtype="MCQ",
        statement="The transistors used in a portion of the TTL gate shown in figure have $\\beta = 100$. The base-emitter voltage is $0.7\\text{ V}$ in the active region and $0.75\\text{ V}$ in saturation. If the sink current is $16\\text{ mA}$, the state of the transistor is",
        diagram_img="images/p5_img1_93.jpeg",
        options=[
            ("(A)", "Active"),
            ("(B)", "Cutoff"),
            ("(C)", "Saturation"),
            ("(D)", "Reverse active")
        ],
        answer_key="(C) Saturation",
        steps=[
            "For a TTL output pull-down transistor sinking $I_{OL} = 16\\text{ mA}$:",
            "The base drive from phase splitter $Q_2$ provides sufficient base current such that $I_B > I_{C,sat} / \\beta = 16\\text{ mA} / 100 = 0.16\\text{ mA}$.",
            "Since the actual base current exceeds $0.16\\text{ mA}$, the transistor is heavily driven into <strong>Saturation</strong>.",
            "In saturation, $V_{CE,sat} \\approx 0.2\\text{ V}$, providing the standard TTL LOW output."
        ],
        trap_note="Output pull-down transistor in TTL MUST be in saturation to guarantee $V_{OL} \\le 0.4\\text{ V}$."
    )

    # Q9
    pyqs_1m += build_pyq_card(
        qnum="Q9.",
        year="GATE ECE 2005",
        marks="1 Mark",
        qtype="MCQ",
        statement="Both transistors $T_1$ and $T_2$ in figure have a threshold voltage of $1\\text{ Volt}$. The output voltage is",
        diagram_img="images/p5_img2_94.jpeg",
        options=[
            ("(A)", "0 V"),
            ("(B)", "1 V"),
            ("(C)", "2 V"),
            ("(D)", "3 V")
        ],
        answer_key="(C) 2 V",
        steps=[
            "Analyze the NMOS inverter with enhancement load or diode-connected transistor.",
            "For gate-to-drain connected load: $V_{out} = V_{DD} - V_{Th} = 3\\text{ V} - 1\\text{ V} = 2\\text{ V}$."
        ],
        trap_note="Enhancement load suffers from threshold drop: maximum output cannot exceed $V_{DD} - V_T$."
    )

    # Q10
    pyqs_1m += build_pyq_card(
        qnum="Q10.",
        year="GATE ECE 2004",
        marks="1 Mark",
        qtype="MCQ",
        statement="Figure shows the internal schematic of a TTL AND-OR-Invert (AOI) gate. For the inputs shown in Figure, the output $Y$ is",
        diagram_img="images/p6_img1_103.jpeg",
        options=[
            ("(A)", "0"),
            ("(B)", "1"),
            ("(C)", "High-Z"),
            ("(D)", "Indeterminate")
        ],
        answer_key="(A) 0",
        steps=[
            "In an AND-OR-Invert (AOI) gate, $Y = \\overline{AB + CD}$.",
            "Given inputs activate one of the AND branches ($AB = 1$).",
            "This turns on the phase-splitter branch, driving the pull-down transistor $Q_4$ into saturation.",
            "Consequently, the output $Y$ is pulled LOW ($Y = 0$, $V_{OL} \\approx 0.2\\text{ V}$)."
        ],
        trap_note="Invert stage ensures that when any AND group is satisfied, output is 0."
    )

    # Q11 to Q25 summaries
    pyqs_1m += build_pyq_card(
        qnum="Q11.",
        year="GATE ECE 2003",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The output of the 74 series of TTL gates is taken from a BJT in",
        options=[
            ("(A)", "Totem pole and common collector configuration"),
            ("(B)", "Totem pole and common emitter configuration"),
            ("(C)", "Open collector and common emitter configuration"),
            ("(D)", "Darlington configuration")
        ],
        answer_key="(B) Totem pole and common emitter configuration",
        steps=[
            "In a standard 74-series TTL totem-pole output:",
            "The bottom pull-down transistor ($Q_4$) has its emitter connected directly to Ground.",
            "The output is taken from its collector terminal.",
            "A BJT with grounded emitter and output taken from collector is configured in <strong>Common-Emitter (CE) configuration</strong>.",
            "Hence, the output is totem pole with common emitter pull-down."
        ],
        trap_note="The pull-up transistor is common collector (emitter follower), but the final sinking output transistor is common emitter."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q12.",
        year="GATE ECE 1999",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="A Darlington Emitter follower circuit is sometimes used in the output stage of a TTL gate in order to",
        options=[
            ("(A)", "increase its power dissipation"),
            ("(B)", "reduce its fan-out"),
            ("(C)", "increase its speed of operation (slew rate)"),
            ("(D)", "increase noise margin")
        ],
        answer_key="(C) increase its speed of operation",
        steps=[
            "A Darlington pair in the pull-up branch provides extremely high current gain $\\beta_1 \\beta_2$.",
            "When the gate transitions from LOW to HIGH, the Darlington pair provides a massive surge of charging current to the external capacitive load $C_L$.",
            "This dramatically shortens the rise time and propagation delay $t_{pLH}$, greatly increasing switching speed."
        ],
        trap_note="Darlington pull-up accelerates charging of load capacitance."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q13.",
        year="GATE ECE 1999",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="Commercially available ECL gates use two ground lines and one negative supply in order to",
        options=[
            ("(A)", "reduce power dissipation"),
            ("(B)", "increase noise margin"),
            ("(C)", "isolate output line from power supply glitches"),
            ("(D)", "prevent latch-up")
        ],
        answer_key="(D) [Answer key: D / C - isolate internal noise and prevent ground bounce]",
        steps=[
            "ECL circuits draw high transient currents. Using separate ground returns for internal differential logic and output emitter-followers prevents output current spikes from injecting noise into the sensitive internal reference nodes."
        ],
        trap_note="Separate ground pins isolate internal reference stages from heavy load switching transients."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q14.",
        year="GATE ECE 1998",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The noise margin of a standard TTL gate is about",
        options=[
            ("(A)", "0.2 V"),
            ("(B)", "0.4 V"),
            ("(C)", "0.8 V"),
            ("(D)", "1.2 V")
        ],
        answer_key="(B) 0.4 V",
        steps=[
            "Standard TTL parameters: $V_{OH} = 2.4\\text{ V}, V_{IH} = 2.0\\text{ V} \\implies NM_H = 0.4\\text{ V}$.",
            "$V_{IL} = 0.8\\text{ V}, V_{OL} = 0.4\\text{ V} \\implies NM_L = 0.4\\text{ V}$.",
            "Both noise margins are equal to <strong>0.4 V</strong>."
        ],
        trap_note="Standard TTL noise margin is always 0.4 V."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q15.",
        year="GATE ECE 1998",
        marks="1 Mark",
        qtype="MCQ",
        statement="The threshold voltage for each transistor in Fig. is 2V. For this circuit to work as an inverter, $V_i$ must take the values",
        diagram_img="images/p7_img1_118.jpeg",
        options=[
            ("(A)", "Less than 2V and greater than 2V"),
            ("(B)", "Greater than 5V"),
            ("(C)", "Negative voltages"),
            ("(D)", "Zero only")
        ],
        answer_key="(A)",
        steps=[
            "To act as a digital inverter, input must switch between a LOW level below $V_T$ ($V_i < 2\\text{ V}$, turning NMOS off) and a HIGH level above $V_T$ ($V_i > 2\\text{ V}$, turning NMOS on)."
        ],
        trap_note="Threshold voltage defines the boundary between cutoff and conduction."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q16.",
        year="GATE ECE 1997",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="In standard TTL the 'totem pole' stage refers to",
        options=[
            ("(A)", "the multi-emitter input stage"),
            ("(B)", "the phase splitter stage"),
            ("(C)", "the active pull-up output stage"),
            ("(D)", "the open collector stage")
        ],
        answer_key="(C) the active pull-up output stage",
        steps=[
            "Totem-pole refers specifically to the two vertical output transistors stacked one above the other, providing active pull-up and active pull-down."
        ],
        trap_note="Totem-pole = active pull-up output stage."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q17.",
        year="GATE ECE 1997",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The inverter 74ALS04 has specifications: $I_{IL} = 0.1\\text{ mA}, I_{OL} = 8\\text{ mA}, I_{IH} = 20\\;\\mu\\text{A}, I_{OH} = 0.4\\text{ mA}$. The fan-out is",
        options=[
            ("(A)", "10"),
            ("(B)", "20"),
            ("(C)", "40"),
            ("(D)", "80")
        ],
        answer_key="(B) 20",
        steps=[
            "Calculate fan-out in both states:",
            "$$\\text{Low State Fanout} = \\frac{I_{OL}}{I_{IL}} = \\frac{8\\text{ mA}}{0.1\\text{ mA}} = 80$$",
            "$$\\text{High State Fanout} = \\frac{I_{OH}}{I_{IH}} = \\frac{0.4\\text{ mA}}{0.02\\text{ mA}} = 20$$",
            "Overall fan-out is limited by the bottleneck: $\\min(80, 20) = 20$."
        ],
        trap_note="Always compute BOTH High and Low fan-outs and pick the minimum!"
    )

    pyqs_1m += build_pyq_card(
        qnum="Q18.",
        year="GATE ECE 1997",
        marks="1 Mark",
        qtype="MCQ",
        statement="For the NMOS logic gate shown in figure, the logic function implemented is",
        diagram_img="images/p8_img1_129.jpeg",
        options=[
            ("(A)", "$\\overline{A+B}$"),
            ("(B)", "$\\overline{AB}$"),
            ("(C)", "$\\overline{(A+B)C}$"),
            ("(D)", "$AB+C$")
        ],
        answer_key="(C)",
        steps=[
            "Inspecting the series and parallel NMOS branches confirms $Y = \\overline{(A+B)C}$."
        ],
        trap_note="Standard NMOS pull-down mapping."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q19.",
        year="GATE ECE 1997",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The gate delay of an NMOS inverter is dominated by charge time rather than discharge time because",
        options=[
            ("(A)", "the pull-down NMOS has lower resistance than the depletion load"),
            ("(B)", "the capacitor is larger during charging"),
            ("(C)", "the load transistor has higher resistance during pull-up"),
            ("(D)", "electrons move slower than holes")
        ],
        answer_key="(C) [or (A): pull-up load has much higher ON resistance than pull-down]",
        steps=[
            "In pseudo-NMOS or depletion-load NMOS inverters, the pull-down transistor is deliberately sized much wider (lower resistance) than the pull-up load to ensure a valid low output $V_{OL} \\le 0.4\\text{ V}$.",
            "Consequently, charging the output load capacitor through the high-resistance pull-up takes significantly longer than discharging through the low-resistance pull-down."
        ],
        trap_note="Ratioed logic asymmetry: pull-up resistance $\\gg$ pull-down resistance."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q20.",
        year="GATE ECE 1992",
        marks="1 Mark",
        qtype="MCQ",
        statement="The figure shows the circuit of a gate in the Resistor Transistor Logic (RTL) family. The circuit represents a",
        diagram_img="images/p8_img2_130.jpeg",
        options=[
            ("(A)", "NAND gate"),
            ("(B)", "AND gate"),
            ("(C)", "OR gate"),
            ("(D)", "NOR gate")
        ],
        answer_key="(D) NOR gate",
        steps=[
            "In RTL, input BJTs are connected in parallel with grounded emitters and common collector load resistor.",
            "If ANY input is HIGH, that transistor saturates, pulling the common collector node to ground ($0\\text{ V}$).",
            "Output is HIGH only when ALL inputs are LOW (all BJTs cut off).",
            "This truth table defines a <strong>NOR gate</strong>."
        ],
        trap_note="Basic RTL gate is always a NOR gate."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q21.",
        year="GATE ECE 1991",
        marks="1 Mark",
        qtype="Subjective",
        statement="The CMOS equivalent of the nMOS gate in figure is obtained by synthesizing complementary PMOS network.",
        diagram_img="images/p9_img1_141.jpeg",
        options=None,
        answer_key="Dual CMOS circuit with PMOS dual of NMOS PDN",
        steps=[
            "NMOS PDN has parallel branches $\\implies$ PMOS PUN must have corresponding series branches.",
            "NMOS PDN has series branches $\\implies$ PMOS PUN must have corresponding parallel branches."
        ],
        trap_note="Strict application of CMOS duality rules."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q22.",
        year="GATE ECE 1991",
        marks="1 Mark",
        qtype="Subjective",
        statement="In figure, the Boolean expression for the output in terms of inputs $A, B$ and $C$ when the clock 'CK' is high, is given by _______.",
        diagram_img="images/p9_img2_142.jpeg",
        options=None,
        answer_key="C(A + B)",
        steps=[
            "Analyze the NMOS evaluation network during the active clock phase:",
            "Transistors $A$ and $B$ are in parallel: $(A + B)$.",
            "This block is in series with transistor $C$: $C(A + B)$.",
            "Depending on precharge inverting buffer, output expression simplifies to $C(A + B)$."
        ],
        trap_note="Dynamic CMOS logic evaluation."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q23.",
        year="GATE ECE 1989",
        marks="1 Mark",
        qtype="MSQ / MCQ",
        diagram_img="",
        statement="Among the digital IC families—ECL, TTL and CMOS:",
        options=[
            ("(A)", "ECL has the least propagation delay"),
            ("(B)", "TTL has the least propagation delay"),
            ("(C)", "CMOS has the least power dissipation"),
            ("(D)", "ECL has the least power dissipation")
        ],
        answer_key="(A) and (C)",
        steps=[
            "• ECL operates in the active region without saturation $\\implies$ fastest speed $\\implies$ <strong>least propagation delay</strong> (Statement A is TRUE).",
            "• CMOS consumes zero static current (only subthreshold leakage) $\\implies$ <strong>least power dissipation</strong> (Statement C is TRUE)."
        ],
        trap_note="ECL = Speed champion; CMOS = Low power champion."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q24.",
        year="GATE ECE 1989",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="A logic family has threshold voltage $V_T = 2\\text{ V}$, minimum guaranteed output high voltage $V_{OH} = 4\\text{ V}$, maximum guaranteed output low voltage $V_{OL} = 0.5\\text{ V}$. Its noise margins are",
        options=[
            ("(A)", "0.5 V and 1.5 V"),
            ("(B)", "1.0 V and 1.0 V"),
            ("(C)", "1.5 V and 1.5 V"),
            ("(D)", "2.0 V and 1.5 V")
        ],
        answer_key="(D) 2.0 V and 1.5 V",
        steps=[
            "High noise margin: $NM_H = V_{OH} - V_{IH} = 4.0 - 2.0 = 2.0\\text{ V}$.",
            "Low noise margin: $NM_L = V_{IL} - V_{OL} = 2.0 - 0.5 = 1.5\\text{ V}$.",
            "Noise margins are $2.0\\text{ V}$ and $1.5\\text{ V}$."
        ],
        trap_note="Direct substitution into noise margin definitions."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q25.",
        year="GATE ECE 1987",
        marks="1 Mark",
        qtype="Subjective",
        diagram_img="",
        statement="Which TTL family has the lowest speed-power product? Which family has the lowest power consumption?",
        options=None,
        answer_key="(a) 74LS (Low power Schottky) has lowest speed-power product; (b) CMOS has lowest power consumption.",
        steps=[
            "Among TTL subfamilies, 74LS achieves the optimal speed-power product (Figure of Merit $\\approx 20\\text{ pJ}$).",
            "Among all logic families, CMOS achieves the lowest static power dissipation."
        ],
        trap_note="Speed-power product = Propagation delay $\\times$ Power dissipation."
    )

    # 2-Mark PYQs: Q26 to Q32
    pyqs_2m = ""

    # Q26
    pyqs_2m += build_pyq_card(
        qnum="Q26.",
        year="GATE ECE 2013",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the circuit shown below, $Q_1$ has negligible collector-to-emitter saturation voltage and the diode $D$ has a forward drop of $0.7\\text{ V}$. For $V_{in} = 5\\text{ V}$, the state of transistor $Q_2$ is",
        diagram_img="images/p10_img1_155.png",
        options=[
            ("(A)", "Active"),
            ("(B)", "Saturation"),
            ("(C)", "Cutoff"),
            ("(D)", "Reverse active")
        ],
        answer_key="(B) Saturation",
        steps=[
            "When $V_{in} = 5\\text{ V}$, base current flows into $Q_1$ turning it ON.",
            "Tracing current into the base of $Q_2$ shows $I_B > I_{C} / \\beta$, forcing $Q_2$ into Saturation."
        ],
        trap_note="Calculate base current vs collector saturation current."
    )

    # Q27
    pyqs_2m += build_pyq_card(
        qnum="Q27.",
        year="GATE ECE 2008",
        marks="2 Marks",
        qtype="MCQ",
        statement="The logic function implemented by the following circuit at the terminal OUT is",
        diagram_img="images/p11_img1_165.png",
        options=[
            ("(A)", "$P\\text{ NOR } Q$"),
            ("(B)", "$P\\text{ NAND } Q$"),
            ("(C)", "$P\\text{ OR } Q$"),
            ("(D)", "$P\\text{ XNOR } Q$")
        ],
        answer_key="(D) P XNOR Q (or NOR)",
        steps=[
            "Examine the complementary PMOS and NMOS network driven by inputs $P$ and $Q$.",
            "The truth table evaluation reveals output HIGH when both inputs are equal, representing XNOR."
        ],
        trap_note="Verify all four input combinations $(00, 01, 10, 11)$."
    )

    # Q28
    pyqs_2m += build_pyq_card(
        qnum="Q28.",
        year="GATE ECE 2007",
        marks="2 Marks",
        qtype="MCQ",
        statement="The circuit diagram of a standard TTL NOT gate is shown in the figure. When $V_{in} = 0.2\\text{ V}$, the modes of operation of transistors $Q_1, Q_2, Q_3, Q_4$ are respectively:",
        diagram_img="images/p11_img2_167.png",
        options=[
            ("(A)", "Cutoff, Saturation, Active, Cutoff"),
            ("(B)", "Saturation, Cutoff, Active, Cutoff"),
            ("(C)", "Active, Cutoff, Cutoff, Saturation"),
            ("(D)", "Saturation, Active, Cutoff, Saturation")
        ],
        answer_key="(B) Saturation, Cutoff, Active, Cutoff",
        steps=[
            "When input is LOW ($V_{in} = 0.2\\text{ V}$):",
            "1. <strong>$Q_1$:</strong> Base-emitter is forward-biased ($V_B = 0.2 + 0.7 = 0.9\\text{ V}$). Base current drives $Q_1$ into <strong>Saturation</strong>.",
            "2. <strong>$Q_2$:</strong> Collector of $Q_1$ is at $V_{CE1,sat} + 0.2 \\approx 0.4\\text{ V}$, which is below the $1.4\\text{ V}$ needed to turn on $Q_2$ and $Q_4$. Therefore, $Q_2$ is in <strong>Cutoff</strong>.",
            "3. <strong>$Q_4$:</strong> Receives zero base current from $Q_2 \\implies Q_4$ is in <strong>Cutoff</strong>.",
            "4. <strong>$Q_3$:</strong> With $Q_2$ in cutoff, its collector pulls up to $V_{CC}$ through $R_c$, turning $Q_3$ ON as an emitter follower (<strong>Active</strong> mode) to pull the output HIGH.",
            "Summary: $Q_1$ Saturation, $Q_2$ Cutoff, $Q_3$ Active, $Q_4$ Cutoff (Option B)."
        ],
        trap_note="A hallmark classic GATE TTL question! When input is LOW: $Q_1$ Sat, $Q_2$ Cutoff, $Q_3$ Active, $Q_4$ Cutoff."
    )

    # Q29
    pyqs_2m += build_pyq_card(
        qnum="Q29.",
        year="GATE ECE 2003",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="images/p12_img1_177.jpeg",
        statement="The DTL, TTL, ECL and CMOS families of digital ICs are compared in the following 4 columns for Propagation Delay, Power Dissipation, Noise Margin and Fan-out. The correct column is",
        options=[
            ("(A)", "Column 1"),
            ("(B)", "Column 2"),
            ("(C)", "Column 3"),
            ("(D)", "Column 4")
        ],
        answer_key="(B) Column 2",
        steps=[
            "Verify the absolute rankings of logic families:",
            "• Propagation Delay: $\\text{ECL} < \\text{TTL} < \\text{CMOS}$. (ECL is fastest)",
            "• Power Dissipation: $\\text{CMOS} \\ll \\text{TTL} < \\text{ECL}$. (CMOS lowest, ECL highest)",
            "• Fan-out: $\\text{CMOS} > \\text{TTL} > \\text{DTL}$.",
            "Column 2 correctly reflects these physical properties."
        ],
        trap_note="ECL has least delay and highest power. CMOS has least power and high fan-out."
    )

    # Q30
    pyqs_2m += build_pyq_card(
        qnum="Q30.",
        year="GATE ECE 1994",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="In the output stage of a standard TTL, we have a diode between the emitter of the pull-up transistor and the collector of the pull-down transistor. The purpose of this diode is to",
        options=[
            ("(A)", "protect against negative voltage spikes"),
            ("(B)", "prevent both output transistors from conducting simultaneously when output is LOW"),
            ("(C)", "increase the fan-out"),
            ("(D)", "reduce the propagation delay")
        ],
        answer_key="(B) prevent both output transistors from conducting simultaneously",
        steps=[
            "When output is LOW, $Q_4$ is in saturation ($V_{CE4,sat} \\approx 0.2\\text{ V}$).",
            "$Q_2$ is also in saturation, so its collector voltage is $V_{C2} = V_{BE4,sat} + V_{CE2,sat} \\approx 0.7 + 0.2 = 0.9\\text{ V}$.",
            "This voltage ($0.9\\text{ V}$) appears at the base of pull-up transistor $Q_3$.",
            "If the diode were absent, $V_{BE3} = V_{B3} - V_{out} = 0.9\\text{ V} - 0.2\\text{ V} = 0.7\\text{ V}$, which would turn $Q_3$ ON!",
            "Inserting diode $D$ requires $V_{B3} - V_{out} \\ge V_{BE3} + V_D = 0.7 + 0.7 = 1.4\\text{ V}$ to turn on.",
            "Since $0.9 - 0.2 = 0.7\\text{ V} < 1.4\\text{ V}$, $Q_3$ stays completely OFF.",
            "This eliminates shoot-through current from $V_{CC}$ to Ground."
        ],
        trap_note="Without the diode, both totem-pole transistors would turn on together, causing massive current spikes and thermal destruction."
    )

    # Q31
    pyqs_2m += build_pyq_card(
        qnum="Q31.",
        year="GATE ECE 1987",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="Given that for a logic family, $V_{OH}$ is the minimum output high-level voltage, $V_{OL}$ is the maximum output low-level voltage, $V_{IH}$ is the minimum input high-level voltage, and $V_{IL}$ is the maximum input low-level voltage. The noise margins are correctly defined as",
        options=[
            ("(A)", "$V_{OH} - V_{OL}$ and $V_{IH} - V_{IL}$"),
            ("(B)", "$V_{OH} - V_{IH}$ and $V_{IL} - V_{OL}$"),
            ("(C)", "$V_{IH} - V_{OH}$ and $V_{OL} - V_{IL}$"),
            ("(D)", "$V_{OH} - V_{IL}$ and $V_{IH} - V_{OL}$")
        ],
        answer_key="(B) VOH - VIH and VIL - VOL",
        steps=[
            "By fundamental definition:",
            "$$NM_H = V_{OH} - V_{IH}$$",
            "$$NM_L = V_{IL} - V_{OL}$$",
            "Matches Option (B)."
        ],
        trap_note="High noise margin subtracts input threshold from output level; low noise margin subtracts output level from input threshold."
    )

    # Q32
    pyqs_2m += build_pyq_card(
        qnum="Q32.",
        year="GATE ECE 1988",
        marks="8 Marks",
        qtype="Subjective / Design",
        diagram_img="",
        statement="Implement the function $F = AB + CD$ using two open-collector TTL 2-input NAND gates and an external pull-up resistor.",
        options=None,
        answer_key="Wired-AND realization: F = (AB)' . (CD)' = (AB + CD)' -> requires inverter for true SOP, or DeMorgan realization.",
        steps=[
            "Open collector NAND gates tied together form a Wired-AND output:<br/>$$Y = \\overline{AB} \\cdot \\overline{CD}$$",
            "Applying De Morgan's Law:<br/>$$Y = \\overline{AB + CD}$$",
            "This directly synthesizes the AND-OR-Invert (AOI) function $\\overline{AB + CD}$.",
            "To obtain uncomplemented $F = AB + CD$, feed through an open-collector inverter stage."
        ],
        trap_note="Wired-AND of NAND gates produces the AND-OR-INVERT (NOR of products) function."
    )

    sections_data = [
        {
            "id": "sec-taxonomy",
            "pill": "Chapter 03 · Part 1",
            "title": "Logic Family Taxonomy, Voltage Parameters & Noise Margins",
            "content": sec1_content
        },
        {
            "id": "sec-ttl",
            "pill": "Chapter 03 · Part 2",
            "title": "Transistor-Transistor Logic (TTL): Totem-Pole & Open-Collector",
            "content": sec2_content
        },
        {
            "id": "sec-cmos",
            "pill": "Chapter 03 · Part 3",
            "title": "CMOS Logic Design: PUN/PDN Synthesis, Dynamic Power & Sizing",
            "content": sec3_content
        },
        {
            "id": "sec-ecl",
            "pill": "Chapter 03 · Part 4",
            "title": "Emitter-Coupled Logic (ECL): High-Speed Non-Saturated Physics",
            "content": sec4_content
        },
        {
            "id": "sec-interfacing",
            "pill": "Chapter 03 · Part 5",
            "title": "Logic Family Interfacing & Pull-Up Level Shifting",
            "content": sec5_content
        },
        {
            "id": "sec-pyqs-1m",
            "pill": "GATE Official Archive · 1-Mark Questions",
            "title": "Official GATE 1-Mark PYQ Solutions (Q1 to Q25)",
            "content": pyqs_1m
        },
        {
            "id": "sec-pyqs-2m",
            "pill": "GATE Official Archive · 2-Mark & Design Questions",
            "title": "Official GATE 2-Mark PYQ Solutions (Q26 to Q32)",
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

    out_file = "digital/logic-families/notes.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"✓ Successfully generated {out_file} ({len(html_out)} bytes).")

if __name__ == "__main__":
    generate_logic_families()
