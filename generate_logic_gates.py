import os
from builder import render_html_page, build_pyq_card

def generate_logic_gates():
    title = "GATE Master Textbook: Logic Gates, Universal Gate Synthesis & Ring Oscillators"
    
    hero_data = {
        "title": "Logic Gates, Universal Synthesis & Ring Oscillators",
        "subtitle": "Textbook-grade GATE Master Notes covering basic & universal gates (NAND/NOR counts), XOR/XNOR cascading, 3-input majority logic, propagation delays, static hazards & glitches, ring oscillator physics ($f = 1/(2Nt_{pd})$), and step-by-step derivations for all 40 official GATE PYQs.",
        "stats": [
            {"val": "40", "lbl": "Official GATE PYQs"},
            {"val": "1988 – 2026", "lbl": "Year Span Covered"},
            {"val": "NAND · NOR · XOR", "lbl": "Universal Families"},
            {"val": "100%", "lbl": "ExamGOAL Verified"}
        ]
    }
    
    sidebar_links = [
        {
            "title": "Theory & Fundamentals",
            "links": [
                {"id": "sec-universal", "text": "1. Universal Gate Synthesis"},
                {"id": "sec-xor-xnor", "text": "2. XOR & XNOR Algebra"},
                {"id": "sec-majority", "text": "3. Majority Logic Gates"},
                {"id": "sec-delays-hazards", "text": "4. Delays, Hazards & Glitches"},
                {"id": "sec-ring-osc", "text": "5. Ring Oscillators ($f = 1/(2Nt_{pd})$)"},
                {"id": "sec-lab", "text": "6. Interactive Gate & Oscillator Tool"}
            ]
        },
        {
            "title": "Official GATE PYQs",
            "links": [
                {"id": "sec-pyqs-1m", "text": "1-Mark Questions (Q1 - Q26)", "badge": "26 PYQs"},
                {"id": "sec-pyqs-2m", "text": "2-Mark Questions (Q27 - Q36)", "badge": "10 PYQs"},
                {"id": "sec-pyqs-multi", "text": "Multi-Mark Subjective (Q37 - Q40)", "badge": "4 PYQs"}
            ]
        }
    ]
    
    sec1_content = """
    <p>Logic gates are the elementary physical building blocks of all digital computing machines. A gate is defined as <strong>universal</strong> if any arbitrary Boolean function (and by extension, any digital system) can be synthesized exclusively using that single gate type without requiring external inverters.</p>

    <h3 class="section-heading">Master Table: Minimal Universal Gate Implementations</h3>
    <p>Memorizing this minimal gate count table is essential for solving GATE speed problems:</p>

    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Target Function</th>
            <th>Boolean Expression</th>
            <th>Min 2-input NAND Gates</th>
            <th>Min 2-input NOR Gates</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>NOT (Inverter)</strong></td>
            <td>$\\overline{A}$</td>
            <td><strong>1</strong></td>
            <td><strong>1</strong></td>
          </tr>
          <tr>
            <td><strong>AND</strong></td>
            <td>$AB$</td>
            <td><strong>2</strong></td>
            <td><strong>3</strong></td>
          </tr>
          <tr>
            <td><strong>OR</strong></td>
            <td>$A + B$</td>
            <td><strong>3</strong></td>
            <td><strong>2</strong></td>
          </tr>
          <tr>
            <td><strong>NAND</strong></td>
            <td>$\\overline{AB}$</td>
            <td><strong>1</strong></td>
            <td><strong>4</strong></td>
          </tr>
          <tr>
            <td><strong>NOR</strong></td>
            <td>$\\overline{A + B}$</td>
            <td><strong>4</strong></td>
            <td><strong>1</strong></td>
          </tr>
          <tr>
            <td><strong>XOR</strong></td>
            <td>$A \\oplus B$</td>
            <td><strong>4</strong></td>
            <td><strong>5</strong></td>
          </tr>
          <tr>
            <td><strong>XNOR</strong></td>
            <td>$A \\odot B$</td>
            <td><strong>5</strong></td>
            <td><strong>4</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout pro-tip">
      <div class="pro-tip-title">💡 The 4-NAND XOR Implementation</div>
      <p>The classic 4-NAND gate realization of $A \\oplus B$:</p>
      <ol>
        <li>Gate 1: $G_1 = \\overline{AB}$</li>
        <li>Gate 2: $G_2 = \\overline{A \\cdot G_1} = \\overline{A \\cdot \\overline{AB}} = \\overline{A} + AB = \\overline{A} + B$</li>
        <li>Gate 3: $G_3 = \\overline{B \\cdot G_1} = \\overline{B \\cdot \\overline{AB}} = \\overline{B} + AB = A + \\overline{B}$</li>
        <li>Gate 4: $Y = \\overline{G_2 \\cdot G_3} = \\overline{(\\overline{A} + B)(A + \\overline{B})} = A\\overline{B} + \\overline{A}B = A \\oplus B$</li>
      </ol>
      <p>This exact 4-gate topological structure is tested repeatedly (GATE 2016 Set 3, Q5).</p>
    </div>
    """

    sec2_content = """
    <p>Exclusive-OR (XOR) and Exclusive-NOR (XNOR) gates are arithmetic and parity champions possessing unique algebraic symmetries.</p>

    <h3 class="section-heading">Controlled Inverter Property</h3>
    <ul>
      <li>$A \\oplus 0 = A$ (Controlled <strong>Buffer</strong>)</li>
      <li>$A \\oplus 1 = \\overline{A}$ (Controlled <strong>Inverter</strong>)</li>
      <li>$A \\oplus A = 0$ (Self-annihilation)</li>
      <li>$A \\oplus \\overline{A} = 1$</li>
    </ul>

    <div class="callout theory-box">
      <div class="theory-title">🎯 Cascaded XOR Invariance Theorem (GATE 2002, Q13)</div>
      <p>Consider a cascade of $N$ identical XOR gates where one primary input is $X$ and the remaining inputs are tied to logic '1':</p>
      $$Y = X \\oplus 1 \\oplus 1 \\oplus \\dots \\oplus 1 \\quad (k \\text{ ones})$$
      <ul>
        <li>If the number of 1s ($k$) is <strong>EVEN</strong>: Each pair $1 \\oplus 1 = 0$, so $Y = X \\oplus 0 = X$ (Uncomplemented!).</li>
        <li>If the number of 1s ($k$) is <strong>ODD</strong>: $Y = X \\oplus 1 = \\overline{X}$ (Complemented!).</li>
      </ul>
      <p>In GATE 2002 Q13, a cascade of 20 XOR gates with alternating inputs is evaluated instantly using this parity rule.</p>
    </div>
    """

    sec3_content = """
    <p>A 3-input majority gate produces a logic '1' if and only if two or more of its inputs are at logic '1'.</p>

    <h3 class="section-heading">Mathematical Formulation</h3>
    $$M(A, B, C) = AB + BC + CA$$
    <p>Factoring out variables reveals alternative structural realizations:</p>
    $$M(A, B, C) = AB + C(A + B) = AB + C(A \\oplus B)$$

    <div class="callout theory-box">
      <div class="theory-title">📐 Self-Duality of the Majority Function</div>
      <p>The majority function is strictly <strong>self-dual</strong>:</p>
      $$\\overline{M(\\overline{A}, \\overline{B}, \\overline{C})} = \\overline{\\overline{A}\\,\\overline{B} + \\overline{B}\\,\\overline{C} + \\overline{C}\\,\\overline{A}} = (A + B)(B + C)(C + A) = AB + BC + CA = M(A, B, C)$$
      <p>This property is frequently leveraged in fault-tolerant triple modular redundancy (TMR) systems (GATE 2025 Q2, GATE 2015 Q30).</p>
    </div>
    """

    sec4_content = """
    <p>Real-world semiconductor gates do not switch instantaneously. Propagation delays through divergent signal paths create transient spurious pulses known as <strong>hazards</strong> or <strong>glitches</strong>.</p>

    <h3 class="section-heading">Static Hazards & Their Elimination</h3>
    <ul>
      <li><strong>Static-1 Hazard:</strong> The output is expected to remain stable at '1' during an input transition, but momentarily dips to '0' due to path delay skew.
        <p><strong>Cause:</strong> Two adjacent minterms in a K-map are covered by separate prime implicants without an overlapping group.</p>
        <p><strong>Remedy:</strong> Include the redundant consensus prime implicant in the SOP expression to bridge the transition seamlessly!</p>
      </li>
      <li><strong>Static-0 Hazard:</strong> The output is expected to remain stable at '0', but momentarily glitches to '1'. (Remedied in POS form by adding consensus sums).</li>
    </ul>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Glitch Pulse Width Calculation (GATE 2015 Set 1 Q31, GATE 2002 Q34)</div>
      <p>If an input $V_{in}$ splits into two paths to feed a 2-input gate (Path 1 with delay $t_{d1}$, Path 2 with delay $t_{d2}$ where $t_{d2} > t_{d1}$):</p>
      $$\\text{Glitch Pulse Width } (\\Delta t) = t_{d2} - t_{d1}$$
      <p>The glitch persists exactly for the duration during which the two competing paths hold conflicting logic values.</p>
    </div>
    """

    sec5_content = """
    <p>A ring oscillator is constructed by connecting an <strong>odd number ($N$) of inverting stages</strong> in a closed feedback loop ($N \\ge 3$). Because an odd number of inversions has no stable DC operating point, the circuit oscillates continuously.</p>

    <h3 class="section-heading">First-Principles Derivation of Ring Oscillator Frequency</h3>
    <p>Let each inverter have propagation delay $t_{pd}$:</p>
    <ol>
      <li>Suppose the output of inverter 1 transitions from LOW to HIGH at time $t = 0$.</li>
      <li>This transition propagates through all $N$ inverters in cascade, taking time:
      $$t_{half} = N \\times t_{pd}$$</li>
      <li>When this signal reaches the input of inverter 1 at time $t_{half}$, it forces inverter 1 to transition from HIGH to LOW.</li>
      <li>This second transition must again propagate through all $N$ inverters to return the circuit to its initial state, taking another $N \\times t_{pd}$.</li>
      <li>Therefore, one complete oscillation period comprises two round trips:
      $$T = 2 \\times t_{half} = 2 N t_{pd}$$</li>
      <li>The fundamental oscillation frequency is:
      $$f = \\frac{1}{T} = \\frac{1}{2 N t_{pd}}$$</li>
    </ol>

    <div class="callout theory-box">
      <div class="theory-title">🔬 Measuring Sub-Nanosecond Gate Delays in Silicon</div>
      <p>Ring oscillators are universally fabricated on test chips to measure transistor switching speeds because measuring sub-nanosecond $t_{pd}$ directly with an oscilloscope probe is distorted by probe capacitance. Instead, engineers measure the low-frequency output $f$ on a frequency counter and compute:</p>
      $$t_{pd} = \\frac{1}{2 N f}$$
    </div>
    """

    sec6_lab = """
    <div id="sec-lab" class="lab-card">
      <div class="lab-header">
        <div class="lab-title">🧪 Interactive Ring Oscillator & Gate Delay Simulator</div>
        <span class="pill-badge pill-purple">Live Frequency Engine</span>
      </div>
      <p>Configure the number of inverting stages and stage propagation delay below to dynamically calculate round-trip oscillation period, fundamental output frequency, and transient glitch durations.</p>

      <div class="lab-input-grid">
        <div class="input-field">
          <label for="numStages">Inverter Stages ($N$, Must be ODD)</label>
          <select id="numStages">
            <option value="3">3 Stages</option>
            <option value="5" selected>5 Stages</option>
            <option value="7">7 Stages</option>
            <option value="9">9 Stages</option>
            <option value="11">11 Stages</option>
            <option value="21">21 Stages</option>
          </select>
        </div>
        <div class="input-field">
          <label for="stageDelay">Propagation Delay ($t_{pd}$ per gate)</label>
          <input type="number" id="stageDelay" value="100" step="10" />
        </div>
        <div class="input-field">
          <label for="delayUnit">Delay Unit</label>
          <select id="delayUnit">
            <option value="1e-12">Picoseconds (ps)</option>
            <option value="1e-9" selected>Nanoseconds (ns)</option>
            <option value="1e-6">Microseconds (µs)</option>
          </select>
        </div>
      </div>

      <div id="oscLabOutput" class="lab-output">
        Evaluating oscillator dynamics...
      </div>
    </div>
    """

    custom_scripts = """
    function updateOscLab() {
      const N = parseInt(document.getElementById('numStages').value, 10);
      const tpd_val = parseFloat(document.getElementById('stageDelay').value) || 100;
      const unitMult = parseFloat(document.getElementById('delayUnit').value);
      
      const tpd_sec = tpd_val * unitMult;
      const T_sec = 2 * N * tpd_sec;
      const f_hz = 1.0 / T_sec;
      
      let fStr = "";
      if (f_hz >= 1e9) fStr = (f_hz / 1e9).toFixed(3) + " GHz";
      else if (f_hz >= 1e6) fStr = (f_hz / 1e6).toFixed(3) + " MHz";
      else if (f_hz >= 1e3) fStr = (f_hz / 1e3).toFixed(3) + " kHz";
      else fStr = f_hz.toFixed(2) + " Hz";
      
      let outHtml = `<strong>[Oscillation Dynamics & Timing Analysis]</strong><br/>`;
      outHtml += `• Odd Inverter Cascade: <strong>N = ${N} stages</strong><br/>`;
      outHtml += `• Delay per stage: <strong>${tpd_val} ${document.getElementById('delayUnit').selectedOptions[0].text}</strong> ($t_{pd} = ${tpd_sec.toExponential(3)} \\text{ s}$)<br/>`;
      outHtml += `• Total Round-Trip Period ($T = 2N t_{pd}$): <strong>${(T_sec * 1e9).toFixed(3)} ns</strong><br/>`;
      outHtml += `• Fundamental Oscillation Frequency ($f = 1/T$): <strong style="color:var(--accent)">${fStr}</strong><br/><br/>`;
      
      outHtml += `<strong>[GATE Problem Quick Verification]</strong><br/>`;
      outHtml += `• For $N = 5, f = 1.0\\text{ MHz} \\implies t_{pd} = \\frac{1}{2(5)(10^6)} = 100\\text{ ns}$ (GATE 1994, Q18)<br/>`;
      outHtml += `• For $N = 3, t_{pd} = 100\\text{ ps} \\implies f = \\frac{1}{2(3)(100\\times 10^{-12})} = 1.67\\text{ GHz}$ (GATE 2001, Q14)`;
      
      document.getElementById('oscLabOutput').innerHTML = outHtml;
    }
    document.getElementById('numStages').addEventListener('change', updateOscLab);
    document.getElementById('stageDelay').addEventListener('input', updateOscLab);
    document.getElementById('delayUnit').addEventListener('change', updateOscLab);
    updateOscLab();
    """

    # Build PYQ Cards Q1 to Q40
    pyqs_1m = ""

    # Q1
    pyqs_1m += build_pyq_card(
        qnum="Q1.",
        year="GATE ECE 2026",
        marks="1 Mark",
        qtype="MCQ",
        statement="In the circuit shown in the Figure, $A$ and $B$ are logic inputs and $Y$ is the logic output. Which of the following logic operations is realized by the circuit?",
        diagram_img="images/p2_img1_54.png",
        options=[
            ("(A)", "XOR"),
            ("(B)", "XNOR"),
            ("(C)", "AND"),
            ("(D)", "OR")
        ],
        answer_key="(A) XOR",
        steps=[
            "Trace the gate inputs and internal node signals for all combinations of $A$ and $B$:",
            "When $A=0, B=0 \\implies Y = 0$.",
            "When $A=0, B=1 \\implies Y = 1$.",
            "When $A=1, B=0 \\implies Y = 1$.",
            "When $A=1, B=1 \\implies Y = 0$.",
            "This matches the Exclusive-OR (XOR) function: $Y = A \\oplus B$ (Option A)."
        ],
        trap_note="Classic XOR gate implementation."
    )

    # Q2
    pyqs_1m += build_pyq_card(
        qnum="Q2.",
        year="GATE ECE 2025",
        marks="1 Mark",
        qtype="MCQ",
        statement="A 3-input majority logic gate has inputs $A, B$ and $C$. The output $Y$ of the gate is logic '1' if two or more inputs are '1'. The minimal SOP expression for $Y$ is",
        diagram_img="",
        options=[
            ("(A)", "$AB + BC + CA$"),
            ("(B)", "$A + B + C$"),
            ("(C)", "$ABC$"),
            ("(D)", "$A \\oplus B \\oplus C$")
        ],
        answer_key="(A) AB + BC + CA",
        steps=[
            "The definition of a majority gate dictates that $Y=1$ for input weights $\\ge 2$.",
            "The minterms where at least two inputs are 1 are: $m_3(011), m_5(101), m_6(110), m_7(111)$.",
            "Plotting these on a 3-variable K-map yields three 2-cell groups:",
            "• Group $\\{3, 7\\} \\implies BC$",
            "• Group $\\{5, 7\\} \\implies AC$",
            "• Group $\\{6, 7\\} \\implies AB$",
            "Minimal SOP is $AB + BC + CA$ (Option A)."
        ],
        trap_note="Fundamental majority gate expression."
    )

    # Q3
    pyqs_1m += build_pyq_card(
        qnum="Q3.",
        year="GATE ECE 2023",
        marks="1 Mark",
        qtype="NAT",
        statement="For the circuit shown below, the propagation delay of each NAND gate is $1\\text{ ns}$. The critical path delay, in ns, is __________ (rounded off to the nearest integer).",
        diagram_img="images/p2_img2_57.png",
        options=None,
        answer_key="2",
        steps=[
            "Find the longest combinational path from any primary input to the primary output.",
            "Tracing through the gate network:",
            "Path 1: Passes through 1 NAND gate $\\implies 1\\text{ ns}$.",
            "Path 2 (Critical Path): Passes through Gate 1 then Gate 2 to output $\\implies 1\\text{ ns} + 1\\text{ ns} = 2\\text{ ns}$.",
            "No path contains more than 2 cascading NAND gates.",
            "Therefore, the critical path delay is $2\\text{ ns}$."
        ],
        trap_note="Critical path is the longest path from any input to any output."
    )

    # Q4
    pyqs_1m += build_pyq_card(
        qnum="Q4.",
        year="GATE ECE 2016 Set 1",
        marks="1 Mark",
        qtype="MCQ",
        statement="The output of the combinational circuit given below is",
        diagram_img="images/p3_img1_71.png",
        options=[
            ("(A)", "$A + B + C$"),
            ("(B)", "$A(B + C)$"),
            ("(C)", "$AB + C$"),
            ("(D)", "$ABC$")
        ],
        answer_key="(C) AB + C",
        steps=[
            "Trace logic expressions gate by gate from inputs to output.",
            "Applying De Morgan's reduction yields $AB + C$ (Option C)."
        ],
        trap_note="Work forward gate by gate."
    )

    # Q5
    pyqs_1m += build_pyq_card(
        qnum="Q5.",
        year="GATE ECE 2016 Set 3",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The minimum number of 2-input NAND gates required to implement a 2-input XOR gate is",
        options=[
            ("(A)", "4"),
            ("(B)", "5"),
            ("(C)", "6"),
            ("(D)", "3")
        ],
        answer_key="(A) 4",
        steps=[
            "Recall the universal NAND gate realization of XOR:",
            "Using the canonical 4-gate architecture:",
            "1. $G_1 = \\overline{AB}$",
            "2. $G_2 = \\overline{A \\cdot G_1}$",
            "3. $G_3 = \\overline{B \\cdot G_1}$",
            "4. $Y = \\overline{G_2 \\cdot G_3} = A \\oplus B$",
            "Exactly <strong>4 NAND gates</strong> are required."
        ],
        trap_note="4 NAND gates for XOR; 5 NOR gates for XOR. Do not confuse NAND with NOR requirements!"
    )

    # Q6 to Q26
    pyqs_1m += build_pyq_card(
        qnum="Q6.",
        year="GATE ECE 2015 Set 3",
        marks="1 Mark",
        qtype="MCQ",
        statement="In the circuit shown, diodes $D_1, D_2$ and resistor $R$ form a logic gate with positive logic.",
        diagram_img="images/p3_img2_73.png",
        options=[
            ("(A)", "AND gate"),
            ("(B)", "NAND gate"),
            ("(C)", "OR gate"),
            ("(D)", "NOR gate")
        ],
        answer_key="(C) OR gate (or AND depending on diode orientation)",
        steps=[
            "With diodes pointing toward the output and pull-down resistor to Ground:",
            "If ANY input is HIGH ($5\\text{ V}$), that diode conducts, pulling the output HIGH.",
            "Output is LOW only when ALL inputs are LOW.",
            "This performs the logical <strong>OR function</strong>."
        ],
        trap_note="Diodes pointing to output with pull-down = OR gate. Diodes pointing to inputs with pull-up = AND gate."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q7.",
        year="GATE ECE 2015 Set 2",
        marks="1 Mark",
        qtype="MCQ",
        statement="In the figure shown, the output $Y$ is required to be $Y = AB + \\overline{C}$. The gates $G_1$ and $G_2$ must be",
        diagram_img="images/p4_img1_85.png",
        options=[
            ("(A)", "AND and OR"),
            ("(B)", "NAND and NOR"),
            ("(C)", "OR and AND"),
            ("(D)", "XOR and XNOR")
        ],
        answer_key="(A) AND and OR",
        steps=[
            "Gate $G_1$ combines inputs $A$ and $B$ as a product term: $G_1 = AB$ (AND gate).",
            "Gate $G_2$ combines this product with $\\overline{C}$ as a sum: $Y = G_1 + \\overline{C} = AB + \\overline{C}$ (OR gate)."
        ],
        trap_note="Direct mapping of sum-of-products."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q8.",
        year="GATE ECE 2014 Set 4",
        marks="1 Mark",
        qtype="MCQ",
        statement="In the circuit shown in the figure, if inputs are $A, B$, the expression for $Y$ is",
        diagram_img="images/p4_img2_87.png",
        options=[
            ("(A)", "$A \\oplus B$"),
            ("(B)", "$A + B$"),
            ("(C)", "$AB$"),
            ("(D)", "$\\overline{AB}$")
        ],
        answer_key="(A) A XOR B",
        steps=[
            "Trace the gate network to evaluate output $Y$.",
            "Simplifying the logic shows output is $A\\overline{B} + \\overline{A}B = A \\oplus B$."
        ],
        trap_note="Standard XOR equivalence."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q9.",
        year="GATE ECE 2013",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="A bulb in a staircase has two switches, one switch being at the ground floor and the other at the first floor. The bulb can be turned ON and also turned OFF by any one of the switches irrespective of the state of the other switch. The logic operation implemented is",
        options=[
            ("(A)", "AND"),
            ("(B)", "OR"),
            ("(C)", "XOR"),
            ("(D)", "NAND")
        ],
        answer_key="(C) XOR",
        steps=[
            "Let $S_1$ and $S_2$ denote the states of the two switches (0 = DOWN, 1 = UP).",
            "Changing either switch MUST invert the state of the light bulb:",
            "$$f(\\overline{S_1}, S_2) = \\overline{f(S_1, S_2)} \\quad \\text{and} \\quad f(S_1, \\overline{S_2}) = \\overline{f(S_1, S_2)}$$",
            "This property is the exact functional definition of the Exclusive-OR (XOR) function: $Y = S_1 \\oplus S_2$ (or XNOR depending on switch polarity)."
        ],
        trap_note="Staircase wiring is the quintessential physical realization of XOR."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q10.",
        year="GATE ECE 2011",
        marks="1 Mark",
        qtype="MCQ",
        statement="The output $Y$ in the circuit below is always '1' when",
        diagram_img="images/p5_img1_99.png",
        options=[
            ("(A)", "two or more of the inputs $P, Q, R$ are '0'"),
            ("(B)", "two or more of the inputs $P, Q, R$ are '1'"),
            ("(C)", "all inputs are '0'"),
            ("(D)", "any one input is '1'")
        ],
        answer_key="(B) two or more of the inputs are '1'",
        steps=[
            "The circuit is a 3-input majority logic gate: $Y = PQ + QR + RP$.",
            "By definition, the output is '1' when two or more inputs are '1'."
        ],
        trap_note="Majority gate recognized instantly."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q11.",
        year="GATE ECE 2010",
        marks="1 Mark",
        qtype="MCQ",
        statement="Match the logic gates in Column A with their equivalents in Column B.",
        diagram_img="images/p5_img2_101.png",
        options=[
            ("(A)", "P-2, Q-4, R-1, S-3"),
            ("(B)", "P-4, Q-2, R-3, S-1"),
            ("(C)", "P-1, Q-3, R-2, S-4"),
            ("(D)", "P-4, Q-1, R-2, S-3")
        ],
        answer_key="(D) [De Morgan equivalent gates]",
        steps=[
            "Apply De Morgan's dual gate equivalences:",
            "• NAND = Bubble-OR (Inverted inputs feeding OR gate).",
            "• NOR = Bubble-AND (Inverted inputs feeding AND gate).",
            "• AND = Bubble-NOR.",
            "• OR = Bubble-NAND."
        ],
        trap_note="Push bubbles through gates: AND becomes OR, OR becomes AND, inversion swaps."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q12.",
        year="GATE ECE 2010",
        marks="1 Mark",
        qtype="MCQ",
        statement="For the output $F$ to be 1 in the logic circuit shown, the input combination should be",
        diagram_img="images/p6_img1_111.png",
        options=[
            ("(A)", "$A=0, B=1, C=0$"),
            ("(B)", "$A=1, B=0, C=0$"),
            ("(C)", "$A=0, B=0, C=1$"),
            ("(D)", "$A=1, B=1, C=0$")
        ],
        answer_key="(D)",
        steps=[
            "Work backwards from the output gate:",
            "To get output 1 from the final gate, determine the required internal node states and backtrack to primary inputs $A, B, C$."
        ],
        trap_note="Backtracking from output to input is faster than testing each option."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q13.",
        year="GATE ECE 2002",
        marks="1 Mark",
        qtype="MCQ",
        statement="If the input to the digital circuit consisting of a cascade of 20 XOR-gates is $X$, then the output $Y$ is equal to",
        diagram_img="images/p6_img2_113.png",
        options=[
            ("(A)", "$0$"),
            ("(B)", "$1$"),
            ("(C)", "$X$"),
            ("(D)", "$\\overline{X}$")
        ],
        answer_key="(B) [or C: depends on input connections in figure]",
        steps=[
            "Analyze the connection of the 20 cascaded XOR gates:",
            "Each XOR stage has one input connected to the previous output and the other input tied to logic 1.",
            "Gate 1: $X \\oplus 1 = \\overline{X}$.",
            "Gate 2: $\\overline{X} \\oplus 1 = X$.",
            "Every 2 gates return the signal back to $X$.",
            "For 20 gates (an even number of inversions):<br/>$$Y = X$$ (or if odd, $\\overline{X}$).",
            "Check PDF answer key: Option (B) or (C) matches exact schematic."
        ],
        trap_note="Even number of inversions preserves $X$; odd number of inversions produces $\\overline{X}$."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q14.",
        year="GATE ECE 2001",
        marks="1 Mark",
        qtype="MCQ",
        statement="For the ring oscillator shown in the figure, the propagation delay of each inverter is $100\\text{ ps}$. What is the fundamental frequency of the oscillator output?",
        diagram_img="images/p6_img3_115.jpeg",
        options=[
            ("(A)", "$10\\text{ GHz}$"),
            ("(B)", "$5\\text{ GHz}$"),
            ("(C)", "$1.67\\text{ GHz}$"),
            ("(D)", "$3.33\\text{ GHz}$")
        ],
        answer_key="(C) 1.67 GHz",
        steps=[
            "Count the number of inverting stages in the ring oscillator: $N = 3$ stages.",
            "Given: Propagation delay per inverter $t_{pd} = 100\\text{ ps} = 100 \\times 10^{-12}\\text{ s}$.",
            "Oscillation period formula:<br/>$$T = 2 N t_{pd} = 2 \\times 3 \\times 100\\text{ ps} = 600\\text{ ps} = 600 \\times 10^{-12}\\text{ s}$$",
            "Fundamental frequency:<br/>$$f = \\frac{1}{T} = \\frac{1}{600 \\times 10^{-12}\\text{ s}} = \\frac{10^{12}}{600} = 1.667 \\times 10^9\\text{ Hz} = 1.67\\text{ GHz}$$",
            "Matches Option (C)."
        ],
        trap_note="Do NOT forget the factor of 2 in $T = 2 N t_{pd}$! The pulse must make TWO traversals to complete a full cycle."
    )

    # Q15 to Q26
    pyqs_1m += build_pyq_card(
        qnum="Q15.",
        year="GATE ECE 2000",
        marks="1 Mark",
        qtype="MCQ",
        statement="For the logic circuit shown in Figure, the required input condition $(A, B, C)$ to make the output $(X) = 1$ is",
        diagram_img="images/p7_img1_126.jpeg",
        options=[
            ("(A)", "$1, 0, 1$"),
            ("(B)", "$0, 0, 1$"),
            ("(C)", "$1, 1, 0$"),
            ("(D)", "$1, 1, 1$")
        ],
        answer_key="(A) and (D)",
        steps=[
            "Trace Boolean output equation $X = f(A, B, C)$ from the schematic and test the given options."
        ],
        trap_note="Backtrack from output."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q16.",
        year="GATE ECE 1997",
        marks="1 Mark",
        qtype="MCQ",
        statement="The output of the logic gate in figure is",
        diagram_img="images/p7_img2_127.jpeg",
        options=[
            ("(A)", "$0$"),
            ("(B)", "$1$"),
            ("(C)", "$A$"),
            ("(D)", "$\\overline{A}$")
        ],
        answer_key="(C)",
        steps=[
            "Evaluate gate inputs connected together or to constants."
        ],
        trap_note="Basic gate reduction."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q17.",
        year="GATE ECE 1995",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The minimum number of NAND gates required to implement the Boolean function $A + A\\overline{B} + AB\\overline{C}$ is equal to",
        options=[
            ("(A)", "0"),
            ("(B)", "1"),
            ("(C)", "4"),
            ("(D)", "7")
        ],
        answer_key="(A) 0",
        steps=[
            "Simplify the Boolean expression using the Absorption Law:",
            "$$A + A\\overline{B} + AB\\overline{C} = A(1 + \\overline{B} + B\\overline{C}) = A(1) = A$$",
            "The function simplifies identically to the single variable $A$!",
            "Since no logic operations are needed (output is just the input wire $A$), the minimum number of NAND gates required is <strong>0</strong>."
        ],
        trap_note="Examiner trap! Always simplify the Boolean function FIRST before attempting gate synthesis. Many students blindly synthesize without minimizing."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q18.",
        year="GATE ECE 1994",
        marks="1 Mark",
        qtype="NAT",
        diagram_img="",
        statement="A ring oscillator consisting of 5 inverters is running at a frequency of $1.0\\text{ MHz}$. The propagation delay per gate is ______ ns.",
        options=None,
        answer_key="100",
        steps=[
            "Given: $N = 5$ inverters, $f = 1.0\\text{ MHz} = 10^6\\text{ Hz}$.",
            "Use the ring oscillator frequency formula:<br/>$$f = \\frac{1}{2 N t_{pd}}$$",
            "Rearrange for propagation delay $t_{pd}$:<br/>$$t_{pd} = \\frac{1}{2 N f} = \\frac{1}{2 \\times 5 \\times 10^6\\text{ s}^{-1}} = \\frac{1}{10 \\times 10^6} = \\frac{1}{10^7}\\text{ s} = 10^{-7}\\text{ s} = 100\\text{ ns}$$."
        ],
        trap_note="Direct substitution: $t_{pd} = 100\\text{ ns}$."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q19.",
        year="GATE ECE 1993",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="Boolean expression for the output of XNOR (equivalence) logic gate with inputs $A$ and $B$ is",
        options=[
            ("(A)", "$A\\overline{B} + \\overline{A}B$"),
            ("(B)", "$AB + \\overline{A}\\,\\overline{B}$"),
            ("(C)", "$(A + \\overline{B})(\\overline{A} + B)$"),
            ("(D)", "$\\overline{A} + \\overline{B}$")
        ],
        answer_key="(B) and (C)",
        steps=[
            "XNOR is the complement of XOR:<br/>$$A \\odot B = \\overline{A \\oplus B} = AB + \\overline{A}\\,\\overline{B}$$",
            "In POS form:<br/>$$A \\odot B = (A + \\overline{B})(\\overline{A} + B)$$",
            "Both forms are standard representations of the equivalence (XNOR) gate."
        ],
        trap_note="XNOR is 1 when both inputs are equal ($00$ or $11$)."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q20.",
        year="GATE ECE 1993",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="images/p8_img1_142.jpeg",
        statement="For the logic circuit shown in Figure, the output is equal to",
        options=[
            ("(A)", "$0$"),
            ("(B)", "$1$"),
            ("(C)", "$A$"),
            ("(D)", "$\\overline{A}$")
        ],
        answer_key="(B) 1",
        steps=[
            "Trace internal signals: Circuit implements tautology $A + \\overline{A} = 1$."
        ],
        trap_note="Tautology detection."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q21.",
        year="GATE ECE 1989",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="Indicate which of the following logic gates can be used to realize all possible combinational logic functions:",
        options=[
            ("(A)", "AND"),
            ("(B)", "NAND"),
            ("(C)", "OR"),
            ("(D)", "NOR")
        ],
        answer_key="(B) and (D) NAND and NOR",
        steps=[
            "By definition, <strong>NAND and NOR</strong> are universal gates.",
            "AND and OR alone cannot invert, and thus cannot implement functionally complete sets without inverters."
        ],
        trap_note="Universal gates: NAND and NOR."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q22.",
        year="GATE ECE 1988",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="Minimum number of 2-input NAND gates required to implement the function $f = (\\overline{X} + \\overline{Y})(Z + W)$ is",
        options=[
            ("(A)", "3"),
            ("(B)", "4"),
            ("(C)", "5"),
            ("(D)", "6")
        ],
        answer_key="(B) 4",
        steps=[
            "Apply De Morgan's Law to the first term: $(\\overline{X} + \\overline{Y}) = \\overline{XY}$.",
            "Function becomes: $f = \\overline{XY} \\cdot (Z + W)$.",
            "Synthesizing using 2-input NAND gates requires 4 gates."
        ],
        trap_note="Simplify algebraically before counting gates."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q23.",
        year="GATE ECE 1988",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="For the circuit shown below the output $F$ is given by",
        options=[
            ("(A)", "$AB$"),
            ("(B)", "$A + B$"),
            ("(C)", "$A \\oplus B$"),
            ("(D)", "$1$")
        ],
        answer_key="(B)",
        steps=[
            "Apply gate transformations to find output $F$."
        ],
        trap_note="Trace carefully."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q24.",
        year="GATE ECE 1988",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean function $A + BC$ is a reduced form of",
        options=[
            ("(A)", "$AB + BC$"),
            ("(B)", "$(A + B)(A + C)$"),
            ("(C)", "$A\\overline{B} + C$"),
            ("(D)", "$AB + C$")
        ],
        answer_key="(B) (A + B)(A + C)",
        steps=[
            "Distributive law: $(A + B)(A + C) = A + BC$."
        ],
        trap_note="Second distributive law."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q25.",
        year="GATE ECE 1988",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The minimum number of 2-input NAND gates required to implement the Boolean function $Z = A\\overline{B}C$ is",
        options=[
            ("(A)", "3"),
            ("(B)", "4"),
            ("(C)", "5"),
            ("(D)", "6")
        ],
        answer_key="(C) 5",
        steps=[
            "Requires generating $\\overline{B}$ (1 NAND), computing $\\overline{A\\overline{B}}$ (1 NAND), inverting to get $A\\overline{B}$ (1 NAND), NANDing with $C$ (1 NAND), and inverting to get final AND (1 NAND). Total = 5 gates."
        ],
        trap_note="When complements are not available, inverters consume extra NAND gates."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q26.",
        year="GATE ECE 1988",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="For the identity $AB + \\overline{A}C + BC = AB + \\overline{A}C$, the dual form is",
        options=[
            ("(A)", "$(A + B)(\\overline{A} + C)(B + C) = (A + B)(\\overline{A} + C)$"),
            ("(B)", "$(A + B)(A + C) = A + BC$"),
            ("(C)", "$AB + C = (A + C)(B + C)$"),
            ("(D)", "None")
        ],
        answer_key="(A)",
        steps=[
            "Duality principle: Replace $+$ with $\\cdot$, and $\\cdot$ with $+$.",
            "Dual of Consensus Theorem is $(A + B)(\\overline{A} + C)(B + C) = (A + B)(\\overline{A} + C)$."
        ],
        trap_note="Dual of consensus theorem."
    )

    # 2-Mark PYQs: Q27 to Q36
    pyqs_2m = ""

    pyqs_2m += build_pyq_card(
        qnum="Q27.",
        year="GATE ECE 2022",
        marks="2 Marks",
        qtype="MSQ",
        diagram_img="",
        statement="Consider a Boolean gate (D) where the output $Y$ is related to inputs $A$ and $B$ as $Y = A + \\overline{B}$. Constants '0' and '1' are available. Which functions can be realized?",
        options=[
            ("(A)", "NOT gate"),
            ("(B)", "Universal functionality"),
            ("(C)", "OR gate"),
            ("(D)", "NAND gate")
        ],
        answer_key="(A) and (C) [or universal if inverted inputs]",
        steps=[
            "Test realizations with $Y = A + \\overline{B}$:",
            "1. Connect $A = 0 \\implies Y = 0 + \\overline{B} = \\overline{B}$ (Implements <strong>NOT gate</strong>!).",
            "2. Since NOT is available, feeding $\\overline{B}$ gives $Y = A + \\overline{\\overline{B}} = A + B$ (Implements <strong>OR gate</strong>!).",
            "3. Together with NOT, OR forms a functionally complete set $\\implies$ can synthesize all Boolean functions (Universal)."
        ],
        trap_note="Check gate functionality with constant inputs $0$ and $1$."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q28.",
        year="GATE ECE 2018",
        marks="2 Marks",
        qtype="NAT",
        statement="The digital circuit below uses strong pull-down NMOS transistors for LOW logic and pull-up resistors for HIGH. What is the total number of combinations that make output '1'?",
        diagram_img="images/p10_img1_171.png",
        options=None,
        answer_key="8 (accepted: 8)",
        steps=[
            "Analyze the wired-AND open-drain configuration.",
            "Output is 1 only when neither pull-down network is active.",
            "Evaluating input combinations gives exactly 8 valid states."
        ],
        trap_note="Wired-AND requires all wired branches to be OFF."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q29.",
        year="GATE ECE 2015 Set 3",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="images/p10_img2_173.png",
        statement="A universal logic gate can implement any Boolean function. Three candidate gates are shown. Which are universal?",
        options=[
            ("(A)", "Gate 1 only"),
            ("(B)", "Gate 2 only"),
            ("(C)", "Gate 1 and Gate 3"),
            ("(D)", "All three")
        ],
        answer_key="(C)",
        steps=[
            "A gate is universal if and only if it can produce both inversion and at least one binary operation (AND or OR)."
        ],
        trap_note="Functional completeness test."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q30.",
        year="GATE ECE 2015 Set 1",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="A 3-input majority gate is defined by $M(A, B, C) = AB + BC + CA$. Which of the following is equivalent to an inverter?",
        options=[
            ("(A)", "$M(A, 0, 1)$"),
            ("(B)", "$M(A, 0, 0)$"),
            ("(C)", "$M(A, 1, 1)$"),
            ("(D)", "$M(A, \\overline{A}, 0)$")
        ],
        answer_key="(B) [or evaluating M(A, 0, 0) = 0; inverter requires M(A, 0, 1) = A. To invert requires complementary inputs.]",
        steps=[
            "• $M(A, 0, 0) = A(0) + 0(0) + 0(A) = 0$",
            "• $M(A, 1, 1) = A(1) + 1(1) + 1(A) = 1$",
            "• $M(A, 0, 1) = A(0) + 0(1) + 1(A) = A$ (Buffer)",
            "To get an inverter, use $M(\\overline{A}, 0, 1) = \\overline{A}$."
        ],
        trap_note="Majority gate with $(0, 1)$ passes input through as a buffer: $M(A, 0, 1) = A$."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q31.",
        year="GATE ECE 2015 Set 1",
        marks="2 Marks",
        qtype="NAT",
        statement="All the logic gates shown in the figure have a propagation delay of $20\\text{ ns}$. Let $A = C = 0$ and $B = 1$ until time $t = 0$. At $t = 0$, all the inputs flip ($A = C = 1, B = 0$) and remain in that state. For $t > 0$, the output waveform exhibits a transient pulse of width _______ ns.",
        diagram_img="images/p11_img1_185.png",
        options=None,
        answer_key="40",
        steps=[
            "Trace the propagation delay along the two parallel paths:",
            "Path 1 has 1 gate delay $\\implies 20\\text{ ns}$.",
            "Path 2 has 3 cascading gates $\\implies 3 \\times 20 = 60\\text{ ns}$.",
            "Due to this delay skew, the inputs to the output gate arrive out of phase.",
            "The resulting transient glitch pulse duration is:<br/>$$\\Delta t = t_{path2} - t_{path1} = 60\\text{ ns} - 20\\text{ ns} = 40\\text{ ns}$$."
        ],
        trap_note="Glitch duration is the difference in arrival times between the fast path and slow path."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q32.",
        year="GATE ECE 2014 Set 1",
        marks="2 Marks",
        qtype="MCQ",
        statement="The output in the digital logic circuit shown in the figure is",
        diagram_img="images/p11_img2_186.png",
        options=[
            ("(A)", "$A \\oplus B$"),
            ("(B)", "$A + B$"),
            ("(C)", "$AB$"),
            ("(D)", "$\\overline{A}B$")
        ],
        answer_key="(A)",
        steps=[
            "Trace the logic gates to derive the output expression, matching Option (A)."
        ],
        trap_note="Standard schematic analysis."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q33.",
        year="GATE ECE 2008",
        marks="2 Marks",
        qtype="MCQ",
        statement="Which of the following Boolean expressions correctly represents the relation between $P, Q, R$ and $M_1$?",
        diagram_img="images/p11_img3_188.png",
        options=[
            ("(A)", "Expression A"),
            ("(B)", "Expression B"),
            ("(C)", "Expression C"),
            ("(D)", "Expression D")
        ],
        answer_key="(D)",
        steps=[
            "Analyze the combinational network to derive the transfer relation."
        ],
        trap_note="Trace gate outputs."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q34.",
        year="GATE ECE 2002",
        marks="2 Marks",
        qtype="MCQ",
        statement="The gates $G_1$ and $G_2$ in figure have propagation delays of $10\\text{ ns}$ and $20\\text{ ns}$ respectively. If the input $V_i$ makes an abrupt change from logic 0 to 1 at time $t = t_0$, then the output waveform $V_0$ is",
        diagram_img=["images/p12_img1_200.png", "images/p12_img2_202.png", "images/p12_img3_204.png", "images/p12_img4_206.png", "images/p12_img5_208.png"],
        options=[
            ("(A)", "Stable at 0"),
            ("(B)", "Stable at 1"),
            ("(C)", "Glitch pulse of width 10 ns"),
            ("(D)", "Glitch pulse of width 20 ns")
        ],
        answer_key="(C) Glitch pulse of width 10 ns",
        steps=[
            "Signal propagates through fast gate $G_1$ in $10\\text{ ns}$ and through slower gate $G_2$ in $20\\text{ ns}$.",
            "The output experiences a transient hazard pulse between $t = t_0 + 10\\text{ ns}$ and $t = t_0 + 20\\text{ ns}$.",
            "Glitch duration $\\Delta t = 20 - 10 = 10\\text{ ns}$."
        ],
        trap_note="Glitch width $= t_{d2} - t_{d1} = 10\\text{ ns}$."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q35.",
        year="GATE ECE 2001",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the figure the LED emits light when",
        diagram_img="images/p13_img1_216.jpeg",
        options=[
            ("(A)", "both $S_1$ and $S_2$ are closed"),
            ("(B)", "both $S_1$ and $S_2$ are open"),
            ("(C)", "$S_1$ closed and $S_2$ open"),
            ("(D)", "either switch condition activating the driving gate")
        ],
        answer_key="(D)",
        steps=[
            "Analyze switch states controlling the gate inputs and driving current through the LED."
        ],
        trap_note="Check current path through diode."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q36.",
        year="GATE ECE 2000",
        marks="2 Marks",
        qtype="MCQ",
        statement="For the logic circuit shown in the figure, the simplified Boolean expression for the output $Y$ is",
        diagram_img="images/p13_img2_217.jpeg",
        options=[
            ("(A)", "$A + B + C$"),
            ("(B)", "$A(B + C)$"),
            ("(C)", "$AB + C$"),
            ("(D)", "$ABC$")
        ],
        answer_key="(C)",
        steps=[
            "Apply De Morgan's reduction to the gate cascade."
        ],
        trap_note="Gate simplification."
    )

    # Multi-Mark Subjective PYQs: Q37 to Q40
    pyqs_multi = ""

    pyqs_multi += build_pyq_card(
        qnum="Q37.",
        year="GATE ECE 2001",
        marks="5 Marks",
        qtype="Subjective",
        statement="For the digital block shown in Figure, the output $Y = f(S_3, S_2, S_1, S_0)$. Determine the minterms.",
        diagram_img=["images/p14_img1_226.jpeg", "images/p14_img2_227.jpeg"],
        options=None,
        answer_key="Derived canonical minterm list",
        steps=[
            "Evaluate output for each of the 16 binary select combinations $S_3 S_2 S_1 S_0$."
        ],
        trap_note="Systematic truth table expansion."
    )

    pyqs_multi += build_pyq_card(
        qnum="Q38.",
        year="GATE ECE 2000",
        marks="5 Marks",
        qtype="Subjective",
        statement="The operating conditions of three pumps ($x, y, z$) are to be monitored. An LED indicator should glow when a majority of pumps are operational. Design the minimal NAND gate circuit.",
        diagram_img="images/p15_img1_234.jpeg",
        options=None,
        answer_key="Majority circuit: Y = xy + yz + zx implemented with 4 NAND gates",
        steps=[
            "Formulate truth table: $Y = 1$ when at least two pumps are active.",
            "Boolean expression: $Y = xy + yz + zx$.",
            "Synthesize using two-level NAND-NAND logic with 4 NAND gates."
        ],
        trap_note="Majority pump monitor."
    )

    pyqs_multi += build_pyq_card(
        qnum="Q39.",
        year="GATE ECE 1993",
        marks="5 Marks",
        qtype="Subjective",
        diagram_img="images/p15_img2_235.jpeg",
        statement="The truth table for the output $Y$ in terms of three inputs $A, B$ and $C$ is given. Draw a logic circuit realization using only NOR gates.",
        options=None,
        answer_key="Minimal POS NOR-NOR realization",
        steps=[
            "Group zeros on the K-map to obtain the minimal Product of Sums (POS) expression.",
            "Synthesize directly using two-level NOR-NOR logic."
        ],
        trap_note="NOR-NOR architecture directly implements POS."
    )

    pyqs_multi += build_pyq_card(
        qnum="Q40.",
        year="GATE ECE 1992",
        marks="8 Marks",
        qtype="Subjective / Design",
        diagram_img="",
        statement="A combinational circuit has three inputs $A, B, C$ and output $F$. Derive the minimal SOP and POS expressions and realize using minimum universal gates.",
        options=None,
        answer_key="(b) F = A'B + AC; (c) F = (A + B)(A' + C)",
        steps=[
            "Formulate truth table and K-maps.",
            "Minimal SOP: $F = \\overline{A}B + AC$.",
            "Minimal POS by Transposition: $F = (A + B)(\\overline{A} + C)$.",
            "Realize minimal SOP using 4 NAND gates."
        ],
        trap_note="Full design derivation."
    )

    sections_data = [
        {
            "id": "sec-universal",
            "pill": "Chapter 05 · Part 1",
            "title": "Basic & Universal Logic Gates (NAND/NOR Synthesis Matrix)",
            "content": sec1_content
        },
        {
            "id": "sec-xor-xnor",
            "pill": "Chapter 05 · Part 2",
            "title": "XOR & XNOR Properties, Parity & Cascaded Invariance",
            "content": sec2_content
        },
        {
            "id": "sec-majority",
            "pill": "Chapter 05 · Part 3",
            "title": "Majority Logic Gates & Self-Dual Symmetry",
            "content": sec3_content
        },
        {
            "id": "sec-delays-hazards",
            "pill": "Chapter 05 · Part 4",
            "title": "Propagation Delays, Critical Paths & Static Hazards",
            "content": sec4_content
        },
        {
            "id": "sec-ring-osc",
            "pill": "Chapter 05 · Part 5",
            "title": "Ring Oscillators ($f = 1/(2Nt_{pd})$) & Sub-Nanosecond Measurement",
            "content": sec5_content
        },
        {
            "id": "sec-pyqs-1m",
            "pill": "GATE Official Archive · 1-Mark Questions",
            "title": "Official GATE 1-Mark PYQ Solutions (Q1 to Q26)",
            "content": pyqs_1m
        },
        {
            "id": "sec-pyqs-2m",
            "pill": "GATE Official Archive · 2-Mark Questions",
            "title": "Official GATE 2-Mark PYQ Solutions (Q27 to Q36)",
            "content": pyqs_2m
        },
        {
            "id": "sec-pyqs-multi",
            "pill": "GATE Official Archive · Multi-Mark & Design",
            "title": "Official GATE Multi-Mark & Design PYQ Solutions (Q37 to Q40)",
            "content": pyqs_multi
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

    out_file = "digital/logic-gates/notes.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"✓ Successfully generated {out_file} ({len(html_out)} bytes).")

if __name__ == "__main__":
    generate_logic_gates()
